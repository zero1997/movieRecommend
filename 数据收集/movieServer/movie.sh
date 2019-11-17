#!/bin/bash
#cd ~/cm/movieServer
#Cd ~/course/云计算与大数据平台/movieServer

batch=20
sleep_time=30
start_num=$1 
movie_num=$2  #截止的电影数
cookiesChangeNum=5 # 爬多少个电影地址换一个ip

end_num=`expr $start_num + $batch`

while(($start_num<$movie_num))
do
    temp_end_num=`expr $start_num + $batch`
    if [ $temp_end_num -lt $movie_num ]
    then
        end_num=$temp_end_num
    else
        end_num=$movie_num
    fi
    scrapy crawl movieSpider -a start=$start_num -a end=$end_num -a cookiesChange=$cookiesChangeNum
    #python3 movieSelenium.py $start_num $end_num $ipChangeNum
    echo $(date +%F%n%T)
    echo $start_num 到 $end_num 已完成！
    echo "睡眠30秒..."
    
    sleep $sleep_time #睡眠
    start_num=$end_num
    if [ `expr $start_num % 100`  == 0 ]
    then
        echo $(date +%F%n%T) 
        echo "睡眠30秒..."
        sleep $sleep_time #睡眠
    fi

#    if [ `expr $start_num % 1000` == 0 ]
#    then
#        cat /dev/null>nohup.out # 清空日志文件
#    fi


done



