from django.urls import include, path
from sample_app import views

urlpatterns = [
    path('test/', views.test),
]