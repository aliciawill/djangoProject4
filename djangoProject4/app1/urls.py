from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include

# http://127.0.0.1:9999/app1
import app1.views

urlpatterns = [
    path('', app1.views.index, name='index'),
    path('/list', app1.views.list, name='list'),
    path('/insert', app1.views.insert, name='insert'),
    path('/insert2', app1.views.insert2, name='insert2'),
    path('/one/<id>', app1.views.one, name='one'),
    path('/delete/<id>', app1.views.delete, name='delete'),
    path('/update/<id>', app1.views.update, name='update'),
    path('/update2', app1.views.update2, name='update2'),
]

