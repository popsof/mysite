from django.db import models
from django.conf import settings


class Album(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL)
    title = models.CharField(max_length=30)
    desc = models.CharField(max_length=80, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)


class Photo(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL)
    album = models.ForeignKey(Album)
    title = models.CharField(max_length=30)
    desc = models.CharField(max_length=80, blank=True)
    img = models.ImageField(upload_to='photo')
    created_date = models.DateTimeField(auto_now_add=True)

    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL,
                                through='PhotoLike',
                                related_name='photo_set_like_users')

    dislike_users = models.ManyToManyField(settings.AUTH_USER_MODEL,
                                through='PhotoDislike',
                                related_name='photo_set_dislike_users')


class PhotoLike(models.Model):
    photo = models.ForeignKey(Photo)
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    create_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = (('photo', 'user'),)


class PhotoDislike(models.Model):
    photo = models.ForeignKey(Photo)
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    create_date = models.DateTimeField(auto_now_add=True)


