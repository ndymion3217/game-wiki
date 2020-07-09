from django.urls import re_path, path
#from django.conf.urls import patterns, url
from . import views

urlpatterns = [
    re_path('(?P<page_name>[^/]+)/save/$', views.saveView, name='Save'),
    re_path('(?P<page_name>[^/]+)/edit/$', views.editView, name='Edit'),
    re_path('(?P<page_name>[^/]+)/$', views.pageView, name='View'),
]
'''
urlpatterns = [
    path('<str:page_name>/save/', views.saveView, name='Save'),
    path('<str:page_name>/edit/', views.editView, name='Edit'),
    path('<str:page_name>/', views.pageView, name='View'),
]'''