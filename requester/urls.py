from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.homeView, name='requester-home'),#url to home page
    path('home/', views.homeView, name='requester-home'),#url to home page
]