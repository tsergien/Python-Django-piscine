from django.urls import path

from . import views

urlpatterns = [
    path('ex02/form', views.myform, name='myform'),
    path('ex02/index', views.index, name='index'),
]
