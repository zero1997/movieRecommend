package com.pku.evanyang

import org.apache.spark.{SparkConf, SparkContext}
import java.text.SimpleDateFormat

/**
  * Created by evanoneyang on 2019/10/21.
  */
object movieScore {
  def main(args: Array[String]): Unit = {

    val sc = new SparkContext(new SparkConf().setAppName(getClass.getName))

    val fm = new SimpleDateFormat("yyyy-MM-dd HH:mm:ss").toString

    val movieScoreRdd = sc.textFile("/user/tesopzhang/video/data/ml-20m/ratings.csv").map{x =>

      val tokens = x.split(",")
      val movieId = tokens(1).toInt
      val score = tokens(2).toDouble

      (movieId, score)

    }.groupByKey().map(x=>(x._1, x._2.toArray.reduce(_+_)/x._2.size)).sortBy(_._1).map(x=>x._1+","+x._2)




      .saveAsTextFile(s"/user/tesopzhang/video/data/ml-20m/result/movieScore+$fm.csv")


  }
}
