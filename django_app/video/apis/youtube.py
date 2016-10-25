from googleapiclient.discovery import build
#from googleapiclient.errors import HttpError
#from oauth2client.tools import argparser
from video.models import Video

DEVELOPER_KEY = "AIzaSyDQFKJ4NDJKZhRw2qCxF4JfZOqlMvlHGOQ"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"


def youtube_search(keyword, page_token, max_results=5):
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
                    developerKey=DEVELOPER_KEY)

    search_res = youtube.search().list(
        q=keyword,
        part="id,snippet",
        type="video",
        maxResults=max_results,
        pageToken=page_token,
        ).execute()

    id_list = [item['id']['videoId'] for item in search_res['items']]

    print(id_list)

    detail_res = youtube.videos().list(
        id=','.join(id_list),
        part="id,snippet,statistics",
        ).execute()

#    print(detail_res)

    id_list = [item['id'] for item in detail_res['items']]
    video_list = Video.objects.filter(youtube_id__in=id_list)
    youtube_id_list = [video.youtube_id for video in video_list]

    print(youtube_id_list)

    for item in detail_res['items']:
        print(item['id'])
        if item['id'] in youtube_id_list:
            item['exist'] = True

    return detail_res
