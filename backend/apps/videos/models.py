from django.db import models
from django.utils.translation import gettext_lazy as _


class Video(models.Model):
    class Status(models.TextChoices):
        DRAFT = "draft", _("Draft")
        PENDING = "pending", _("Pending Review")
        APPROVED = "approved", _("Approved")
        PUBLISHED = "published", _("Published")
        REJECTED = "rejected", _("Rejected")

    channel = models.ForeignKey(
        "channels.Channel",
        on_delete=models.CASCADE,
        related_name="videos",
    )
    title = models.CharField(max_length=300)
    youtube_url = models.URLField()
    youtube_video_id = models.CharField(max_length=32, unique=True)
    thumbnail_url = models.URLField(blank=True)
    description = models.TextField(blank=True)
    category = models.ForeignKey(
        "core.Category",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="videos",
    )
    language = models.CharField(max_length=5, default="en")
    status = models.CharField(
        max_length=20, choices=Status.choices, default=Status.DRAFT
    )
    tags = models.ManyToManyField("Tag", blank=True, related_name="videos")
    published_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.title


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name
