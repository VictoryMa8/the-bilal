from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('articles/', views.articles, name='articles'),
    path('topics/', views.topics, name='topics'),
    path('contact/', views.contact, name='contact'),
    path('profile/', views.profile, name='profile'),
]