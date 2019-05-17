from django.urls import path, include
from django.conf import settings
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('user/<str:user>/', views.userDetails, name='userDetails'),
    path('add', views.add, name='add')
]
