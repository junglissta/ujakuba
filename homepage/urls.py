from django.urls import path
from . import views
from django.contrib.auth import views as view

urlpatterns = [
    path('', views.HomeView.as_view(),name='home'),
    path('about/', views.about, name='about'),
    path('menu/', views.menu, name='menu'),
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('login/', view.LoginView.as_view(), name='login'),
]

