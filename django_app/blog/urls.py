from django.conf.urls import url

from . import admin
from . import views
#####???????????????????##############
urlpatterns = [
        url(r'^admin/',admin.site.urls),
        url(r'^$',views.post_list,name ='post_list'),
        url(r'^post/\d+/$',views.post_detail,name='post_datail'),

 ]

