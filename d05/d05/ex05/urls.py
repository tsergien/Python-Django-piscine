from django.urls import path

from . import views

urlpatterns = [
    path('ex05/init', views.init, name='init'),
    path('ex05/populate', views.populate, name='populate'),
    path('ex05/display', views.display, name='display'),
    path('ex05/remove', views.remove, name='remove'),
]
