### 文件说明

- hotMovie

  热门内容推荐池，用于对未登录用户的推荐

- userMovieGroup_sort

  ucf召回池，用于对每个已登录的userId，推荐一批movie

  每行第一个为userId，后面为movieName，使用"\t"分割

- movieMovieGroup

  icf召回池，用于对每个movie，推荐一批相似的movie

  每行第一个为当前的movieName，后面为推荐的movieName，使用"\t"分割

- 注意

  - 所有的推荐内容，都要从当前推荐池中`随机`出
  - 对于movie推荐movie的情况，可能会重复推荐当前的movie，所以请在推荐的时候注意`去重`
  - 所有的movieId已经转换成了movieName

  

  