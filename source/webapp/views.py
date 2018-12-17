from django.views.generic import ListView, DetailView, FormView, CreateView, UpdateView
from webapp.models import User, Article, Comment, Rating
from webapp.forms import ArticleSearchForm, ArticleForm, CommentForm
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


class ArticleCreateView(CreateView):
    model = Article
    template_name = 'article_create.html'
    form_class = ArticleForm
    success_url = reverse_lazy('article_list')

class ArticleUpdateView(UpdateView):
    model = Article
    template_name = 'article_update.html'
    form_class = ArticleForm
    success_url = reverse_lazy('article_list')

class CommentCreateView(CreateView):
    model = Comment
    template_name = 'comment_create.html'
    form_class = CommentForm
    success_url = reverse_lazy('article_list')