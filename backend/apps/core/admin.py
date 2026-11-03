from django.contrib import admin
from .models import Category, SystemSetting


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name_en", "slug", "is_active", "order")
    prepopulated_fields = {"slug": ("name_en",)}
    list_editable = ("is_active", "order")


@admin.register(SystemSetting)
class SystemSettingAdmin(admin.ModelAdmin):
    list_display = ("key", "updated_at")
