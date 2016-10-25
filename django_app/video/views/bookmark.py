from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from video.models import Video

__all__ = ['bookmark_add', 'bookmark_list', 'bookmark_detail']


def bookmark_add(request):
    path = request.POST.get('next')

    try:
        kind = request.POST.get('kind')
        video_id = request.POST.get('video_id')
        title = request.POST.get('title')
        description = request.POST.get('description')
        published_date = request.POST.get('published_date')
        thumbnail = request.POST.get('thumbnail')

        video = Video.objects.create(
                kind=kind,
                youtube_id=video_id,
                title=title,
                description=description,
                published_date=published_date,
                thumbnail=thumbnail
        )
        msg = '{} 영상을 북마크 등록에 성곡했습니다.'.format(video.title)
        messages.success(request, msg)
    except Exception as e:
        msg = 'Exception! {}'.format(e.args)
        messages.error( request, msg )

    if path:
        return redirect(path)
    else:
        return redirect( 'video:bookmark_list' )


def bookmark_list(request):

    videos = Video.objects.all()
    context = {
        'videos': videos,
    }

    return render( request, 'video/bookmark_list.html', context )


def bookmark_detail(request, pk):

    video = get_object_or_404(Video, pk=pk)
    context = {
        'video': video
    }

    return render( request, 'video/bookmark_detail.html', context )




