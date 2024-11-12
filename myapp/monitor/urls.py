# monitor/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.htop_view, name='htop'),  # Route to /htop endpoint
]
