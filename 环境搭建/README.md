# 基于大数据平台的电影推荐系统



## 一、节点任务分配（计划）

| 节点编号 | Web服务器 | 数据库       | hadoop&Spark&Zookeeper |
| -------- | --------- | ------------ | ---------------------- |
| node0    | √         |              | Datanode               |
| node1    |           | MySQL        | Datanode               |
| node2    |           | Redis        | Datanode               |
| node3    |           | Hbase Master | Datanode               |
| node4    |           |              | Master、Datanode       |






## 二、进度安排

### 10.27

完成各服务器python、Django、MySQL、Redis、java、scala等相关环境的搭建



### 11.4

完成hadoop集群和spark集群的搭建



### 11.11

完成Hbase的搭建

# 运维笔记（不完整版）

## 服务器情况

内存总计约3.5G

物理核数：1

逻辑核数：2

---

## 使用root账号

adduser hadoop

passwd hadoop

chmod u+w /etc/sudoers

vim /etc/sudoers

```
hadoop  ALL=(ALL)       NOPASSWD:ALL
```

chmod u-w /etc/sudoers

su hadoop

---

## 使用hadoop账号

cd ~

sudo yum update

sudo yum install -y tmux

mkdir temp

cd temp

wget https://repo.anaconda.com/archive/Anaconda3-2019.10-Linux-x86_64.sh

sh Anaconda3-2019.10-Linux-x86_64.sh

source ~/.bashrc

cd ~

---

### 配置免密登录

#### ssh-keygen

#### ssh-copy-id hadoop@host

ssh-copy-id hadoop@39.98.136.163

ssh-copy-id hadoop@39.100.226.136

ssh-copy-id hadoop@47.92.67.19

ssh-copy-id hadoop@39.99.140.90

ssh-copy-id hadoop@39.98.135.249

#### 更改hosts

sudo chmod u+w /etc/hosts

sudo vim /etc/hosts

```39.98.136.163	node0
0.0.0.0	localhost

172.26.240.222  node0
172.26.240.213  node1
172.26.240.224  node2
172.26.154.143  node3
172.26.240.212  node4
```

sudo chmod u-w /etc/hosts

---

### Java

sudo yum install java-1.8.0-openjdk-devel.x86_64

vim ~/.bashrc

```
# java
JAVA_HOME=/usr/lib/jvm/java-1.8.0
export PATH=$PATH:$JAVA_HOME/bin
```

### scala

sudo tar -zxvf scala-2.11.12.tgz -C /usr/local/
vim ~/.bashrc 

```
# scala
export SCALA_HOME=/usr/local/scala-2.11.12
export PATH=$PATH:$SCALA_HOME/bin
```

### hadoop

上传hadoop-2.6.0.tar.gz文件

在~/.bashrc中添加如下内容

```
# hadoop

export HADOOP_HOME=/usr/local/hadoop-2.6.0
export CLASSPATH=$($HADOOP_HOME/bin/hadoop classpath):$CLASSPATH
export PATH=/usr/local/hadoop-2.6.0/bin/:$PATH
```

sudo chown -R hadoop:hadoop /usr/local/hadoop-2.6.0/

将本地的hadoop_conf中的配置文件逐个传到服务器端

hdfs namenode -format

### spark

在.bashrc中添加如下内容

```
Spark

export SPARK_HOME=/usr/local/spark-2.1.2-bin-hadoop2.6
export PATH=${PATH}:${SPARK_HOME}/lib
export PATH=${PATH}:${SPARK_HOME}/bin
```

sudo tar -zxvf spark-2.1.2-bin-hadoop2.6.tgz -C /usr/local/

cd /usr/local/

chown -R hadoop:hadoop spark-2.1.2-bin-hadoop2.6

更改了${SPARK_HOME}/conf/slaves

类似于hadoop

在conf/spark-env.sh

```
export SPARK_HOME=/usr/local/spark-2.1.2-bin-hadoop2.6
export SCALA_HOME=/usr/local/scala-2.11.12
export JAVA_HOME=/usr/lib/jvm/java-1.8.0
export HADOOP_HOME=/usr/local/hadoop-2.6.0
export PATH=$PATH:$JAVA_HOME/bin:$HADOOP_HOME/bin:$HADOOP_HOME/sbin:$SCALA_HOME/bin
export HADOOP_CONF_DIR=$HADOOP_HOME/etc/hadoop
export YARN_CONF_DIR=$YARN_HOME/etc/hadoop
export SPARK_LOCAL_DIRS=/usr/local/spark-2.1.2-bin-hadoop2.6
export SPARK_DRIVER_MEMORY=1G
export SPARK_LIBARY_PATH=.:$JAVA_HOME/lib:$JAVA_HOME/jre/lib:$HADOOP_HOME/lib/native
```



// 如果不小心进入安全模式，解除命令为：hdfs dfsadmin -safemode leave

### hadoop 时间同步

sudo yum install -y ntp ntpdate

sudo vi /etc/ntp.conf

sudo systemctl enable ntpd.service


### Zookeeper

下载3.4.6，在.bashrc中添加

```
# zookeeper
export ZOOKEEPER_HOME=/usr/local/zookeeper-3.4.6
PATH=$PATH:$ZOOKEEPER_HOME/bin
```

在${ZOOKEEPER_HOME}中

在conf/zoo.cfg中添加如下内容

```
dataDir=/usr/local/zookeeper-3.4.6/data
dataLogDir=/usr/local/zookeeper-3.4.6/logs
server.1=node0:2888:3888
server.2=node1:2888:3888
server.3=node2:2888:3888
server.4=node3:2888:3888
server.5=node4:2888:3888
```

mkdir data

mkdir logs

echo 'x' > data/myid

在leader和follower中先后使用zkServer.sh start 命令启动zookeeper集群

### hbase

使用hadoop配置文件中的core-site.xml、hbase-env.sh、hbase-site.xml、hdfs-site.xml放入到\$HBASE_HOME/conf中，修改\$HBASE_HOME/conf/regionservers，类似于hadoop的slaves

在~/.bashrc中添加如下内容

```
# hbase
export HBASE_HOME=/usr/local/hbase-0.98.0-hadoop2
export PATH=$PATH:$HBASE_HOME/bin
```

\$HBASE_HOME/bin/start-hbase.sh启动hbase

hbase-daemon.sh start thrift

---

### Django in node0

pip install redis

pip install PyMysql

pip install Django

### mysql in node1

cd ~/wy/temp

wget http://repo.mysql.com/mysql-community-release-el7-5.noarch.rpm

rpm -ivh mysql-community-release-el7-5.noarch.rpm

yum update

yum install mysql-server

sudo systemctl start mysqld

sudo systemctl enable mysqld

mysql

mysql> GRANT ALL PRIVILEGES ON *.* TO 'root'@'%' WITH GRANT OPTION;

mysql> FLUSH PRIVILEGES;

mysql> exit;

### redis in node2

cd ~/wy/temp

sudo vim /etc/redis.conf

将bind 127.0.0.1改为： bind 0.0.0.0

sudo systemctl start redis

sudo systemctl enable redis

---

### docker 


yum install mysql-server

hadoop-env.sh

export HADOOP_SSH_OPTS="-p 16022"

echo "Port 11022" >> /etc/ssh/sshd_config

ports:

   - "8042:8042"
   - "19888:19888"
   - "50070:50070"  //Hadoop集群的webui地址
   - "8088:8088"  //Spark集群的webui地址
   - "9000:9000"
   - "9001:9001"
   - "2181:2181"
   - "16010:16010"  //HBase的webui地址
   - "16301:16301"
   - "16201:16201"
   - "4040:4040"
   - "8080:8080"
   - "18080:18080"



### Dockerfile

```
FROM centos:7

ADD java-1.8.0-openjdk.tar.gz /usr/local/
ENV JAVA_HOME /usr/local/java-1.8.0-openjdk
ENV PATH $JAVA_HOME/bin:$PATH

ADD scala-2.11.12.tar.gz /usr/local/
ENV SCALA_HOME /usr/local/scala-2.11.12
ENV PATH $PATH:$SCALA_HOME/bin

ADD spark-2.1.2-bin-hadoop2.6.tar.gz /usr/local/
ENV SPARK_HOME /usr/local/spark-2.1.2-bin-hadoop2.6
ENV PATH $PATH:$SPARK_HOME/lib

ADD zookeeper-3.4.6.tar.gz /usr/local/
ENV ZOOKEEPER_HOME /usr/local/zookeeper-3.4.6
ENV PATH $PATH:$ZOOKEEPER_HOME/bin

RUN yum install -y which sudo vim less openssh-server openssh-clients

RUN echo "root    ALL=(ALL)       ALL" >> /etc/sudoers && \
    echo "hadoop  ALL=(ALL)       NOPASSWD:ALL" >> /etc/sudoers && \
    groupadd hadoop && useradd -m hadoop -g hadoop -p 123456 -s /bin/bash && cd ~ && ssh-keygen \
    && sudo /usr/sbin/sshd -D
```

之后完成sshd启动，以及ssh-copy-id等等
