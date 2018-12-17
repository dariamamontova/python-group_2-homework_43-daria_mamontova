from django.views.generic import ListView, DetailView, FormView
from webapp.models import User, Article, Comment, Rating
from webapp.forms import ArticleSearchForm
from django.urls import reverse_lazy

class ArticleListView(ListView, FormView):
    model = Article
    template_name = 'article_list.html'
    form_class = ArticleSearchForm

    def get_queryset(self):
        article_name = self.request.GET.get('article_name')
        if article_name:
            return Article.objects.filter(title__icontains=article_name)
        else:
            return self.model.objects.all()

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


