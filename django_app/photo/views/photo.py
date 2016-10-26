from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from photo.forms import PhotoForm
from photo.models import Album, Photo, PhotoLike, PhotoDislike

__all__ = [
    'photo_add',
    'photo_like',
    'photo_dislike',
]


@login_required
def photo_add(request, album_id):
    if request.method != 'POST':
        return redirect('photo:album_detail', album_id)

    album = get_object_or_404(Album, pk=album_id)

    form = PhotoForm(request.POST, request.FILES)
    if not form.is_valid():
        return redirect('photo:album_detail', album_id)

    album.photo_set.create(
        owner=request.user,
        title=form.cleaned_data['title'],
        desc=form.cleaned_data['desc'],
        img=form.cleaned_data['img'],
#        img=request.FILES['img'],
    )

    return redirect('photo:album_detail', album_id)


@login_required
def photo_like(request, album_id, photo_id):
    album = get_object_or_404(Album, pk=album_id)
    photo = get_object_or_404(album.photo_set, pk=photo_id)

    PhotoLike.objects.create(photo=photo, user=request.user)
    return redirect('photo:album_detail', album_id)

@login_required
def photo_dislike(request, album_id, photo_id):
    album = get_object_or_404(Album, pk=album_id)
    photo = get_object_or_404(album.photo_set, pk=photo_id)

    PhotoDislike.objects.create(photo=photo, user=request.user)
    return redirect('photo:album_detail', album_id)

