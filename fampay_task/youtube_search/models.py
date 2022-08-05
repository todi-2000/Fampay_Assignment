from django.db import models

# Create your models here.
SIZE_CHOICES =(
    ("default", "default"),
    ("medium", "medium"),
    ("high", "high"),
)

class Video(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    published_date_time = models.DateTimeField()
    video_id = models.CharField(max_length=255)
    video_url = models.URLField()

    class Meta:
        verbose_name = "Video"
        verbose_name_plural = "Videos"

    def __str__(self):
        return self.title

class Thumbnail(models.Model):
    video = models.ForeignKey(Video, on_delete=models.CASCADE, related_name='thumbnails')
    size = models.CharField(max_length=255, choices=SIZE_CHOICES)
    url = models.URLField()

    class Meta:
        verbose_name = "Thumbnail"
        verbose_name_plural = "Thumbnails"

    def __str__(self):
        return f"{self.video.title} {self.size}"

class APIKey(models.Model):
    key = models.CharField(max_length=255)
    is_quota_exhausted = models.BooleanField(default=False)

    class Meta:
        verbose_name = "API Key"
        verbose_name_plural = "API Keys"

    def __str__(self):
        return self.key