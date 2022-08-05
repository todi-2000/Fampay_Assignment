from rest_framework import generics
from rest_framework.response import Response

from youtube_search.models import Video, APIKey
from youtube_search.serializers import VideoGetSerializer, APIKeySerializer

# Create your views here.
class VideoListView(generics.ListAPIView):
    """
    View to retrieve all the videos
    """
    model = Video
    serializer_class = VideoGetSerializer

    def get_queryset(self):
        return Video.objects.all().order_by('-published_date_time')


class APIKeyListCreateView(generics.ListCreateAPIView):
    """
    View to get and add APIKey
    """
    queryset = APIKey.objects.all()
    serializer_class = APIKeySerializer