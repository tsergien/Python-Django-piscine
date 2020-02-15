from django.urls import path

from . import views

urlpatterns = [
    path('ex04/init', views.init, name='init'),
    path('ex04/populate', views.populate, name='populate'),
    path('ex04/display', views.display, name='display'),
    path('ex04/remove', views.remove, name='remove'),
]
