from django.db import models
from django.conf import settings


class Album(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL)
    title = models.CharField(max_length=30)
    desc = models.CharField(max_length=80, blank=True)


class Photo(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL)
    album = models.ForeignKey(Album)
    title = models.CharField(max_length=30)
    desc = models.CharField(max_length=80, blank=True)
    img = models.ImageField(upload_to='photo')


