from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from photo.models import Album, PhotoLike, PhotoDislike
from photo.forms import AlbumForm, PhotoForm

__all__ = [
    'album_list',
    'album_new',
    'album_detail',
]


#@login_required
def album_list(request):
    # albums = Album.objects.filter(owner=request.user).order_by('-created_date')
    albums = Album.objects.order_by('-created_date')

    context = {
        'albums': albums,
    }

    return render(request, 'photo/album_list.html', context)


@login_required
def album_new(request):
    if request.method != 'POST':
        form = AlbumForm()
        return render(request, 'photo/album_edit.html', {'form': form})

    form = AlbumForm(request.POST)

    if form.is_valid():
        album = form.save(commit=False)
        album.owner = request.user
        album.save()
        return redirect('photo:album_detail', album.id)


@login_required
def album_detail(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    photos = album.photo_set.order_by('-created_date')
    form = PhotoForm()
    
    id_list = [photo.id for photo in photos]

    like_list = PhotoLike.objects.\
                    filter(user=request.user).filter(photo__in=id_list)
    like_ids = [like.photo.id for like in like_list]
    for photo in photos:
        if photo.id in like_ids:
            photo.like = True

    like_list = PhotoDislike.objects.\
                    filter(user=request.user).filter(photo__in=id_list)
    like_ids = [like.photo.id for like in like_list]
    for photo in photos:
        if photo.id in like_ids:
            photo.dislike = True

    context = {
        'album': album,
        'photos': photos,
        'form': form,
    }

    return render(request, 'photo/album_detail.html', context)



