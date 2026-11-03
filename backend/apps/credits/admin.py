from django.contrib import admin
from .models import CreditWallet, CreditTransaction, CreditPackage


@admin.register(CreditWallet)
class CreditWalletAdmin(admin.ModelAdmin):
    list_display = ("user", "balance", "reserved_balance", "updated_at")
    search_fields = ("user__email",)
    readonly_fields = ("balance", "reserved_balance")


@admin.register(CreditTransaction)
class CreditTransactionAdmin(admin.ModelAdmin):
    list_display = ("wallet", "type", "amount", "balance_after", "created_at")
    list_filter = ("type",)
    search_fields = ("wallet__user__email", "idempotency_key", "reference_id")
    readonly_fields = (
        "wallet", "type", "amount", "balance_after",
        "reference_id", "idempotency_key", "metadata", "created_at",
    )

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(CreditPackage)
class CreditPackageAdmin(admin.ModelAdmin):
    list_display = ("name", "credits_amount", "price_eur", "is_active", "order")
    list_editable = ("is_active", "order")
    prepopulated_fields = {"slug": ("name",)}
