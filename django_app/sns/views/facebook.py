import json

import requests
from django.http import HttpResponse
from django.urls import reverse

from apis import facebook

__all__ = [
    'friends_ranking',
]


def friends_ranking(request):
    if request.GET.get('error'):
        return HttpResponse( '사용자 로그인 거부' )
    if request.GET.get('code'):
        redirect_uri = 'http://{host}{url}'.format(
            host=request.META['HTTP_HOST'],
            url=reverse('sns:friends_ranking')
        )

        code = request.GET.get('code')
        access_token = facebook.get_access_token(code, redirect_uri)
        user_id = facebook.get_user_id_from_token(access_token)

        url_feed = 'https://graph.facebook.com/v2.8/{}/feed?' \
                    'fields=comments{{from,comments}}&' \
                    'access_token={}'.format( user_id, access_token )

        r = requests.get( url_feed )
        rsp_feed = r.json()
        json_data = json.dumps( rsp_feed, indent=2 )
        return HttpResponse( json_data )



        return HttpResponse( '{}<br>{}'.format( redirect_uri, access_token) )