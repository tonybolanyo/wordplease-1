"""wordplease URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from users.views import LoginView, logout, CreateUser
from blog.views import home,CreatePost,post_detail,all_blogs

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blogs/<int:pk>',post_detail,name='post_detail'),
    path('blogs',all_blogs,name='blogs'),

    path('login',LoginView.as_view(),name='login_page'),
    path('logout',logout,name="logout_page"),
    path('new-post',CreatePost.as_view(),name='post_form'),
    path('signup',CreateUser.as_view(),name='signup_page'),
    path('',home,name="home_page"),
]
