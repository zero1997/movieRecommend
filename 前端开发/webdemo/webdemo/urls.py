"""webdemo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib import admin
from django.urls import path
from web import views
from django.conf.urls import *
from django.views.static import serve

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index',views.rOrL,name='rOrL'),#最初界面选择了注册或登录
    path('log/',views.loginTest,name='login'),#输入用户名和和密码后登录
    path('register/',views.registerTest,name='register'),#输入用户名和和密码后注册
    path('changeInformation',views.changeInformation,name='changeInformation'),#从用户信息页面点击修改进入用户修改信息页面
    path('modify',views.modifyTest,name='modify'),#在用户信息修改页面，修改后进入推荐页面
    path('information', views.information,name='userInformation'),#在用户推荐页面点击查看用户信息进入用户信息页面
    path('hot', views.hot),#未登录的热门电影推荐页面
    #path('like', views.watch,name='like'),#在电影详细页面点击喜欢
    path('detail0', views.detail0,name='showDetail0'),#在电影推荐里面找到想看的点详细
    path('detail1', views.detail1,name='showDetail1'),
    path('detail2', views.detail2,name='showDetail2'),
    path('detail3', views.detail3,name='showDetail3'),
    path('detail4', views.detail4,name='showDetail4'),
    path('detail5', views.detail5,name='showDetail5'),
    path('detail6', views.detail6,name='showDetail6'),
    path('detail7', views.detail7,name='showDetail7'),
    path('detail8', views.detail8,name='showDetail8'),
    path('detail9', views.detail9,name='showDetail9'),
    path('detail10', views.detail10,name='showDetail10'),
    path('detail11', views.detail11,name='showDetail11'),
    path('detail12', views.detail12,name='showDetail12'),
    path('detail13', views.detail13,name='showDetail13'),
    path('detail14', views.detail14,name='showDetail14'),
    path('detail15', views.detail15,name='showDetail15'),
    path('detail16', views.detail16,name='showDetail16'),
    path('detail17', views.detail17,name='showDetail17'),
    path('dislike', views.loginTest,name='dislike'),#在电影详细页面点击不喜欢
    #url(r'^type_add/', views.type_add, name='type_add'),
    url(r'^image/pic/(?P<path>.*)', serve, {'document_root':'/home/hadoop/cm/posters'}),
]
