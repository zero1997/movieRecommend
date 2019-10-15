package com.pku.evanyang

import com.alibaba.fastjson.JSON
import com.tencent.omg.cf.InterRedisClient
import com.tencent.omg.utils.{safeToDouble, safeToInt, safeToLong}
import org.apache.hadoop.fs.Path
import org.apache.spark.{SparkConf, SparkContext}
import org.apache.spark.storage.StorageLevel
import com.tencent.omg.utils._

import scala.collection.mutable.ArrayBuffer

/**
  * Created by evanoneyang on 2019/3/19.
  */
object RecommendOrgVicfOneMore {
  def main(args: Array[String]): Unit = {
    val pathString1 = args(0)   //路径更改
    val topK = safeToInt(args(1))
    val lowClickAid1 = safeToInt(args(2)) //10
    val highClickAid1 = safeToInt(args(3))
    val lowViewNum1 = safeToInt(args(4)) //3
    val highViewNum1 = safeToInt(args(5)) //150
    val threshold = safeToDouble(args(6))
    val writeHdfs = args(7)
    val ifWriteHdfs = safeToInt(args(8)) //1 write or close
    val filterLargeNum = safeToInt(args(9)) //2000
    val dayNumInput = safeToInt(args(10)) //3
    val ifWriteRedis = safeToInt(args(11))
    val maxTotal = safeToInt(args(12)) //10
    val maxIdle = safeToInt(args(13)) //10
    val minIdle = safeToInt(args(14)) //1
    val redisTimeout = safeToInt(args(15)) //3000
    val outTime = safeToInt(args(16)) //172800
    val valueDay = safeToInt(args(17)) //3
    val eachUserPairNum = safeToInt(args(18)) //4000
    val newskeyStrAdd = args(19)
    val writeRedisServer = args(20)
    val ifWriteFilterClickData = safeToInt(args(21))
    val writeFilterClickData = args(22)
    val vidFile = args(23)
    val aIndexPathFile = args(24)
    val writeHdfs_video = args(25)
    val vIndexPathFile = args(26)
    val videokeyStrAdd = args(27)


    org.apache.hadoop.fs.FileSystem.get(new org.apache.hadoop.conf.Configuration()).delete(new Path(writeHdfs), true)
    org.apache.hadoop.fs.FileSystem.get(new org.apache.hadoop.conf.Configuration()).delete(new Path(writeHdfs_video), true)

    val sc = new SparkContext(new SparkConf().setAppName(getClass.getName))

    val rddLog = sc.textFile(pathString1)

    val rddClick = rddLog.map{ line =>
      val tokens = line.split("\t",-1)

      if(tokens.size >= 6){
        val deviceId = tokens(2)
        val newsId = tokens(4)
        var Type = ""

        if(isValidAid(newsId)) Type = "1"
        else if(isValidVid(newsId)) Type = "2"

        (deviceId, (newsId, Type))
      }
      else null


    }.filter{x=> x != null && (x._1 != "" && x._2._1 != "" && x._2._2 != "")}.distinct().persist(StorageLevel.MEMORY_AND_DISK)





    /*println("newid cnt:",rddClick.map(_._2._1).distinct().count())
    println("news cnt:", rddClick.filter(_._2._2 == "1").map(_._2._1).distinct().count())
    println("videos cnt:", rddClick.filter(_._2._2 == "2").map(_._2._1).distinct().count())
    println("users: num")
    rddClick.groupByKey().map(x => (x._1, x._2.size)).sortBy(_._2, false).take(100).foreach(println)
    println("news: num")
    rddClick.map(x => (x._2._1, x._1)).groupByKey().map(x => (x._1, x._2.size)).sortBy(_._2, false).take(100).foreach(println)*/

    //val test = rddClick.map(x => (x._2, 1)).reduceByKey()
    val lowClickAids = rddClick.map(x => (x._2, 1)).reduceByKey(_+_).filter{case (sAid, num) =>
      num <= lowClickAid1 || num >= highClickAid1
    }

    val lowViewUser = rddClick.map(x => (x._1, 1)).reduceByKey(_ + _).filter{case (sDevid, num) =>
      num <= lowViewNum1 || num >= highViewNum1
    }


    val rddFilterClick1 = rddClick.map(x => (x._2, x._1)).subtractByKey(lowClickAids).map(x => (x._2, x._1))//删除lowClickAids
    //DeviceId, newsId

    val rddFilterClick = rddFilterClick1.subtractByKey(lowViewUser).persist(StorageLevel.MEMORY_AND_DISK_SER)
    rddFilterClick.count
    //变为(设备号,(文章号,type))

    //println("filter newid cnt:",rddFilterClick.map(_._2._1).distinct().count())

    rddClick.unpersist()

    val validNewsTmp = sc.textFile(aIndexPathFile).map{ line =>
      parseNewsInfo(line)
    }
    val bValidNewsId= sc.broadcast(validNewsTmp.collect().toSet)
    //推荐平台的aid,用来做交集过滤

    val validVideosTmp = sc.textFile(vIndexPathFile).map{ line =>
      parseNewsInfo_video(line)
    }
    val bValidVideosId= sc.broadcast(validVideosTmp.collect().toSet)
    //推荐平台的vid,用来做交集过滤

    val rddNewsReadNum = rddFilterClick.map(x => (x._2._1, 1)).reduceByKey(_ + _) //每篇文章的数量
    val newsReadNum = rddNewsReadNum.collectAsMap()
    val bNewsReadNum = sc.broadcast(newsReadNum)


    /*println("filterLargeNum: ")
    rddFilterClick.groupByKey().map(x => (x._1, x._2.size)).sortBy(_._2, false).take(100).foreach(println)*/

    //(设备号,(文章号,type))
    val rddPairwiseNewsTmp = rddFilterClick.aggregateByKey(ArrayBuffer[(String, String)]())(
      (u, v) => {
        if (u.size < filterLargeNum)
          u += v
        u
      },
      (u1, u2) => {
        u1 ++= u2
        if(u1.size > filterLargeNum){
          val len = u1.length
          u1.remove(0, len - filterLargeNum)
        }
        u1
      }
    )


    //TLNewsIndex 图文

    val rddPairwiseNews = rddPairwiseNewsTmp.map{case(users, news)=>
      //val pairNews = new ArrayBuffer[((Int, Int), Int)]()
      val pairNews = new ArrayBuffer[((String, String), Int)]()
      val newsSet = news.toSet //(文章id,type)

      val validnews = newsSet.filter(x=>x._2=="1").map(_._1).intersect(bValidNewsId.value)
      val invalidnews = newsSet.map(_._1).diff(validnews)
      var bool = true
      validnews.toArray.combinations(2).foreach{x=>  //两两组合
        if (bool) {
          pairNews += Tuple2((x(0), x(1)), 1)
          pairNews += Tuple2((x(1), x(0)), 1)
          if(pairNews.size > eachUserPairNum){
            bool = false
          }
        }
      }
      invalidnews.foreach { x =>
        validnews.foreach { y =>
          if(bool) {
            pairNews += Tuple2((x, y), 1)
            if(pairNews.size > eachUserPairNum){
              bool = false
            }
          }
        }

      }

      pairNews
    }

    val rddPairNewsResTmp = rddPairwiseNews.flatMap(x => x).reduceByKey(_+_   //（文章id1，文章id2）, 重复数量
    ).filter{ case(x,y) => if(y > 3) true else false
    }.persist(StorageLevel.MEMORY_AND_DISK)

    //news1和news2相同的
    val rddPairNewsRes = rddPairNewsResTmp.map{case((news1, news2), sum) =>
      val score = sum.toDouble/math.sqrt(bNewsReadNum.value.get(news1).get.toDouble*bNewsReadNum.value.get(news2).get.toDouble) // 组合数/sqrt（数量1*数量2）
      (news1, (news2, score))
    }

    val rddNewsScore = rddPairNewsRes.filter{case(news1Id, (news2Id, score)) =>
      score > threshold
    }

    //每个文章(id,type)后面跟一串文章(id,type)和score
    val simsNews = rddNewsScore.aggregateByKey(ArrayBuffer[(String, Double)]())(
      (a, i) => {
        var b = ArrayBuffer[(String, Double)]()

        a += i
        b = a
        if(b.size > topK){
          b = b.sortWith(_._2 < _._2)
          b.remove(0)
        }

        b
      },
      (a1, a2) => {
        var c = ArrayBuffer[(String, Double)]()
        c = a1 ++ a2
        while(c.size > topK){
          c = c.sortWith(_._2 < _._2)
          c.remove(0)
        }
        c
      }
    )


    val sims = simsNews.map{case(news, scores) =>
      val arr = scores.sortWith(_._2>_._2).map{case(x,y) =>
        val str = "%s:%.8f".format(x, y)
        str
      }
      val strResult = arr.mkString(",")
      (news, strResult)
    }.filter{case(x,y) => y!=""}




    if(ifWriteRedis==1) {
      sims.map {case (key, value) =>
        (key + newskeyStrAdd, value)
      }.foreachPartition { partRecord =>
        InterRedisClient.makePool(writeRedisServer, redisTimeout, maxTotal, maxIdle, minIdle)
        val jedis = InterRedisClient.getPool.getResource

        partRecord.foreach {case (newsId, simNews) =>
          if (simNews != "") {
            jedis.setex(newsId, outTime, simNews)
          }
        }
        InterRedisClient.getPool.returnResource(jedis)
      }
    }



    if(ifWriteHdfs == 1) {
      sims.map { case (key, value) =>
        key + "\t" + value
      }.saveAsTextFile(writeHdfs)
    }


    //TLVideoIndex 视频

    val rddPairwiseVideos = rddPairwiseNewsTmp.map{case(users, news)=>
      //val pairNews = new ArrayBuffer[((Int, Int), Int)]()
      val pairNews = new ArrayBuffer[((String, String), Int)]()
      val newsSet = news.toSet //(文章id,type)

      val validvideos = newsSet.filter(x=>x._2=="2").map(_._1).intersect(bValidVideosId.value)
      val invalidvideos = newsSet.map(_._1).diff(validvideos)
      var bool = true
      validvideos.toArray.combinations(2).foreach{x=>  //两两组合
        if (bool) {
          pairNews += Tuple2((x(0), x(1)), 1)
          pairNews += Tuple2((x(1), x(0)), 1)
          if(pairNews.size > eachUserPairNum){
            bool = false
          }
        }
      }
      invalidvideos.foreach { x =>
        validvideos.foreach { y =>
          if(bool) {
            pairNews += Tuple2((x, y), 1)
            if(pairNews.size > eachUserPairNum){
              bool = false
            }
          }
        }

      }

      pairNews
    }

    val rddPairVideosResTmp = rddPairwiseVideos.flatMap(x => x).reduceByKey(_+_   //（文章id1，文章id2）, 重复数量
    ).filter{ case(x,y) => if(y > 3) true else false
    }.persist(StorageLevel.MEMORY_AND_DISK)

    //news1和news2相同的
    val rddPairVideosRes = rddPairVideosResTmp.map{case((news1, news2), sum) =>
      val score = sum.toDouble/math.sqrt(bNewsReadNum.value.get(news1).get.toDouble*bNewsReadNum.value.get(news2).get.toDouble) // 组合数/sqrt（数量1*数量2）
      (news1, (news2, score))
    }

    val rddVideosScore = rddPairVideosRes.filter{case(news1Id, (news2Id, score)) =>
      score > threshold
    }

    //每个文章(id,type)后面跟一串文章(id,type)和score
    val simsVideos = rddVideosScore.aggregateByKey(ArrayBuffer[(String, Double)]())(
      (a, i) => {
        var b = ArrayBuffer[(String, Double)]()

        a += i
        b = a
        if(b.size > topK){
          b = b.sortWith(_._2 < _._2)
          b.remove(0)
        }

        b
      },
      (a1, a2) => {
        var c = ArrayBuffer[(String, Double)]()
        c = a1 ++ a2
        while(c.size > topK){
          c = c.sortWith(_._2 < _._2)
          c.remove(0)
        }
        c
      }
    )


    val sims_videos = simsVideos.map{case(news, scores) =>
      val arr = scores.sortWith(_._2>_._2).map{case(x,y) =>
        val str = "%s:%.8f".format(x, y)
        str
      }
      val strResult = arr.mkString(",")
      (news, strResult)
    }.filter{case(x,y) => y!=""}




    if(ifWriteRedis==1) {
      sims_videos.map {case (key, value) =>
        (key + videokeyStrAdd, value)
      }.foreachPartition { partRecord =>
        InterRedisClient.makePool(writeRedisServer, redisTimeout, maxTotal, maxIdle, minIdle)
        val jedis = InterRedisClient.getPool.getResource

        partRecord.foreach {case (newsId, simNews) =>
          if (simNews != "") {
            jedis.setex(newsId, outTime, simNews)
          }
        }
        InterRedisClient.getPool.returnResource(jedis)
      }
    }




    if(ifWriteHdfs == 1) {
      sims_videos.map { case (key, value) =>
        key + "\t" + value
      }.saveAsTextFile(writeHdfs_video)
    }




  }


  def parseNewsInfo(line:String) = {

    var pt = -1L
    var title = ""
    var aid = ""
    var app_ch = ""

    try {
      val jsonMap = JSON.parseObject(line)

      if (jsonMap.containsKey("APP_CH")){
        val chSet = jsonMap.getJSONArray("APP_CH").toArray().toSet
        if (chSet.contains("daily_timeline")) {
          app_ch = "daily_timeline"
        }
      }


      if (jsonMap.containsKey("ID")){
        aid = jsonMap.getString("ID")
      }

    }
    catch {
      case ex: Exception =>
        println("parse json err: " + line)
    }
    if (aid.nonEmpty && app_ch.nonEmpty)
      aid
    else  null
  }

  def parseNewsInfo_video(line:String) = {

    var pt = -1L
    var title = ""
    var vid = ""
    var app_ch = ""

    try {
      val jsonMap = JSON.parseObject(line)

      if (jsonMap.containsKey("APP_CH")){
        val chSet = jsonMap.getJSONArray("APP_CH").toArray().toSet
        if (chSet.contains("daily_timeline")) {
          app_ch = "daily_timeline"
        }
      }


      if (jsonMap.containsKey("ID")){
        vid = jsonMap.getString("ID")
      }

    }
    catch {
      case ex: Exception =>
        println("parse json err: " + line)
    }
    if (vid.nonEmpty && app_ch.nonEmpty)
      vid
    else  null
  }

  def isValidAid(sAid: String) = {
    (sAid.length == 16 && sAid.toCharArray.getOrElse(8,' ') == 'A') || (sAid.length == 19 && sAid.substring(0, 4) != "CELL"  && sAid.toCharArray.getOrElse(11,' ') == 'A')
  }

  def isValidVid(sAid: String) = {
    (sAid.length == 16 && sAid.toCharArray.getOrElse(8,' ') == 'V') || (sAid.length == 19 && sAid.substring(0, 4) != "CELL"  && sAid.toCharArray.getOrElse(11,' ') == 'V')
  }

}
