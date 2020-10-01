from django.urls import path
from .views import *
urlpatterns = [
    path('',index,name='index'),
    path('template',template,name='template'),
    path('illustration',illustration,name='illustration'),
]
