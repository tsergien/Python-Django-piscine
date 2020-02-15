from django.urls import path
from django.views.generic.base import RedirectView
from blog.views import ArticleView, HomePageView, LoginView


urlpatterns = [
    path('articles', ArticleView.as_view(), name='articles'),
    path('login', LoginView.as_view(), name='login'),
    path('', RedirectView.as_view(url='articles'), name='home'),
]
