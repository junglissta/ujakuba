from django.urls import path
from . import views
from django.contrib.auth import views as view

urlpatterns = [
    path('', views.HomeView.as_view(),name='home'),
    path('about/', views.about, name='about'),
    path('menu/', views.menu, name='menu'),
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('login/', view.LoginView.as_view(), name='login'),
    path('posts/', views.PostView.as_view(), name='posts'),
    path("logout/", views.signout, name="logout"),
    # path('create_post/', views.CreatePostView.as_view(), name='create_post'),
]

