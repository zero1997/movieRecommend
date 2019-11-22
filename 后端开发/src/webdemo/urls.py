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
    path('',views.loginTest,name='login'),#输入用户名和和密码后登录
    path('register/',views.registerTest,name='register'),#输入用户名和和密码后注册
    path('changeInformation',views.changeInformation,name='changeInformation'),#从用户信息页面点击修改进入用户修改信息页面
    path('modify',views.modifyTest,name='modify'),#在用户信息修改页面，修改后进入推荐页面
    path('information', views.information,name='userInformation'),#在用户推荐页面点击查看用户信息进入用户信息页面
    path('hot', views.hot),#未登录的热门电影推荐页面
    path('like', views.watch,name='like'),#在电影详细页面点击喜欢
    path('detail', views.detail,name='showDetail'),#在电影推荐里面找到想看的点详细
    path('dislike', views.dislike,name='dislike'),#在电影详细页面点击不喜欢
    #url(r'^type_add/', views.type_add, name='type_add'),
    url(r'^image/pic/(?P<path>.*)', serve, {'document_root':'/home/hadoop/cm/posters'}),
]
