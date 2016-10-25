from django.shortcuts import render
from video.apis.youtube import youtube_search

__all__ = ['search']


def search(request):

    keyword = request.GET.get( 'q', None )
    page_token = request.GET.get( 'page_token', None )

    if not keyword:
        return render( request, 'video/search.html', {} )


#    if keyword:


    result = youtube_search( keyword, page_token )
#    print(json.dumps(result, indent=2, sort_keys=True))

    context = {
        'keyword': keyword,
        'result': result,
    }

    return render( request, 'video/search.html', context )

