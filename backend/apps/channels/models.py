from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _


class Channel(models.Model):
    class Status(models.TextChoices):
        PENDING = "pending", _("Pending Review")
        APPROVED = "approved", _("Approved")
        REJECTED = "rejected", _("Rejected")

    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="channels",
    )
    name = models.CharField(max_length=200)
    youtube_url = models.URLField()
    youtube_channel_id = models.CharField(max_length=64, unique=True, blank=True)
    avatar_url = models.URLField(blank=True)
    description = models.TextField(blank=True)
    category = models.ForeignKey(
        "core.Category",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="channels",
    )
    primary_language = models.CharField(max_length=5, default="en")
    target_country = models.CharField(max_length=2, blank=True)
    status = models.CharField(
        max_length=20, choices=Status.choices, default=Status.PENDING
    )
    is_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.name
