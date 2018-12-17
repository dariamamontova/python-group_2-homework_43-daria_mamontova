from django import forms
from webapp.models import Article

class ArticleSearchForm(forms.Form):
    article_name = forms.CharField(max_length=200, required=False, label='Название статьи')


class ArticleForm(forms.ModelForm):

    class Meta:
        model = Article
        fields = ['title', 'text', 'author']