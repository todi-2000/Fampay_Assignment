from django.urls import path

from youtube_search.views import VideoListView, APIKeyListCreateView

urlpatterns = [
    path('videos/list/', VideoListView.as_view(), name='videos-list'),
    path('apikey/', APIKeyListCreateView.as_view(), name='api-key'),
]
