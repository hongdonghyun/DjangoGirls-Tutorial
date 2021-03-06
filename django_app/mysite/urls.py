"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from blog import views


# o /post/1
# o /post/35
# o /post/234
# x /post/234/asdf
# /post/로 시작하고 중간에 숫자 1개이상으 가지고 /로 끝나는 정규표현식


urlpatterns = [
        url(r'^admin/',admin.site.urls),
        url(r'^$',views.post_list,name ='post_list'),
        url(r'^post/(?P<pk>\d+)/$',views.post_detail,name='post_detail'), #pk라는 key값을 전달
        url(r'^post/create/$',views.post_create,name = 'post_create'),
        url(r'^post/(?P<pk>\d+)/modify/$',views.post_modify,name='post_modify')

 ]
