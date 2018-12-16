from django.db import models

class User(models.Model):
    name = models.CharField(max_length=50, verbose_name='Имя')
    last_name = models.CharField(max_length=50, verbose_name="Фамилия")
    email = models.EmailField(max_length=50, verbose_name="Почта")
    favorites = models.ManyToManyField('Article', blank=True, related_name='favored_by', verbose_name='Избранное')

    def __str__(self):
        return "%s %s" % (self.name, self.last_name)


class Article(models.Model):
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    text = models.TextField(max_length=2000, verbose_name='Текст')
    author = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='Автор')

    def __str__(self):
        return self.title

class Comment(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    text = models.TextField(max_length=5000, verbose_name='Текст')
    author = models.ForeignKey(User, on_delete=models.PROTECT, related_name='comment_author', verbose_name='Автор')
    article = models.ForeignKey(Article, on_delete=models.PROTECT, related_name='comment_article', verbose_name='Статья')
    answer = models.ForeignKey('self', on_delete=models.PROTECT, blank=True, null=True, related_name='comment_answer', verbose_name='Ответ')


    def __str__(self):
        return self.title
