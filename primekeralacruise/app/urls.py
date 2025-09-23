from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [

    #--------------Public-----------------
    path('',views.index),
    path('login',views.login),

    #--------------Admin-----------------
    path('admin_home',views.admin_home),
    path('admin_view_package',views.admin_view_package, name='admin_view_package'),
    path('admin_add_package',views.admin_add_package),
    path('admin_edit_package/<int:id>',views.admin_edit_package),
    path('admin_delete_package/<int:id>',views.admin_delete_package),
]
