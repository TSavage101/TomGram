from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('auth/signup/', views.signup, name='signup'),
    path('auth/login/', views.login, name='login'),
    path('auth/logout/', views.logout, name='logout'),
    path('tg/<str:username>/', views.profile, name='profile'),
    path('accounts/settings/', views.settings, name='settings'),
]