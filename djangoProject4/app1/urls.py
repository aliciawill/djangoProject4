from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include

# http://127.0.0.1:9999/app1
import app1.views

urlpatterns = [
    path('', app1.views.index, name='index'),
]

