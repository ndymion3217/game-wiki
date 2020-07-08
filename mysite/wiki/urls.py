from django.urls import re_path, path
#from django.conf.urls import patterns, url
from . import views

urlpatterns = [
    re_path('(?P<page_name>[^/]+)/$', views.pageView, name='View'),
    re_path('(?P<page_name>[^/]+)/edit/$', views.editView, name='Edit'),

]
'''
urlpatterns = patterns('',
                       url('(?P<page_name>[^/]+)/$', views.pageView),
)
'''