from django.db import models
from django.utils.translation import gettext_lazy as _


class Category(models.Model):
    slug = models.SlugField(unique=True)
    name_en = models.CharField(max_length=100)
    name_fr = models.CharField(max_length=100, blank=True)
    name_fa = models.CharField(max_length=100, blank=True)
    icon = models.CharField(max_length=50, blank=True)  # emoji or icon name
    is_active = models.BooleanField(default=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name_plural = "categories"
        ordering = ["order", "name_en"]

    def __str__(self):
        return self.name_en

    def get_name(self, lang="en"):
        return getattr(self, f"name_{lang}", self.name_en) or self.name_en


class SystemSetting(models.Model):
    key = models.CharField(max_length=100, unique=True)
    value = models.JSONField(default=dict)
    description = models.TextField(blank=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.key
