from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('post/<int:pk>/', views.detail_post, name='post'),
    path('create_post', views.create_post, name='create_post'),
]