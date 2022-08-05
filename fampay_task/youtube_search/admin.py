from django.contrib import admin

from youtube_search.models import Video, Thumbnail, APIKey

# # Register your models here.
class ThumbnailInline(admin.TabularInline):
    model = Thumbnail
    fields = ['url', 'size']

class VideoAdmin(admin.ModelAdmin):
    inlines = [ThumbnailInline]
    list_display = ['id', 'title', 'video_id', 'published_date_time', 'video_url']

class APIKeyAdmin(admin.ModelAdmin):
    list_display = ['key', 'is_quota_exhausted']

admin.site.register(Video, VideoAdmin)
admin.site.register(APIKey, APIKeyAdmin)

