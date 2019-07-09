from django.urls import path 
from AppTwo import views

urlpatterns = [
  #      url(r'^$', views.index, name='help'),
        path('', views.index, name='index'),
        path('users/', views.users, name='users'),
        ]

