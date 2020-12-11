from django.db import models
from django.conf import settings
from django.utils import timezone

class Word(models.Model):
  word = models.CharField('word', max_length=200)
  definition = models.CharField('definition', max_length=200)
  author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=5)
  adding_date = models.DateTimeField('date of adding', default=timezone.now)

  def __str__(self):
    return self.word