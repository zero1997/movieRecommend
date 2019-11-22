# _*_ coding: utf-8 _*_
from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from django.shortcuts import render
from .userHandlers import userHandler
from .hbaseHandlers import movieHandler,recomHandler
from .redisHandler import feedHandler
import logging
logger = logging.getLogger('django')
class Movie:
    def __init__(self,movieid,moviename,score,poster):
        self.movieid=movieid
        self.moviename=moviename
        self.score=score
        self.poster=poster

d=[]

# Create your views here.
def index(request):
    #return render(request,'index.html')
    return render(request,'changeInformation.html')

def hot(request):
    #return render(request,'index.html')
    uid = -1
    rh = recomHandler()
    movieids=rh.getRecomList(uid)
    print("movieid",movieids)
    movie = []
    mh = movieHandler()
    for i in movieids:
        row = mh.getMovieDetail(str(i))
        rowscore = row[b"score:score"].decode().split(',')
        if len(rowscore)>1:
            score="%s (%s人评分)"%(rowscore[0],rowscore[1])
        else:
            score="3.924612 (47人评分)"
        movie.append(Movie(i,row[b"identity:names"].decode(),score,'image/pic/%d.jpg'%i))
    d={}
    for i in range(18):
        d["movie%d"%i] = movie[i]
    print(d)
    return render(request,'hotRecommend.html',d)
	
def recommend(request):
    #return render(request,'index.html')
    if "uid" in request.session.keys():
        uid = request.session["uid"]
    else:
        uid = -1
    rh = recomHandler()
    movieids=rh.getRecomList(uid)
    print("movieid",movieids)
    movie = []
    mh = movieHandler()
    for i in movieids:
        row = mh.getMovieDetail(str(i))
        rowscore = row[b"score:score"].decode().split(',')
        if len(rowscore)>1:
            score="%s (%s人评分)"%(rowscore[0],rowscore[1])
        else:
            score="3.924612 (47人评分)"
        movie.append(Movie(i,row[b"identity:names"].decode(),score,'image/pic/%d.jpg'%i))
    d={}
    for i in range(18):
        d["movie%d"%i] = movie[i]
    print(d)
    return render(request,'recommend.html',d)

def rOrL(request):
    #return render(request,'index.html')
    return render(request,'index.html')

def detail(request):
    if request.method == 'POST':
        mid = request.POST.get('movieid')
    print(mid)
    #return render(request,'index.html')
    mh = movieHandler()
    #mid = request.POST.get("moiveid")
    row = mh.getMovieDetail(str(mid))
    movieid=mid
    movieName=row[b"identity:names"].decode()
    score=row[b"score:score"].decode().split(',')
    if len(score)>1:
        score="%s (%s人评分)"%(score[0],score[1])
    else:
        score="3.924612 (47人评分)"
    poster='image/pic/%s.jpg'%mid
    director=row[b"creation:director"].decode()
    scripwriter=row[b"creation:scriptwriter"].decode()
    mainActor=row[b"creation:actor"].decode()
    filmType=row[b"basic:filmType"].decode()
    area=row[b"basic:area"].decode()
    language=row[b"basic:language"].decode()
    pubDate=row[b"basic:date"].decode()
    duration=row[b"basic:duration"].decode()
    summary=row[b"text:summary"].decode()
    comments=row[b"text:comments"].decode().split("|*|")
    print(comments)
    referenceUrl=row[b"text:url"].decode().split("photo")[0]
    print("director",director)
    print("scriptwriter",scripwriter)
    return render(request,'detail.html',{"movieid":movieid,"movieName":movieName,"score":score,"poster":poster,"director":director,"scripwriter":scripwriter,"mainActor":mainActor,"filmType":filmType,"area":area,"language":language,"pubDate":pubDate,"duration":duration,"summary":summary,"comments":comments,"referenceUrl":referenceUrl})

def watch(request):
    if request.method == 'POST':
        mid = request.POST.get('movieid')
    if "uid" in request.session.keys():
        uid = request.session["uid"]
    else:
        uid = -1
    
    fh = feedHandler()
    fh.hbaseSave(int(uid),int(mid),1)
    #return render(request,'index.html')
    return render(request,'www.baidu.com')

def dislike(request):
    if request.method == 'POST':
        mid = request.POST.get('movieid')
    if "uid" in request.session.keys():
        uid = request.session["uid"]
    else:
        uid = -1
    
    fh = feedHandler()
    fh.hbaseSave(int(uid),int(mid),0)

    rh = recomHandler()
    movieids=rh.getRecomList(uid)
    print("movieid",movieids)
    movie = []
    mh = movieHandler()
    for i in movieids:
        row = mh.getMovieDetail(str(i))
        rowscore = row[b"score:score"].decode().split(',')
        if len(rowscore)>1:
            score="%s (%s人评分)"%(rowscore[0],rowscore[1])
        else:
            score="3.924612 (47人评分)"
        movie.append(Movie(i,row[b"identity:names"].decode(),score,'image/pic/%d.jpg'%i))
    d={}
    for i in range(18):
        d["movie%d"%i] = movie[i]
    print(d)
    return render(request,"recommend.html")
    
def loginTest(request):
    if request.method == 'POST':
        name = request.POST.get('username1')
        pwd = request.POST.get('password1')
    uh = userHandler()
    status,info,userid,username=uh.userLoginCheck(name,pwd)
    request.session["uid"] = int(userid)
    request.session["uname"] = username
    request.session["logged"] = 1
    if "uid" in request.session.keys():
        uid = request.session["uid"]
    else:
        uid = -1
    rh = recomHandler()
    movieids=rh.getRecomList(uid)
    print("movieid",movieids)
    movie = []
    mh = movieHandler()
    for i in movieids:
        row = mh.getMovieDetail(str(i))
        rowscore = row[b"score:score"].decode().split(',')
        if len(rowscore)>1:
            score="%s (%s人评分)"%(rowscore[0],rowscore[1])
        else:
            score="3.924612 (47人评分)"
        movie.append(Movie(i,row[b"identity:names"].decode(),score,'image/pic/%d.jpg'%i))
    d={}
    for i in range(18):
        d["movie%d"%i] = movie[i]
    print(d)
    return render(request, 'recommend.html',d)

def changeInformation(request):
    #return render(request,'index.html')
    return render(request,'changeInformation.html')

def modifyTest(request):
    if request.method == 'POST':
        gender = request.POST.get('gender')
        age1 = request.POST.get('birthdayYear')
        age2 = request.POST.get('birthdayMonth')
        age3 = request.POST.get('birthdayDay')
        city = request.POST.get('city')
    uid = request.session["uid"]
    uname = request.session["uname"]
    gender2 = 1
    if gender == "男":
        gender2 = 1
    else:
        gender2 = 0
    print(age1,age2,age3)
    age = '-'.join([age1,age2,age3])
    
    uh = userHandler()
    uh.modifyInfo(uid,uname,age,city,gender2)

    if "uid" in request.session.keys():
        uid = request.session["uid"]
    else:
        uid = -1
    rh = recomHandler()
    movieids=rh.getRecomList(uid)
    print("movieid",movieids)
    movie = []
    mh = movieHandler()
    for i in movieids:
        row = mh.getMovieDetail(str(i))
        movie.append(Movie(i,row[b"identity:names"].decode(),row[b"score:score"].decode(),'image/pic/%d.jpg'%i))
    d={}
    for i in range(18):
        d["movie%d"%i] = movie[i]
    print(d)
    return render(request, 'recommend.html',d)

def registerTest(request):
    if request.method == 'POST':
        name = request.POST.get('username')
        pwd = request.POST.get('password')
        pwd2=request.POST.get('password2')
    uh = userHandler()
    userid,status,infos = uh.userCreate(name,pwd)
    logger.info(status)
    logger.info(userid)
    logger.info(infos)

    return render(request, 'index.html')


def information(request):
    years = range(1999,2019)
    uid = request.session["uid"]
    uh = userHandler()
    tmp = uh.getInfo(uid)
    age = tmp["birth"]
    gender = int(tmp["sex"])
    if gender==1:
        gender="男"
    else:
        gender="女"
    city = tmp["city"]
    return render(request, 'information.html', {"data":years,"gender":gender,"age":age,"city":city})
