from django.conf.urls import url
from video import views

app_name = 'video'
urlpatterns = [
    url(r'^bookmark/list/$', views.bookmark_list, name='bookmark_list'),
    url(r'^bookmark/detail/(\d+)$', views.bookmark_detail, name='bookmark_detail'),
    url(r'^bookmark/add/$', views.bookmark_add, name='bookmark_add'),
    url(r'^search/$', views.search, name='search'),
]