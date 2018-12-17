from django import forms
from webapp.models import Article, Comment

class ArticleSearchForm(forms.Form):
    article_name = forms.CharField(max_length=200, required=False, label='Название статьи')


class ArticleForm(forms.ModelForm):

    class Meta:
        model = Article
        fields = ['title', 'text', 'author']

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['title', 'text', 'author', 'article', 'answer']

class CommentUpdateForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['title', 'text', 'answer']