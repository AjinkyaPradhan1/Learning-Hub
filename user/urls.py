from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url


from . import views

urlpatterns = [
    path('',views.userhome),
    path('ncertsolution/',views.ncertsolution),
    path('paper/',views.paper),
    path('practiceque/',views.practiceque),
    path('videos/',views.videos),
    path('editprofileuser/',views.editprofileuser),
    path('updateDataUser/',views.updateDataUser),
    path('changepassworduser/',views.changepassworduser),
    path('books/',views.books),
    path('subcatviewbooks/',views.subcatviewbooks),
    path('addbooks/',views.addbooks),
    path('showSubject/', views.showSubject),
    path('viewbooksuser/', views.viewbooksuser),
    path('payment/',views.payment),
    path('cancel/',views.cancel),
    path('viewbuybooks/',views.viewbuybooks),
    
    
    
    
    
    
    
    
]