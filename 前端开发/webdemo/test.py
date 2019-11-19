# coding=utf-8
class Movie:
    def __init__(self,movieid,moviename,score,poster):
        self.movieid=movieid
        self.moviename=moviename
        self.score=score
        self.poster=poster

for i in range(1,32):
    print("<option value =\""+str(i)+"\">"+str(i)+"</option>")