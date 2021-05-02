"""turbo URL Configuration

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
from django.urls import path
from django.contrib import admin
from django.urls import path, include
from turbo_app import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('home', views.home),
    path('table', views.table),
    path('show_data',views.show_data),
    path('add_info',views.add_info),
    path('save_person',views.save_person),
    path('login',views.login),
    path('register',views.register),
    path('reg_post',views.reg_post),
    path('add_login',views.add_login,name='add_login'),
    path('forgot_pass',views.forgot_pass,name='forgot_pass'),
    path('forgot_p',views.forgot_p,name='forgot_p'),
    path('profile',views.profile),
    path('add_auction',views.add_auction),
    path('auct_form',views.auct_form),
    #app urls
    #path('turbo_app',include('turbo_app.urls'))
]
