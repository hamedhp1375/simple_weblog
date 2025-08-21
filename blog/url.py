from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),          # آدرس اصلی: localhost:8000/
    path('about/', views.about, name='about'),  # آدرس: localhost:8000/about/
]
