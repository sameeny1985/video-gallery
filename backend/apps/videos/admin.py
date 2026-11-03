from django.contrib import admin
from .models import Video, Tag


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ("title", "channel", "status", "language", "created_at")
    list_filter = ("status", "language")
    search_fields = ("title", "youtube_video_id")
    raw_id_fields = ("channel",)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
