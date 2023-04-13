from django.contrib import admin
from django.urls import path
from members import views


urlpatterns = [
    path('register',views.register,name='register'),
    path('login',views.signin,name='login'),
    path('logout',views.logout,name='logout'),
]
