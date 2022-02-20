"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include

from hello import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path('food',views.food, name='food'),
    path('traffic',views.traffic, name='traffic'),
    path('covid',views.covid, name='covid'),

    path('getdata_news',views.getdata_news, name='getdata_news'),
    path('getdata_covid', views.getdata_covid, name='getdata_covid'),
    path('getdata_vaccinated', views.getdata_vaccinated, name='getdata_vaccinated'),

    path('location', views.location, name='location'),
    path('lunch1', views.lunch1, name='lunch1'),
    path('dinner1', views.dinner1, name='dinner1'),

    path('bicycle', views.bicycle, name='bicycle'),
    path('cafe', views.cafe, name='cafe'),
    path('cinema', views.cinema, name='cinema'),
    path('shopping', views.shopping, name='shopping'),
    path('stay', views.stay, name='stay'),
    path('subway', views.subway, name='subway'),
    path('tour', views.tour, name='tour'),
    path('hotplace_location', views.hotplace_location, name='hotplace_location'),
    path('ranking', views.ranking, name='ranking'),
    path('batch_start', views.batch_start, name='batch_start'),
    path('batch_stop', views.batch_stop, name='batch_stop'),
]

