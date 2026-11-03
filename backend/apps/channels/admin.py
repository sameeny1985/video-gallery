from django.contrib import admin
from .models import Channel


@admin.register(Channel)
class ChannelAdmin(admin.ModelAdmin):
    list_display = ("name", "owner", "status", "primary_language", "created_at")
    list_filter = ("status", "primary_language")
    search_fields = ("name", "youtube_channel_id", "owner__email")
    raw_id_fields = ("owner",)
