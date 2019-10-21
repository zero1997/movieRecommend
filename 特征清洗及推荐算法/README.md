## 基于大数据平台的电影推荐系统

### 算法板块

#### 数据

具体路径在~/movieRecommend/ft_local/ml-20m/*

- genome-scores.csv

  movieId,tagId,relevance
  1,1,0.025000000000000022
  1,2,0.025000000000000022
  1,3,0.057750000000000024
  1,4,0.09675
  1,5,0.14675
  1,6,0.21700000000000003
  1,7,0.067
  1,8,0.26275000000000004

- genome-tags.csv

  tagId,tag
  1,007
  2,007 (series)
  3,18th century
  4,1920s
  5,1930s
  6,1950s

- links.csv

  movieId,imdbId,tmdbId
  1,0114709,862
  2,0113497,8844
  3,0113228,15602

- movies.csv

  movieId,title,genres(类型)
  1,Toy Story (1995),Adventure|Animation|Children|Comedy|Fantasy
  2,Jumanji (1995),Adventure|Children|Fantasy
  3,Grumpier Old Men (1995),Comedy|Romance
  4,Waiting to Exhale (1995),Comedy|Drama|Romance

- ratings.csv

  userId,movieId,rating,timestamp
  1,2,3.5,1112486027
  1,29,3.5,1112484676
  1,32,3.5,1112484819
  1,47,3.5,1112484727
  1,50,3.5,1112484580

- tags.csv

  userId,movieId,tag,timestamp
  18,4141,Mark Waters,1240597180
  65,208,dark hero,1368150078
  65,353,dark hero,1368150079
  65,521,noir thriller,1368149983
  65,592,dark hero,1368150078
  65,668,bollywood,1368149876

#### 现有特征

- movie
  - movieId：编号为1，2，3
  - tagId及relevance：movieId和所有tag的关联程度，一个movieId对应的所有tag的分数都有
  - genres：movie的类型，一个movie可能有多个类型，用|隔开
- user
  - rating：用户对电影的打分以及打分的时间
  - tag：用户对电影的tag评价以及评价的时间

#### 过滤逻辑

- 过滤平均分数较低的电影
- 过滤观看人数过少的电影
- 过滤用户看过的电影

#### icf召回策略

1. 取用户评分最高的k部电影，每部电影召回相似性得分最高的x部电影，这样对一个用户可以召回k*x部电影
2. 对k*x部电影进行过滤，并按相似性得分进行排序，增加类别优化分布策略
3. 相似性得分计算：movie tags(长特征) ，采用余弦相似性，计算相似性得分

#### 热门内容推荐池

取平均分最高的电影，并对内容进行打散，优化类别分布 

#### 重排策略

##### 从未登录过的新用户

只从热门内容推荐池里进行召回文章

##### 有过登录的老用户

采用icf&热门内容推荐池的策略进行召回文章