from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # path('ex00/login', views.login, name='login'),
    # path('ex00/register', views.register, name='register'),
]
