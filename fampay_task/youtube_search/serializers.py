from rest_framework import serializers

from youtube_search.models import Video, Thumbnail, APIKey

class VideoGetSerializer(serializers.ModelSerializer):
    """
    Serializer for Video Model
    """
    thumbnails = serializers.SerializerMethodField()

    def get_thumbnails(self, object):
        """
        Function to get all the thumbnails of the video
        """
        thumbnails = Thumbnail.objects.filter(video=object)
        data = ThumbnailSerializer(thumbnails, many=True).data
        return data

    class Meta:
        model = Video
        fields = '__all__'


class ThumbnailSerializer(serializers.ModelSerializer):
    """
    Serializer for thumbnail model
    """

    class Meta:
        model = Thumbnail
        fields = ["id", "size", "url"]


class APIKeySerializer(serializers.ModelSerializer):
    """
    Serializer for APIKey Model
    """

    class Meta:
        model = APIKey
        fields = "__all__"