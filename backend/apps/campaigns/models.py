from decimal import Decimal
from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _


class Campaign(models.Model):
    class Type(models.TextChoices):
        VIDEO_PROMOTION = "video_promotion", _("Video Promotion")
        CHANNEL_PROMOTION = "channel_promotion", _("Channel Promotion")
        HOMEPAGE_FEATURED = "homepage_featured", _("Homepage Featured")
        CATEGORY_FEATURED = "category_featured", _("Category Featured")
        SEARCH_SPONSORED = "search_sponsored", _("Search Sponsored")
        CREATOR_SPOTLIGHT = "creator_spotlight", _("Creator Spotlight")
        BRAND = "brand", _("Brand Campaign")

    class Status(models.TextChoices):
        DRAFT = "draft", _("Draft")
        PENDING_REVIEW = "pending_review", _("Pending Review")
        APPROVED = "approved", _("Approved")
        SCHEDULED = "scheduled", _("Scheduled")
        ACTIVE = "active", _("Active")
        PAUSED = "paused", _("Paused")
        COMPLETED = "completed", _("Completed")
        REJECTED = "rejected", _("Rejected")
        CANCELLED = "cancelled", _("Cancelled")

    class PricingModel(models.TextChoices):
        CPM = "cpm", _("CPM")
        CPC = "cpc", _("CPC")
        FIXED = "fixed", _("Fixed Placement")

    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="campaigns",
    )
    name = models.CharField(max_length=200)
    campaign_type = models.CharField(max_length=30, choices=Type.choices)
    target_video = models.ForeignKey(
        "videos.Video",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="campaigns",
    )
    target_channel = models.ForeignKey(
        "channels.Channel",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="campaigns",
    )
    creative_image = models.URLField(blank=True)
    creative_text = models.CharField(max_length=300, blank=True)
    destination_url = models.URLField(blank=True)
    status = models.CharField(
        max_length=20, choices=Status.choices, default=Status.DRAFT
    )
    pricing_model = models.CharField(
        max_length=10, choices=PricingModel.choices, default=PricingModel.CPM
    )
    budget_amount = models.DecimalField(
        max_digits=12, decimal_places=2, default=Decimal("0.00")
    )
    spent_amount = models.DecimalField(
        max_digits=12, decimal_places=2, default=Decimal("0.00")
    )
    reserved_amount = models.DecimalField(
        max_digits=12, decimal_places=2, default=Decimal("0.00")
    )
    start_date = models.DateTimeField(null=True, blank=True)
    end_date = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.name} ({self.get_status_display()})"

    @property
    def remaining_budget(self):
        return self.budget_amount - self.spent_amount


class CampaignTargeting(models.Model):
    campaign = models.OneToOneField(
        Campaign, on_delete=models.CASCADE, related_name="targeting"
    )
    languages = models.JSONField(default=list)  # ["en", "fa"]
    countries = models.JSONField(default=list)  # ["DE", "FR"]
    categories = models.ManyToManyField(
        "core.Category", blank=True, related_name="campaign_targetings"
    )


class CampaignPlacement(models.Model):
    class Placement(models.TextChoices):
        HOMEPAGE = "homepage", _("Homepage")
        CATEGORY = "category", _("Category Page")
        SEARCH = "search", _("Search Results")
        VIDEO_SIDEBAR = "video_sidebar", _("Video Sidebar")
        CHANNEL = "channel", _("Channel Page")

    campaign = models.ForeignKey(
        Campaign, on_delete=models.CASCADE, related_name="placements"
    )
    placement = models.CharField(max_length=30, choices=Placement.choices)
