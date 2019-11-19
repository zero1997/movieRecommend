from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from django.shortcuts import render
class Movie:
    def __init__(self,movieid,moviename,score,poster):
        self.movieid=movieid
        self.moviename=moviename
        self.score=score
        self.poster=poster

# Create your views here.
def index(request):
    #return render(request,'index.html')
    return render(request,'changeInformation.html')

def hot(request):
    #return render(request,'index.html')
    src='static/images/img1.jpg'
    return render(request,'hotRecommend.html',{"src":src})
def recommend(request):
    #return render(request,'index.html')
    src='static/images/img1.jpg'
    return render(request,'recommend.html',{"src":src})
def rOrL(request):
    #return render(request,'index.html')
    return render(request,'index.html')

def detail0(request):
    if request.method == 'POST':
        movieid5 = request.POST.get('movieid5')
        movieid3 = request.POST.get('movieid3')
    #print("movieid"+str(movieid5))
    #print("movieid" + str(movieid3))
    #return render(request,'index.html')
    site='https://www.baidu.com'
    print("xzs0")
    movieid=request.POST.get('movieid0')
    print(movieid)
    movieName='a'
    score='b'
    poster='c'
    director='d'
    scripwriter='e'
    mainActor='f'
    filmType='g'
    area='h'
    language='i'
    pubDate='j'
    duration='k'
    summary='l'
    comments='m'
    referenceUrl="http://www.baidu.com"
    print(referenceUrl)
    return render(request,'detail.html',{"movieid":movieid,"movieName":movieName,"score":score,"poster":poster,"director":director,"scripwriter":scripwriter,"mainActor":mainActor,"filmType":filmType,"area":area,"language":language,"pubDate":pubDate,"duration":duration,"summary":summary,"comments":comments,"referenceUrl":referenceUrl})
def detail1(request):
    if request.method == 'POST':
        movieid5 = request.POST.get('movieid5')
        movieid3 = request.POST.get('movieid3')
    #print("movieid"+str(movieid5))
    #print("movieid" + str(movieid3))
    #return render(request,'index.html')
    site='https://www.baidu.com'
    print("xzs1")
    movieid=request.POST.get('movieid1')
    print(movieid)

    movieName='a'
    score='b'
    poster='c'
    director='d'
    scripwriter='e'
    mainActor='f'
    filmType='g'
    area='h'
    language='i'
    pubDate='j'
    duration='k'
    summary='l'
    comments='m'
    referenceUrl='n'
    return render(request,'detail.html',{"movieid":movieid,"movieName":movieName,"score":score,"poster":poster,"director":director,"scripwriter":scripwriter,"mainActor":mainActor,"filmType":filmType,"area":area,"language":language,"pubDate":pubDate,"duration":duration,"summary":summary,"comments":comments,"referenceUrl":referenceUrl})
def detail2(request):
    if request.method == 'POST':
        movieid2 = request.POST.get('movieid2')
        movieid3 = request.POST.get('movieid3')
    #print("movieid"+str(movieid5))
    #print("movieid" + str(movieid3))
    #return render(request,'index.html')
    site='https://www.baidu.com'
    print("xzs2")
    movieid=request.POST.get('movieid2')
    print(movieid)

    movieName='a'
    score='b'
    poster='c'
    director='d'
    scripwriter='e'
    mainActor='f'
    filmType='g'
    area='h'
    language='i'
    pubDate='j'
    duration='k'
    summary='l'
    comments='m'
    referenceUrl='n'
    return render(request,'detail.html',{"movieid":movieid,"movieName":movieName,"score":score,"poster":poster,"director":director,"scripwriter":scripwriter,"mainActor":mainActor,"filmType":filmType,"area":area,"language":language,"pubDate":pubDate,"duration":duration,"summary":summary,"comments":comments,"referenceUrl":referenceUrl})
def detail3(request):
    if request.method == 'POST':
        movieid5 = request.POST.get('movieid5')
        movieid3 = request.POST.get('movieid3')
    #print("movieid"+str(movieid5))
    #print("movieid" + str(movieid3))
    #return render(request,'index.html')
    site='https://www.baidu.com'
    print("xzs3")
    movieid=request.POST.get('movieid3')
    print(movieid)

    movieName='a'
    score='b'
    poster='c'
    director='d'
    scripwriter='e'
    mainActor='f'
    filmType='g'
    area='h'
    language='i'
    pubDate='j'
    duration='k'
    summary='l'
    comments='m'
    referenceUrl='n'
    return render(request,'detail.html',{"movieid":movieid,"movieName":movieName,"score":score,"poster":poster,"director":director,"scripwriter":scripwriter,"mainActor":mainActor,"filmType":filmType,"area":area,"language":language,"pubDate":pubDate,"duration":duration,"summary":summary,"comments":comments,"referenceUrl":referenceUrl})
def detail4(request):
    if request.method == 'POST':
        movieid5 = request.POST.get('movieid5')
        movieid3 = request.POST.get('movieid3')
    #print("movieid"+str(movieid5))
    #print("movieid" + str(movieid3))
    #return render(request,'index.html').
    print("xzs4")
    site='https://www.baidu.com'
    movieid=request.POST.get('movieid4')
    print(movieid)

    movieName='a'
    score='b'
    poster='c'
    director='d'
    scripwriter='e'
    mainActor='f'
    filmType='g'
    area='h'
    language='i'
    pubDate='j'
    duration='k'
    summary='l'
    comments='m'
    referenceUrl='n'
    return render(request,'detail.html',{"movieid":movieid,"movieName":movieName,"score":score,"poster":poster,"director":director,"scripwriter":scripwriter,"mainActor":mainActor,"filmType":filmType,"area":area,"language":language,"pubDate":pubDate,"duration":duration,"summary":summary,"comments":comments,"referenceUrl":referenceUrl})
def detail5(request):
    if request.method == 'POST':
        movieid5 = request.POST.get('movieid5')
        movieid3 = request.POST.get('movieid3')
    #print("movieid"+str(movieid5))
    #print("movieid" + str(movieid3))
    #return render(request,'index.html')
    site='https://www.baidu.com'
    print("xzs5")
    movieid=request.POST.get('movieid5')
    print(movieid)

    movieName='a'
    score='b'
    poster='c'
    director='d'
    scripwriter='e'
    mainActor='f'
    filmType='g'
    area='h'
    language='i'
    pubDate='j'
    duration='k'
    summary='l'
    comments='m'
    referenceUrl='n'
    return render(request,'detail.html',{"movieid":movieid,"movieName":movieName,"score":score,"poster":poster,"director":director,"scripwriter":scripwriter,"mainActor":mainActor,"filmType":filmType,"area":area,"language":language,"pubDate":pubDate,"duration":duration,"summary":summary,"comments":comments,"referenceUrl":referenceUrl})
def detail6(request):
    if request.method == 'POST':
        movieid5 = request.POST.get('movieid5')
        movieid3 = request.POST.get('movieid3')
    #print("movieid"+str(movieid5))
    #print("movieid" + str(movieid3))
    #return render(request,'index.html')
    site='https://www.baidu.com'
    print("xzs6")
    movieid=request.POST.get('movieid6')
    print(movieid)

    movieName='a'
    score='b'
    poster='c'
    director='d'
    scripwriter='e'
    mainActor='f'
    filmType='g'
    area='h'
    language='i'
    pubDate='j'
    duration='k'
    summary='l'
    comments='m'
    referenceUrl='n'
    return render(request,'detail.html',{"movieid":movieid,"movieName":movieName,"score":score,"poster":poster,"director":director,"scripwriter":scripwriter,"mainActor":mainActor,"filmType":filmType,"area":area,"language":language,"pubDate":pubDate,"duration":duration,"summary":summary,"comments":comments,"referenceUrl":referenceUrl})
def detail7(request):
    if request.method == 'POST':
        movieid5 = request.POST.get('movieid5')
        movieid3 = request.POST.get('movieid3')
    #print("movieid"+str(movieid5))
    #print("movieid" + str(movieid3))
    #return render(request,'index.html')
    site='https://www.baidu.com'
    print("xzs7")
    movieid=request.POST.get('movieid7')
    print(movieid)

    movieName='a'
    score='b'
    poster='c'
    director='d'
    scripwriter='e'
    mainActor='f'
    filmType='g'
    area='h'
    language='i'
    pubDate='j'
    duration='k'
    summary='l'
    comments='m'
    referenceUrl='n'
    return render(request,'detail.html',{"movieid":movieid,"movieName":movieName,"score":score,"poster":poster,"director":director,"scripwriter":scripwriter,"mainActor":mainActor,"filmType":filmType,"area":area,"language":language,"pubDate":pubDate,"duration":duration,"summary":summary,"comments":comments,"referenceUrl":referenceUrl})
def detail8(request):
    if request.method == 'POST':
        movieid5 = request.POST.get('movieid5')
        movieid3 = request.POST.get('movieid3')
    #print("movieid"+str(movieid5))
    #print("movieid" + str(movieid3))
    #return render(request,'index.html')
    site='https://www.baidu.com'
    print("xzs8")
    movieid=request.POST.get('movieid8')
    print(movieid)

    movieName='a'
    score='b'
    poster='c'
    director='d'
    scripwriter='e'
    mainActor='f'
    filmType='g'
    area='h'
    language='i'
    pubDate='j'
    duration='k'
    summary='l'
    comments='m'
    referenceUrl='n'
    return render(request,'detail.html',{"movieid":movieid,"movieName":movieName,"score":score,"poster":poster,"director":director,"scripwriter":scripwriter,"mainActor":mainActor,"filmType":filmType,"area":area,"language":language,"pubDate":pubDate,"duration":duration,"summary":summary,"comments":comments,"referenceUrl":referenceUrl})
def detail9(request):
    if request.method == 'POST':
        movieid5 = request.POST.get('movieid5')
        movieid3 = request.POST.get('movieid3')
    #print("movieid"+str(movieid5))
    #print("movieid" + str(movieid3))
    #return render(request,'index.html')
    print("xzs9")
    site='https://www.baidu.com'
    movieid=request.POST.get('movieid9')
    print(movieid)

    movieName='a'
    score='b'
    poster='c'
    director='d'
    scripwriter='e'
    mainActor='f'
    filmType='g'
    area='h'
    language='i'
    pubDate='j'
    duration='k'
    summary='l'
    comments='m'
    referenceUrl='n'
    return render(request,'detail.html',{"movieid":movieid,"movieName":movieName,"score":score,"poster":poster,"director":director,"scripwriter":scripwriter,"mainActor":mainActor,"filmType":filmType,"area":area,"language":language,"pubDate":pubDate,"duration":duration,"summary":summary,"comments":comments,"referenceUrl":referenceUrl})
def detail10(request):
    if request.method == 'POST':
        movieid5 = request.POST.get('movieid5')
        movieid3 = request.POST.get('movieid3')
    #print("movieid"+str(movieid5))
    #print("movieid" + str(movieid3))
    #return render(request,'index.html')
    site='https://www.baidu.com'
    print("xzs10")
    movieid=request.POST.get('movieid10')
    print(movieid)

    movieName='a'
    score='b'
    poster='c'
    director='d'
    scripwriter='e'
    mainActor='f'
    filmType='g'
    area='h'
    language='i'
    pubDate='j'
    duration='k'
    summary='l'
    comments='m'
    referenceUrl="http://www.baidu.com"
    print(referenceUrl)
    return render(request,'detail.html',{"movieid":movieid,"movieName":movieName,"score":score,"poster":poster,"director":director,"scripwriter":scripwriter,"mainActor":mainActor,"filmType":filmType,"area":area,"language":language,"pubDate":pubDate,"duration":duration,"summary":summary,"comments":comments,"referenceUrl":referenceUrl})
def detail11(request):
    if request.method == 'POST':
        movieid5 = request.POST.get('movieid5')
        movieid3 = request.POST.get('movieid3')
    #print("movieid"+str(movieid5))
    #print("movieid" + str(movieid3))
    #return render(request,'index.html')
    site='https://www.baidu.com'
    print("xzs11")
    movieid=request.POST.get('movieid11')
    print(movieid)

    movieName='a'
    score='b'
    poster='c'
    director='d'
    scripwriter='e'
    mainActor='f'
    filmType='g'
    area='h'
    language='i'
    pubDate='j'
    duration='k'
    summary='l'
    comments='m'
    referenceUrl='n'
    return render(request,'detail.html',{"movieid":movieid,"movieName":movieName,"score":score,"poster":poster,"director":director,"scripwriter":scripwriter,"mainActor":mainActor,"filmType":filmType,"area":area,"language":language,"pubDate":pubDate,"duration":duration,"summary":summary,"comments":comments,"referenceUrl":referenceUrl})
def detail12(request):
    if request.method == 'POST':
        movieid5 = request.POST.get('movieid5')
        movieid3 = request.POST.get('movieid3')
    #print("movieid"+str(movieid5))
    #print("movieid" + str(movieid3))
    #return render(request,'index.html')
    site='https://www.baidu.com'
    print("xzs12")
    movieid=request.POST.get('movieid12')
    print(movieid)

    movieName='a'
    score='b'
    poster='c'
    director='d'
    scripwriter='e'
    mainActor='f'
    filmType='g'
    area='h'
    language='i'
    pubDate='j'
    duration='k'
    summary='l'
    comments='m'
    referenceUrl='n'
    return render(request,'detail.html',{"movieid":movieid,"movieName":movieName,"score":score,"poster":poster,"director":director,"scripwriter":scripwriter,"mainActor":mainActor,"filmType":filmType,"area":area,"language":language,"pubDate":pubDate,"duration":duration,"summary":summary,"comments":comments,"referenceUrl":referenceUrl})
def detail13(request):
    if request.method == 'POST':
        movieid5 = request.POST.get('movieid5')
        movieid3 = request.POST.get('movieid3')
    #print("movieid"+str(movieid5))
    #print("movieid" + str(movieid3))
    #return render(request,'index.html')
    site='https://www.baidu.com'
    print("xzs13")
    movieid=request.POST.get('movieid13')
    print(movieid)

    movieName='a'
    score='b'
    poster='c'
    director='d'
    scripwriter='e'
    mainActor='f'
    filmType='g'
    area='h'
    language='i'
    pubDate='j'
    duration='k'
    summary='l'
    comments='m'
    referenceUrl='n'
    return render(request,'detail.html',{"movieid":movieid,"movieName":movieName,"score":score,"poster":poster,"director":director,"scripwriter":scripwriter,"mainActor":mainActor,"filmType":filmType,"area":area,"language":language,"pubDate":pubDate,"duration":duration,"summary":summary,"comments":comments,"referenceUrl":referenceUrl})
def detail14(request):
    if request.method == 'POST':
        movieid5 = request.POST.get('movieid5')
        movieid3 = request.POST.get('movieid3')
    #print("movieid"+str(movieid5))
    #print("movieid" + str(movieid3))
    #return render(request,'index.html')
    site='https://www.baidu.com'
    print("xzs14")
    movieid=request.POST.get('movieid14')
    print(movieid)

    movieName='a'
    score='b'
    poster='c'
    director='d'
    scripwriter='e'
    mainActor='f'
    filmType='g'
    area='h'
    language='i'
    pubDate='j'
    duration='k'
    summary='l'
    comments='m'
    referenceUrl='n'
    return render(request,'detail.html',{"movieid":movieid,"movieName":movieName,"score":score,"poster":poster,"director":director,"scripwriter":scripwriter,"mainActor":mainActor,"filmType":filmType,"area":area,"language":language,"pubDate":pubDate,"duration":duration,"summary":summary,"comments":comments,"referenceUrl":referenceUrl})
def detail15(request):
    if request.method == 'POST':
        movieid5 = request.POST.get('movieid5')
        movieid3 = request.POST.get('movieid3')
    #print("movieid"+str(movieid5))
    #print("movieid" + str(movieid3))
    #return render(request,'index.html')
    site='https://www.baidu.com'
    print("xzs15")
    movieid=request.POST.get('movieid15')
    print(movieid)

    movieName='a'
    score='b'
    poster='c'
    director='d'
    scripwriter='e'
    mainActor='f'
    filmType='g'
    area='h'
    language='i'
    pubDate='j'
    duration='k'
    summary='l'
    comments='m'
    referenceUrl='n'
    return render(request,'detail.html',{"movieid":movieid,"movieName":movieName,"score":score,"poster":poster,"director":director,"scripwriter":scripwriter,"mainActor":mainActor,"filmType":filmType,"area":area,"language":language,"pubDate":pubDate,"duration":duration,"summary":summary,"comments":comments,"referenceUrl":referenceUrl})
def detail16(request):
    if request.method == 'POST':
        movieid5 = request.POST.get('movieid5')
        movieid3 = request.POST.get('movieid3')
    #print("movieid"+str(movieid5))
    #print("movieid" + str(movieid3))
    #return render(request,'index.html')
    site='https://www.baidu.com'
    print("xzs16")
    movieid=request.POST.get('movieid16')
    print(movieid)

    movieName='a'
    score='b'
    poster='c'
    director='d'
    scripwriter='e'
    mainActor='f'
    filmType='g'
    area='h'
    language='i'
    pubDate='j'
    duration='k'
    summary='l'
    comments='m'
    referenceUrl='n'
    return render(request,'detail.html',{"movieid":movieid,"movieName":movieName,"score":score,"poster":poster,"director":director,"scripwriter":scripwriter,"mainActor":mainActor,"filmType":filmType,"area":area,"language":language,"pubDate":pubDate,"duration":duration,"summary":summary,"comments":comments,"referenceUrl":referenceUrl})
def detail17(request):
    if request.method == 'POST':
        movieid5 = request.POST.get('movieid5')
        movieid3 = request.POST.get('movieid3')
    #print("movieid"+str(movieid5))
    #print("movieid" + str(movieid3))
    #return render(request,'index.html')
    site='https://www.baidu.com'
    print("xzs17")
    movieid=request.POST.get('movieid17')
    print(movieid)
    movieName='a'
    score='b'
    poster='c'
    director='d'
    scripwriter='e'
    mainActor='f'
    filmType='g'
    area='h'
    language='i'
    pubDate='j'
    duration='k'
    summary='l'
    comments='m'
    referenceUrl='n'
    return render(request,'detail.html',{"movieid":movieid,"movieName":movieName,"score":score,"poster":poster,"director":director,"scripwriter":scripwriter,"mainActor":mainActor,"filmType":filmType,"area":area,"language":language,"pubDate":pubDate,"duration":duration,"summary":summary,"comments":comments,"referenceUrl":referenceUrl})

#def watch(request):
#   #return render(request,'index.html')
#   return render(request,'www.baidu.com')
def loginTest(request):
    if request.method == 'POST':
        name = request.POST.get('username1')
        pwd = request.POST.get('password1')
    print(name, pwd)
    movie=[]
    for i in range(0,18):
        movie.append(Movie(i,i+10,i+20,i+30))
    movie[0].poster='/static/images/img1.jpg'
    movie[1].poster = '/static/images/img2.jpg'
    movie[2].poster = '/static/images/img3.jpg'
    movie[3].poster = '/static/images/img4.jpg'
    movie[4].poster = '/static/images/img1.jpg'
    movie[5].poster = '/static/images/img2.jpg'
    movie[6].movieid=123321
    movie1=movie[0:3]
    movie2 = movie[3:6]
    movie3 = movie[6:9]
    movie4 = movie[9:12]
    movie5 = movie[12:15]
    movie6 = movie[15:]
    print(str(movie1[0].movieid)+"idddd")
    movie0=movie[0]
    movie1 = movie[1]
    movie2 = movie[2]
    movie3 = movie[3]
    movie4 = movie[4]
    movie5 = movie[5]
    #for i in range(0,10):
        #print(movie[i].moviename,movie[i].movieid)
    return render(request, 'recommend.html',{"movie0":movie0,"movie1":movie1,"movie2":movie2,"movie3":movie3,"movie4":movie4,"movie5":movie5,"movie6":movie6})

def changeInformation(request):
    #return render(request,'index.html')
    return render(request,'changeInformation.html')
def modifyTest(request):
    if request.method == 'POST':
        gender = request.POST.get('gender')
        year= request.POST.get('birthdayYear')
        month=request.POST.get('birthdayMonth')
        day=request.POST.get('birthdayDay')
        city = request.POST.get('city')
    print(gender,year,month,day,city)
    a = [{"movieid": 1, "moviename": 2, "score": 3, "poster": 4},
         {"movieid": 5, "moviename": 6, "score": 7, "poster": 8}]
    return render(request, 'recommend.html',{"a":a})

def registerTest(request):
    if request.method == 'POST':
        name = request.POST.get('username')
        pwd = request.POST.get('password')
        pwd2=request.POST.get('password2')
    print(name, pwd,pwd2)
    return render(request, 'login.html')













def information(request):
    years = range(1997, 2018)
    gender='male'
    age=11
    city='beijing'
    return render(request, 'information.html', {"data":years,"gender":gender,"age":age,"city":city})






def login(request):
    return render(request,'login.html')
def reg(request):
    if request.method == 'POST':
        name=request.POST.get('name')
        pwd=request.POST.get('pwd')
    print(name,pwd)
    return render(request,'login.html')
