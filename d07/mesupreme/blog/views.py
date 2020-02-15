from django.shortcuts import render
from django.utils import timezone
from django.shortcuts import get_object_or_404
from django.views.generic.detail import DetailView
from django.views.generic.base import TemplateView, RedirectView

from blog.models import Article, UserFavouriteArticle
from django.contrib.auth.models import User
from django.views.generic.edit import FormView
from blog.forms import LoginForm
from django.contrib.auth.forms import AuthenticationForm


class HomePageView(RedirectView):
    permanent = False
    query_string = True
    pattern_name = 'article-detail'

    def get_redirect_url(self, *args, **kwargs):
        article = get_object_or_404(Article, pk=kwargs['pk'])
        article.update_counter()
        return super().get_redirect_url(*args, **kwargs)


class ArticleView(TemplateView):
    template_name = 'articles.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_articles'] = Article.objects.all()
        return context


class LoginView(FormView):
    template_name = 'login.html'
    form_class = AuthenticationForm
    success_url = ''


