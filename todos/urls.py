from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='todos-index'),
    path('update/<int:pk>/', views.update, name='todos-update'),
    path('delete/<int:pk>/', views.delete, name='todos-delete'),
]
