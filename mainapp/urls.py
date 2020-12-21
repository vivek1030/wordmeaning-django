from django.contrib import admin
from django.urls import path
from mainapp import views
urlpatterns = [
    path('', views.index, name='home'),
    path('search/', views.search, name='search'),
]
