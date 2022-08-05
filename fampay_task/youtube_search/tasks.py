from dateutil import parser

from celery import shared_task
from django.db import transaction

from fampay_task.settings import VIDEO_BASE_URL
from youtube_search.models import Video, Thumbnail
from youtube_search.utils import youtube_videos

@shared_task(name="add_video_db")
def add_video_db():
    """
    Fetch video using youtube api and add it to the db.
    """
    with transaction.atomic():
        videos_json = youtube_videos()
        if videos_json:
            for item in videos_json["items"]:
                video_url = VIDEO_BASE_URL + item["id"]["videoId"]
                snippet = item["snippet"]
                video = Video(
                    title=snippet["title"],
                    description=snippet["description"],
                    published_date_time=parser.parse(snippet["publishTime"]),
                    video_id=item["id"]["videoId"],
                    video_url=video_url
                )
                video.save()

                for size in snippet["thumbnails"]:
                    thumbnail = Thumbnail(
                        video=video,
                        size=size,
                        url=snippet["thumbnails"][size]["url"]
                    )
                    thumbnail.save()



    
