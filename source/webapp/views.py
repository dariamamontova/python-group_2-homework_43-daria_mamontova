from django.views.generic import ListView, DetailView
from webapp.models import User, Article, Comment, Rating

class ArticleListView(ListView):
    model = Article
    template_name = 'article_list.html'

class ArticleDetailView(DetailView):
    model = Article
    template_name = 'article_detail.html'

class UserListView(ListView):
    model = User
    template_name = 'user_list.html'

class UserDetailView(DetailView):
    model = User
    template_name = 'user_detail.html'

class FavoritesDetailView(DetailView):
    model = User
    template_name = 'favorites_detail.html'
