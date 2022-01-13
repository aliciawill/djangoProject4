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
    path('/insert3', app1.views.insert3, name='insert3'),
    path('/one/<id>', app1.views.one, name='one'),
    path('/delete/<id>', app1.views.delete, name='delete'),
    path('/delete2', app1.views.delete2, name='delete2'),
    path('/update/<id>', app1.views.update, name='update'),
    path('/update2', app1.views.update2, name='update2'),
    path('/many_insert', app1.views.many_insert, name='many_insert'),
]

