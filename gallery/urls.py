from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.gallery, name='gallery'),
    path('tattoo/<str:pk>', views.viewTattoo, name='tattoo'),
    path('add-tattoo/', views.addTattoo, name='addTattoo')
]
