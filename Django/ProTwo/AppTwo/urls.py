from django.urls import path 
from AppTwo import views

urlpatterns = [
        path('', views.index, name='index'),
        path('signup/', views.users, name='signup'),
        ]


app_name = 'AppTwo'
