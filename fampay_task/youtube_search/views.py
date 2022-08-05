from rest_framework import generics
from rest_framework.response import Response

from youtube_search.models import Video
from youtube_search.serializers import VideoGetSerializer 

# Create your views here.
class VideoListView(generics.ListAPIView):
    """
    View to retrieve all the videos
    """
    model = Video
    serializer_class = VideoGetSerializer

    def get_queryset(self):
        return Video.objects.all().order_by('-published_date_time')