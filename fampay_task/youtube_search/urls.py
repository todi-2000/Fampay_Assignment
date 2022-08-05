from django.urls import path

from youtube_search.views import VideoListView

urlpatterns = [
    path('videos/list/', VideoListView.as_view(), name='videos-list'),
]
