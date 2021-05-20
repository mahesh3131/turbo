"""sample URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import include, path
from sample_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home',views.home),
    path('register',views.register,name='register'),
    path('reg_post',views.reg_post),
    path('login_user',views.login_user,name='login_user'),
    path('add_login',views.add_login),
    path('profile',views.profile,name='profile'),
    path('logout_user',views.logout_user),
    path('table',views.table),
    path('add_auction',views.add_auction),
    path('auct_form',views.auct_form),
    path('bid_form',views.bid_form),
    path('add_status_agreed',views.add_status_agreed),
    path('add_status_disagreed',views.add_status_disagreed),
    path('add_status_received',views.add_status_received),
    path('add_status_closed',views.add_status_closed),
    path('post',views.post),
    path('edit_profile',views.edit_profile),
    path('achived',views.achived),
    path('app/', include('sample_app.urls')),
]
