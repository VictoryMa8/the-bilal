from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
from .forms import StyledLoginForm, StyledSignUpForm

urlpatterns = [
    path('', views.index, name='index'),
    path('articles/', views.articles, name='articles'),
    path('topics/', views.topics, name='topics'),
    path('contact/', views.contact, name='contact'),
    path('profile/', views.profile, name='profile'),
    path("accounts/", include("django.contrib.auth.urls")),
    path('login/', auth_views.LoginView.as_view(authentication_form=StyledLoginForm), name='login'),
    path("sign_up/", views.sign_up, name="sign_up"),
    path('forgot_password/', views.forgot_password, name='forgot_password')
]