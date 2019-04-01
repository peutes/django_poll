from django.db import models


class Book(models.Model):
  """書籍"""
  name = models.CharField(verbose_name='書籍名', max_length=255)
  publisher = models.CharField(verbose_name='出版社', max_length=255, blank=true)
  page = models.IntegerField(verbose_name='ページ数', )
