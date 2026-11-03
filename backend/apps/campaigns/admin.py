from django.contrib import admin
from .models import Campaign, CampaignTargeting, CampaignPlacement


class PlacementInline(admin.TabularInline):
    model = CampaignPlacement
    extra = 1


@admin.register(Campaign)
class CampaignAdmin(admin.ModelAdmin):
    list_display = (
        "name", "owner", "campaign_type", "status",
        "budget_amount", "spent_amount", "created_at",
    )
    list_filter = ("status", "campaign_type", "pricing_model")
    search_fields = ("name", "owner__email")
    raw_id_fields = ("owner", "target_video", "target_channel")
    inlines = [PlacementInline]


@admin.register(CampaignTargeting)
class CampaignTargetingAdmin(admin.ModelAdmin):
    raw_id_fields = ("campaign",)
