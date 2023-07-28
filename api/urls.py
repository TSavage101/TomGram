from django.urls import path

from . import views

urlpatterns = [
    path('getFollowers/<str:profile>/', views.getFollowers, name='getFollowers'),
    
]