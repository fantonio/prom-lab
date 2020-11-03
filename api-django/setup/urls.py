from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from clientes.list import ClientesList
from django.conf.urls import url
from django.conf.urls import include

urlpatterns = [
    url('', include('django_prometheus.urls')),
    path('clientes', ClientesList.as_view())
]
