import requests

from datetime import datetime, timedelta

from fampay_task.settings import API_URL, SEARCH_QUERY, MAX_RESULTS
from youtube_search.models import APIKey


def youtube_videos():
    api_keys = APIKey.objects.filter(is_quota_exhausted=False)
    if not len(api_keys):
        return {}
    try:
        published_after = (datetime.utcnow() - timedelta(minutes=4)).isoformat() + "Z"
        published_before = (datetime.utcnow()).isoformat() + "Z"
        params = {
            "part": "snippet",
            "q": SEARCH_QUERY,
            "key": api_keys[0],
            "order": "date",
            "maxResults": MAX_RESULTS,
            "publishedAfter": published_after,
            "publishedBefore": published_before
        }
        response = requests.get(API_URL[0], params)
        if response.status_code == 200:
            return response.json()
        elif response.status_code == 403:
            api_keys[0].is_quota_exhausted = True
            api_keys[0].save()
        return {}
    except Exception as e:
        return {}
