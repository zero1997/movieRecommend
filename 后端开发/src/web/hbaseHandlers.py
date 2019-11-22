# -*- coding: utf-8 -*-
import happybase
from urllib import parse
import json
from random import shuffle
import csv
class recomHandler:
    conn = happybase.Connection("39.99.140.90", 9090)
    u2mfile = "/home/hadoop/lyn/webdemo/web/userMovieGroup_sort.txt"
    m2mfile = "/home/hadoop/lyn/webdemo/web/movieMovieGroup.txt"
    hotfile = "/home/hadoop/lyn/webdemo/web/hotMovie.txt"
    indexfile = "/home/hadoop/lyn/webdemo/web/movies.csv"
    ratingfile = "/home/hadoop/lyn/webdemo/web/ratings.csv"
    presentfile = "/home/hadoop/lyn/webdemo/web/presentMovies.txt"
    touristid = -1

    def loadRating(self):

        presentSet = {}
        with open(self.presentfile,mode='r',encoding='utf-8') as f:
            for line in f:
                presentSet[str(line[:-1])] = [0.0,0]

        with open(self.ratingfile,mode='r',encoding='utf-8') as f:
            reader = csv.reader(f)
            i = 0
            for row in reader:
                if i==0:
                    i += 1
                    continue
                if row[1] in presentSet.keys():
                    presentSet[row[1]][0] += float(row[2])
                    presentSet[row[1]][1] += 1
                i+=1
                if i%10000==0:
                    print(i)
        print(presentSet['1'])
        table = self.conn.table("movies")
        cols = ["score:score"]
        for d,v in presentSet.items():
            data = {}
            if v[1]!=0:
                data["score:score"] = "%f,%d"%(v[0]/v[1],v[1])
            else:
                data["score:score"] = "0.0,0"
            print(data)
            print(d)
            table.put(d,data)

    def getRecomList(self,userid):
        res = set()
        table=self.conn.table("hot")
        row = table.row(str(self.touristid))
        rows = str(row[b"list:hot"],encoding="utf-8").split(',')
        m = [int(x) for x in rows]
        shuffle(m)
        print(m)
        if userid == self.touristid:
            return m[:18]
        table2 = self.conn.table("recom")
        row = table2.row(str(userid))
        print(row)
        rows = str(row[b"list:recom"],encoding="utf-8").split(',')
        rec = [int(x) for x in rows]
        shuffle(rec)
        for x in range(6):
            res.add(m[x])
        i = 0
        while len(res)<18 and (i < len(rec)):
            res.add(rec[i])
            i += 1
        i = 6
        while len(res)<18 and (i<len(m)):
            res.add(m[i])
            i+=1
        i = 1
        while len(res)<18:
            res.add(i)
        return list(res)

    def loadRecom(self):

        str2index = {}
        with open(self.indexfile,mode='r',encoding='utf-8') as f:
            reader = csv.reader(f)
            i = 0
            for row in reader:
                str2index[row[1].replace('"','').strip()] = int(row[0])
                i += 1
            print(i)

        presentSet = set()
        with open(self.presentfile,mode='r',encoding='utf-8') as f:
            for line in f:
                presentSet.add(int(line[:-1]))
        print(len(presentSet))
        

        hotmovie=[]
        with open(self.hotfile,mode='r',encoding="utf-8") as f:
            for line in f:
                if int(str2index[line[:-1]]) in presentSet:
                    hotmovie.append(str(str2index[line[:-1]]))
        print(len(hotmovie))
        self.insertHOT(1,hotmovie)

        with open(self.m2mfile,mode="r",encoding='utf-8') as f:
            for line in f:
                names = line[:-1].split("\t")
                movieid = str2index[names[0].replace('"','').strip()]
                tmp = []
                for x in names[1:]:
                    if int(str2index[x.replace('"','').strip()]) in presentSet:
                        tmp.append(str(str2index[x.replace('"','').strip()]))
                self.insertM2M(movieid,tmp)


        with open(self.u2mfile,mode='r',encoding="utf-8") as f:
            i = 0
            for line in f:
                names = line[:-1].split("\t")
                userid = int(names[0])
                tmp = []
                #print(names)
                for x in names[1:]:
                    if int(str2index[x.replace('"','').strip()]) in presentSet:
                            tmp.append(str(str2index[x.replace('"','').strip()]))
                self.insertU2M(userid,tmp)
                i += 1
                if i%10000==0:
                    print(i)

                

    def insertU2M(self,userid,recom_list):
        d={}
        table=self.conn.table("recom")
        d["list:recom"] = ','.join(recom_list)
        #print("inserting to recom:",d,userid)
        table.put(str(userid),d)
    
    def insertHOT(self,userid,recom_list):
        d={}
        table=self.conn.table("hot")
        d["list:hot"] = ','.join(recom_list)
        #print("inserting to hot:",d,userid)
        table.put(str(self.touristid),d)
    
    def insertM2M(self,movieid,recom_list):
        d={}
        table=self.conn.table("m2m")
        d["list:m2m"] = ','.join(recom_list)
        #print("inserting to m2m:",d,movieid)
        table.put(str(movieid),d)
    
    

class movieHandler:
    cols = ["identity:names","score:score"]
    conn = happybase.Connection("39.99.140.90", 9090)
    def insertMovie(self,movieid,data):
        table = self.conn.table("movies")
        table.put(str(movieid),data)
    
    def getMovieDetail(self,movieid):
        table = self.conn.table("movies")
        row = table.row(str(movieid))
        return row
    
    def getMovie(self,movieids):
        table = self.conn.table("movies")
        row = table.row([str(x) for x in movieids],columns=self.cols)
        return row
    
    def removeMovie(self,movieid):
        table = self.conn.table("movies")
        table.delete(str(movieid))

class crawlerHandler:
    filepath = "/home/hadoop/cm/movieInfo/movieInfo%d"
    def importMovies(self,mh):
        wf = []
        wff = open("./presentMovies.txt",mode="w",encoding="utf-8")
        for i in range(4):
            with open(self.filepath%(i+1),mode='r') as f:
                for line in f:
                    data = json.loads(line[:-1])
                    d = {}
                    d["identity:id"] = str(data["movieId"])
                    d["identity:names"] = data["movieNameDouban"].strip()
                    d["score:score"] = "5.0"
                    d["creation:director"] = ",".join([x.strip() for x in data["director"]])
                    d["creation:actor"] = ",".join([x.strip() for x in data["mainActor"]])
                    d["creation:scriptwriter"] = ",".join([x.strip() for x in data["scriptwriter"]])
                    d["basic:filmType"] = ",".join([x.strip() for x in data["filmType"]])

                    if data["countryArea"]:
                        d["basic:area"] = data["countryArea"].strip()
                    else:
                        d["basic:area"] = "不详"

                    if data["language"]:
                        d["basic:language"] = data["language"].strip()
                    else:
                        d["basic:language"] = "不详"

                    if data["date"]:
                        d["basic:date"] = data["date"].strip()
                    else:
                        d["basic:date"] = "不详"

                    if data["filmDuration"]:
                        d["basic:duration"] = data["filmDuration"].strip()
                    else:
                        d["basic:duration"] = "不详"

                    if data["filmSummary"]:
                        d["text:summary"]=data["filmSummary"].strip()
                    else:
                        d["text:summary"] = "暂无"

                    d["text:comments"] = "|*|".join([x.strip() for x in data["comments"]])
                    d["text:url"] = data["morePosterUrl"]
                    mh.insertMovie(str(data["movieId"]),d)
                    print(data["movieId"])
                    wf.append(data["movieId"])
        wf.sort()
        for num in wf:
            wff.write(str(num)+'\n')
#conn.create_table('movies',{"identity":{},"score":{},
#                   "creation":{},"basic":{},
#                   "text":{}})
#conn.create_table('hot',{"list":{}})
#conn.create_table('recom',{"list":{}})
#conn.create_table('m2m',{"list":{}})
#print(conn.tables())





