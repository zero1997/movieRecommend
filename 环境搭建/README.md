#基于大数据平台的电影推荐系统



## 一、节点任务分配（计划）

| 节点编号  | Web服务器 | 数据库   | hadoop&Spark                       |
| ----- | ------ | ----- | ---------------------------------- |
| node0 | √      |       | Datanode、NodeManager               |
| node1 |        | MySQL | Datanode、NodeManager               |
| node2 |        | Redis | Datanode、NodeManager               |
| node3 |        |       | Namenode、ResourceManager           |
| node4 |        |       | SecondaryNamenode、JobHistoryServer |






## 二、进度安排
### 10.27

完成各服务器python、Django、MySQL、Redis、java、scala等相关环境的搭建



### 11.4

完成hadoop集群和spark集群的搭建