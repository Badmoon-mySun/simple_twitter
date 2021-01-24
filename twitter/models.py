from time import time

from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class Tweet(models.Model):
    slug = models.CharField(max_length=100, unique=True, verbose_name='slug')
    author = models.ForeignKey(User, null=False, blank=False, verbose_name='Автор', on_delete=models.CASCADE)
    body = models.TextField(max_length=1500, blank=False, verbose_name='Содержание')
    date = models.DateTimeField(auto_now_add=True, verbose_name='Опубликовано')
    replying_tweet = models.ForeignKey('self', null=True, blank=True, verbose_name='Replying to', on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('tweet', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.id:
            new_slug = slugify(self.author.first_name, allow_unicode=True)
            new_slug += '-' + (str(int(time())))
            self.slug = new_slug

        super().save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Твиты'
        verbose_name = 'Твит'
        ordering = ['-date']
