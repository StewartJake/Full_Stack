"""adv_cbv URL Configuration

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
from django.urls import path, re_path
from basic_app import views

app_name='basic_app'


urlpatterns = [
    re_path(r'^$', views.SchoolListView.as_view(), name='list'),
    re_path(r'^(?P<pk>\d+)/$',
            views.SchoolDetailView.as_view(),
            name='detail'),
    path('create/', views.SchoolCreateView.as_view(), name='create'),
    re_path(r'^update/(?P<pk>\d+)/$',
            views.SchoolUpdateView.as_view(),
            name='update'),
    re_path(r'^delete/(?P<pk>\d+)/$',
            views.SchoolDeleteView.as_view(),
            name='delete'),
]
