package com.pku.evanyang

import org.apache.spark.{SparkConf, SparkContext}

object movieRecommend {
  def main(args: Array[String]): Unit = {

    val sc = new SparkContext(new SparkConf().setAppName(getClass.getName))


  }
}
