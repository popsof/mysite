from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model

from photo.forms import PhotoForm
from photo.models import Album, Photo, PhotoLike, PhotoDislike

__all__ = [
    'photo_my',
    'photo_my_like',
    'photo_my_dislike',
]


@login_required
def photo_my(request):
    photos = Photo.objects.select_related('album').\
                    filter(owner=request.user).order_by('-created_date')
    context = {
        'title': '내가 올린 사진모음',
        'photos': photos,
        }
    return render(request, 'photo/photo_list.html', context)


@login_required
def photo_my_like(request):
    photos = request.user.photo_set_like_users.\
                    select_related('album').order_by('-created_date')
                    
    context = {
        'title': '내가 좋아하는 사진모음',
        'photos': photos,
        }
    return render(request, 'photo/photo_list.html', context)


@login_required
def photo_my_dislike(request):
    photos = request.user.photo_set_dislike_users.\
                    select_related('album').order_by('-created_date')
                    
    context = {
        'title': '내가 싫어하는 사진모음',
        'photos': photos,
        }
    return render(request, 'photo/photo_list.html', context)

