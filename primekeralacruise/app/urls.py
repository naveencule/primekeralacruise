from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [

    #--------------Public-----------------
    path('',views.index),
    path('login',views.login),

    #--------------Admin-----------------
    path('admin_home',views.admin_home),
]
