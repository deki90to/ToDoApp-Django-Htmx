from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('delete/<pk>/', views.delete, name='delete'),
    path('create/', views.create, name='create'),
    path('contact/', views.contact, name='contact'),
]