from django.urls import path

from . import views

urlpatterns = [
    path('ex03/populate', views.populate, name='populate'),
    path('ex03/display', views.display, name='display'),
]
