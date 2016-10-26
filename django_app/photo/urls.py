from django.conf.urls import url
from . import views

app_name='photo'

urlpatterns = [
    url(r'^$', views.album_list, name='album_list'),
    url(r'^album/new/$', views.album_new, name='album_new'),
    url(r'^album/(\d+)/$', views.album_detail, name='album_detail'),
    url(r'^album/(\d+)/add/$', views.photo_add, name='photo_add'),
    url(r'^album/(\d+)/like/(\d+)/$', views.photo_like, name='photo_like'),
    url(r'^album/(\d+)/dislike/(\d+)/$', views.photo_dislike, name='photo_dislike'),
    url(r'^photo/my/$', views.photo_my, name='photo_my'),
    url(r'^photo/like/$', views.photo_my_like, name='photo_my_like'),
    url(r'^photo/dislike/$', views.photo_my_dislike, name='photo_my_dislike'),
]

