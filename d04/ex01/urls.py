from django.urls import path

from . import views

urlpatterns = [
    path('ex01/django', views.django, name='django'),
    path('ex01/affichage', views.affichage, name='affichage'),
    path('ex01/templates', views.templates, name='templates')
]

