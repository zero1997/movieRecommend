package com.pku.evanyang

import org.apache.spark.{SparkConf, SparkContext}
import java.text.SimpleDateFormat
import scala.collection.mutable
import scala.collection.mutable.ArrayBuffer
/**
  * Created by evanoneyang on 2019/10/21.
  */
object movieScore {
  def main(args: Array[String]): Unit = {

    val sc = new SparkContext(new SparkConf().setAppName(getClass.getName))

    val fm = new SimpleDateFormat("yyyy-MM-dd HH:mm:ss").toString


    //score

    val userMovieScoreRdd = sc.textFile("/user/tesopzhang/video/data/ml-20m/ratings.csv")

      .zipWithIndex().filter(_._2>=1).keys

      .map{x =>

        val tokens = x.split(",")
        val userId = tokens(0).toInt
        val movieId = tokens(1).toInt
        val score = tokens(2).toDouble

        (userId, movieId, score)

      }

    val movieScoreRdd = userMovieScoreRdd.map(x=>(x._2, x._3)).groupByKey()

      .map(x=>(x._1, x._2.toArray.reduce(_+_)/x._2.size)).sortBy(_._1)

    /*结果示例
      * 2,3.5
        29,3.5
        32,3.5
        47,3.5
        50,3.5
      * */

      /*.map(x=>x._1+","+x._2)
      .saveAsTextFile(s"/user/tesopzhang/video/data/ml-20m/result/movieScore")*/


    //genres
    val movieGenresRdd = sc.textFile("/user/tesopzhang/video/data/ml-20m/genres.csv")

      .zipWithIndex().filter(_._2>=1).keys

      .map{x =>

        val tokens = x.split(",")
        val movieId = tokens(0).toInt
        val genres = tokens(2).split("\\|")(0)  //为了方便，暂时只取第一个类别作为电影的类别，这样也能避免重复推荐

        (movieId, genres)
      }


    /**
      * 热门推荐池：取出每个类别下评分最高的5部电影，然后再拉通按分数进行排序
      */

    val hotMovie = movieScoreRdd.join(movieGenresRdd).map(x => (x._2._2, (x._2._1, x._1)))  //genres,score,movieId

      .aggregateByKey(mutable.PriorityQueue[(Double, Int)]()(Ordering[Double].reverse.on(_._1)))(

      (a, i) => {
        a.enqueue(i)
        if (a.size > 5){
          a.dequeue()
        }
        a
      },
      (a1, a2) => {
        a1 ++= a2
        while(a1.size > 5) {
          a1.dequeue()
        }
        a1
      }
    ).flatMap{case(genres, movieGroup) => movieGroup.toArray}

        .map(x=> (x._2, x._1))  //movieid score


    /**
      * icf召回策略
      * 1. 取每个用户评分最高的k部电影，每部电影召回相似性得分最高的x部电影，这样对一个用户可以召回k*x部电影
        2. 对k*x部电影进行过滤，并按相似性得分进行排序，增加类别优化分布策略
        3. 相似性得分计算：movie tags(长特征) ，采用余弦相似性，计算相似性得分
      */

    //取每个用户评分最高的k部电影
    val userMovieGroupRdd = userMovieScoreRdd.map(x=>(x._1, (x._2, x._3)))

      .aggregateByKey(mutable.PriorityQueue[(Int, Double)]()(Ordering[Double].reverse.on(_._2)))(

        (a, i) => {
          a.enqueue(i)
          if (a.size > 5){
            a.dequeue()
          }
          a
        },
        (a1, a2) => {
          a1 ++= a2
          while(a1.size > 5) {
            a1.dequeue()
          }
          a1
        }
      )

    //每部电影召回相似性得分最高的x部电影
    val movieTagRelevanceRdd = sc.textFile("/user/tesopzhang/video/data/ml-20m/genome-scores.csv")

      .zipWithIndex().filter(_._2>=1).keys

      .map{x=>

        val tokens = x.split(",")
        val movieId = tokens(0).toInt
        val tagId = tokens(1).toInt
        val Releveance = tokens(2).toDouble

        (movieId, tagId, Releveance)
    }

    val rdd = movieTagRelevanceRdd.map(x => (x._1, x._3)).groupByKey().map(x=>(x._1, x._2.toArray)).collect()


      .combinations(2)

  }
}
