from django.contrib import admin
from django.urls import path
from . import views

app_name = "blog"
urlpatterns = [
    path('',views.home,name = "home"),
    path('<slug:post>/',views.post_single, name = "post_single")
]

#the slug:post path takes the url with the slug and pass it over to views.post_single. name it as given. 