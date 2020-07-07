from django.urls import path
#from django.conf.urls import patterns, url
from . import views

urlpatterns = [
    path('<str:page_name>/', views.pageView, name='pageView'),
    
]
'''
urlpatterns = patterns('',
                       url('(?P<page_name>[^/]+)/$', views.pageView),
)
'''