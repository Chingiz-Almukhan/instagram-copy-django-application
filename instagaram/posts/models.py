from django.contrib.auth import get_user_model
from django.db import models


class Post(models.Model):
    description = models.CharField(verbose_name='Описание', null=False, blank=False, max_length=200)
    image = models.ImageField(verbose_name='Фото', null=False, blank=False, upload_to='posts')
    author = models.ForeignKey(verbose_name='Автор', to=get_user_model(), related_name='posts', null=False, blank=False,
                               on_delete=models.CASCADE)
    created_at = models.DateField(verbose_name='Дата публикации', auto_now_add=True)


class Comment(models.Model):
    author = models.ForeignKey(verbose_name='Автор', to=get_user_model(), related_name='comments', null=False,
                               blank=False,
                               on_delete=models.CASCADE)
    post = models.ForeignKey(verbose_name='Публикация', to='posts.Post', related_name='comments', null=False,
                             blank=False, on_delete=models.CASCADE)
    text = models.CharField(verbose_name='Текст', null=False, blank=False, max_length=200)
