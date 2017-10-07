from django.conf.urls import url
from hab_app import views
from django.contrib import admin
app_name = 'hab_app'

urlpatterns = [
    url(r'^index/$', views.index,name='index'),
    url(r'^login/$', views.user_login,name='user_login'),
    url(r'^vacate/$', views.vacate,name='vacate'),
    url(r'^allot/$', views.allot,name='allot'),
    url(r'^home/$', views.home,name='home'),
    url(r'^showDetails/$', views.showDetails,name='showDetails'),
    url(r'^chrAllot/$', views.chrAllot,name='chrAllot'),
]
