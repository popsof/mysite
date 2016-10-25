from django.conf.urls import url

from . import views

app_name = 'sns'

urlpatterns =[
    url(r'^$', views.index, name='index'),
    url(r'^facebook/friends-ranking/$', views.friends_ranking, name='friends_ranking'),
]