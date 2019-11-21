# 基于大数据平台的电影推荐系统



## 一、节点任务分配（计划）

| 节点编号  | Web服务器 | 数据库          | hadoop&Spark&Zookeeper |
| ----- | ------ | ------------ | ---------------------- |
| node0 | √      |              | Datanode               |
| node1 |        | MySQL        | Datanode               |
| node2 |        |              | Datanode               |
| node3 |        | Hbase Master | Datanode               |
| node4 |        |              | Master、Datanode        |






## 二、进度安排

### 10.27

完成各服务器python、Django、MySQL、Redis、java、scala等相关环境的搭建



### 11.4

完成hadoop集群和spark集群的搭建



### 11.11

完成Hbase的搭建

# 运维笔记

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

ssh-copy-id hadoop@host

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

```shell
# java
export JAVA_HOME=/usr/lib/jvm/java-1.8.0
export PATH=$PATH:$JAVA_HOME/bin
```

### scala

sudo tar -zxvf scala-2.11.12.tgz -C /usr/local/
vim ~/.bashrc 

```shell
# scala
export SCALA_HOME=/usr/local/scala-2.11.12
export PATH=$PATH:$SCALA_HOME/bin
```

### hadoop

上传hadoop-2.6.0.tar.gz文件

在~/.bashrc中添加如下内容

```shell
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

```shell
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

```shell
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

```shell
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

```shell
# hbase
export HBASE_HOME=/usr/local/hbase-0.98.0-hadoop2
export PATH=$PATH:$HBASE_HOME/bin
```

\$HBASE_HOME/bin/start-hbase.sh启动hbase

hbase-daemon.sh start thrift 用来支持python访问hbase

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



# docker打包镜像

共5个docker 镜像，命名一致，但需要运行在不同机器上，分别记录node0 node1 node2 node3 node4的备份



sudo yum install docker-io

### 1_step. 进入to_docker目录，vim Dockerfile，文件内容如下

```docker
FROM centos:7

ENV JAVA_HOME /usr/lib/jvm/java-1.8.0
ENV PATH $PATH:$JAVA_HOME/bin

ADD scala-2.11.12.tar.gz /usr/local/
ENV SCALA_HOME /usr/local/scala-2.11.12
ENV PATH $PATH:$SCALA_HOME/bin

ADD spark-2.1.2-bin-hadoop2.6.tar.gz /usr/local/
ENV SPARK_HOME /usr/local/spark-2.1.2-bin-hadoop2.6
ENV PATH $PATH:$SPARK_HOME/lib

ADD zookeeper-3.4.6.tar.gz /usr/local/
ENV ZOOKEEPER_HOME /usr/local/zookeeper-3.4.6
ENV PATH $PATH:$ZOOKEEPER_HOME/bin

ADD hadoop-2.6.0.tar.gz /usr/local/
ENV HADOOP_HOME /usr/local/hadoop-2.6.0
ENV HADOOP_CONF_DIR $HADOOP_HOME/etc/hadoop
ENV CLASSPATH $($HADOOP_HOME/bin/hadoop classpath):$CLASSPATH
ENV LD_LIBRARY_PATH $HADOOP_HOME/lib/native/:$LD_LIBRARY_PATH
ENV PATH $HADOOP_HOME/bin:$PATH

ADD hbase-0.98.0-hadoop2.tar.gz /usr/local/
ENV HBASE_HOME /usr/local/hbase-0.98.0-hadoop2
ENV PATH $PATH:$HBASE_HOME/bin

RUN yum install -y which sudo vim less openssh-server openssh-clients net-tools expect wget java-1.8.0-openjdk-devel.x86_64 iptables-services

RUN echo "root    ALL=(ALL)       ALL" >> /etc/sudoers && \
    echo "hadoop  ALL=(ALL)       NOPASSWD:ALL" >> /etc/sudoers && \
    groupadd hadoop && useradd -m hadoop -g hadoop -p 123456 -s /bin/bash && \
    ssh-keygen -q -t rsa -b 2048 -f /etc/ssh/ssh_host_rsa_key -N '' && \
    ssh-keygen -q -t ecdsa -f /etc/ssh/ssh_host_ecdsa_key -N '' && \
    ssh-keygen -t dsa -f /etc/ssh/ssh_host_ed25519_key  -N '' && \
    sed -i "s/#UsePrivilegeSeparation.*/UsePrivilegeSeparation no/g" /etc/ssh/sshd_config && \
    sed -i "s/UsePAM.*/UsePAM no/g" /etc/ssh/sshd_config && \
    echo "123456" | passwd --stdin root && \
    echo "123456" | passwd --stdin hadoop

USER hadoop
```

### 2_step. 初始化image

sudo docker build -t init:v0 . # 初始化image

### 3_step. 根据刚刚初始化得到的image，启动容器temp_c 

sudo docker run --name temp_c -p 16022:22 -it init:v0 /bin/bash #实例化出container

之后完成ssh的配置并备份

/etc/hosts内容如下 

// 运行时按照需要进行修改

```hosts
0.0.0.0	localhost

172.26.240.222  node0
172.26.240.213  node1
172.26.240.224  node2
172.26.154.143  node3
172.26.240.212  node4
```



配置ssh

```shell
sudo /usr/sbin/sshd & #每次启动都要执行
ssh-keygen  #  一路回车
sudo vim /etc/hosts # 内容与
ssh-copy-id -p 16022  hadoop@nodeX
ssh -p 16022  hadoop@nodeX # 验证

# 更新下面两个文件，因宿主机需要占用22端口，所以用16022端口来作为docker上sshd服务使用的端口，此时需要修改hadoop、hbase的默认ssh端口

# 修改hadoop-env.sh
export HADOOP_SSH_OPTS="-p 16022" # 将hadoop集群的ssh端口映射到16022

# 修改hbase-env.sh ，具体暂不确定，未进行到此步骤
export_ssh_opts=“-p 16022”
```

### 4_step. 退出保存备份

control + D 退出

保存

sudo docker commit -m "bak" temp_c bak:v0



### 5_step. 完成可运行的docker

启动脚本启动刚刚保存的新镜像 bak:v0

```
sudo vim /etc/hosts
sudo /usr/sbin/sshd & #每次启动都要执行
sudo systemctl disable iptables.service 关闭防火墙
```



```
sudo docker run --name test_c -it \
-p 13562:13562 \
-p 60010:60010 \
-p 46121:46121 \
-p 8031:8031 \
-p 60000:60000 \
-p 50020:50020 \
-p 60020:60020 \
-p 34861:34861 \
-p 8042:8042 \
-p 19888:19888 \
-p 45777:45777 \
-p 40504:40504 \
-p 37227:37227 \
-p 50075:50075 \
-p 8030:8030 \
-p 8088:8088 \
-p 8032:8032 \
-p 33873:33873 \
-p 8033:8033 \
-p 8040:8040 \
-p 10020:10020 \
-p 2888:2888 \
-p 45241:45241 \
-p 10033:10033 \
-p 3306:3306 \
-p 50010:50010 \
-p 50090:50090 \
-p 60030:60030 \
-p 42691:42691 \
-p 50070:50070 \
-p 9000:9000 \
-p 2181:2181 \
-p 3888:3888 \
-p 35636:35636 \
-p 16022:22 \
-p 41999:41999 \
-p 9090:9090 \
-p 9095:9095 \
-p 8000:8000 \
bak:v0 /bin/bash
```





=============================分割线==============================

以上步骤均为5个节点上均需要执行的内容，后面涉及到各自特殊操作



各节点的特殊操作(按照执行顺序)

```
node1

以root用户
RUN wget http://repo.mysql.com/mysql-community-release-el7-5.noarch.rpm && \
    rpm -ivh mysql-community-release-el7-5.noarch.rpm && \
    yum -y update && \
    yum install -y mysql-server

MySQL正确的启动方式：
以hadoop用户
初始化数据库：	sudo mysql_install_db  --user=mysql
启动mysql：	sudo mysqld --user=mysql &
```



```
node4

bash /usr/local/hadoop-2.6.0/sbin/start-all.sh
bash /usr/local/hadoop-2.6.0/sbin/mr-jobhistory-daemon.sh start historyserver
```



```
在每个节点
zkServer.sh start # 先在node4的docker上执行，后在其它node上执行
```



```
node3

在$HBASE_HOME目录下
bin/start-hbase.sh #启动hbase
hbase-daemon.sh start thrift #用来支持python访问hbase
```



```
node0

配置python3环境，将web端相关代码放入到此docker中，并启动，理论上应该可以通过node0节点的8000端口看到和非docker情况下一样的web界面
```

