from django.conf.urls import url
from . import views
                    
urlpatterns = [
    url(r'^$', views.index),
    url(r'^dashboard$', views.dash),
    url(r'^mercury/(?P<id>\d+)$', views.message),
    url(r'^mercury/(?P<id>\d)+/profile$', views.profile),
    url(r'^register$', views.register),
    url(r'^login$', views.login),
    url(r'^create_message/(?P<id>\d+)$', views.create_message),
    url(r'^create_comment/(?P<id>\d+)$', views.create_comment),
    url(r'^delete_comment/(?P<id>\d+)$', views.delete_comment),
]