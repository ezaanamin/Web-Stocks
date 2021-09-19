from django.contrib import admin
from django.urls import path,include
from .import views
urlpatterns = [
    path('homepage/',views.home,name='home'),
    path("company/",views.homepage,name="homepage"),
    path('serach/',views.mainpage,name='mainpage'),
    

]
