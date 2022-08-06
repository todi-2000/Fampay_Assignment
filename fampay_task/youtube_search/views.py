from rest_framework import filters
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination

from youtube_search.models import Video, APIKey
from youtube_search.serializers import VideoGetSerializer, APIKeySerializer

# Create your views here.
class VideoListPagination(PageNumberPagination):
    """
    View to paginate videos
    """
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 10


class VideoListView(generics.ListAPIView):
    """
    View to retrieve all the videos
    """
    serializer_class = VideoGetSerializer
    pagination_class = VideoListPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'description']

    def get_queryset(self):
        return Video.objects.all().order_by('-published_date_time')


class APIKeyListCreateView(generics.ListCreateAPIView):
    """
    View to get and add APIKey
    """
    queryset = APIKey.objects.all()
    serializer_class = APIKeySerializer