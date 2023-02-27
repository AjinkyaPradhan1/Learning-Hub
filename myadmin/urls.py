from django.contrib import admin
from django.urls import path,include

from .import views

urlpatterns = [
    path('',views.adminhome),
    path('manageusers/',views.manageusers),
    path('manageuserstatus/',views.manageuserstatus),
    path('addclass/',views.addclass),
    path('addsubject/',views.addsubject),
    path('addstate/',views.addstate),
    path('addcity/',views.addcity),
    

]