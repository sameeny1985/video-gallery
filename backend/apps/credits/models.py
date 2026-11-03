from decimal import Decimal
from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _


class CreditWallet(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="wallet",
    )
    balance = models.DecimalField(
        max_digits=12, decimal_places=2, default=Decimal("0.00")
    )
    reserved_balance = models.DecimalField(
        max_digits=12, decimal_places=2, default=Decimal("0.00")
    )
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Wallet of {self.user.email}: {self.balance}"

    @property
    def available_balance(self):
        return self.balance - self.reserved_balance


class CreditTransaction(models.Model):
    """Immutable ledger. Never update or delete rows."""

    class Type(models.TextChoices):
        PURCHASE = "purchase", _("Credit Purchase")
        RESERVATION = "reservation", _("Campaign Reservation")
        CHARGE = "charge", _("Campaign Charge")
        REFUND = "refund", _("Campaign Refund")
        ADJUSTMENT = "adjustment", _("Administrative Adjustment")

    wallet = models.ForeignKey(
        CreditWallet, on_delete=models.PROTECT, related_name="transactions"
    )
    type = models.CharField(max_length=20, choices=Type.choices)
    amount = models.DecimalField(max_digits=12, decimal_places=2)  # positive = credit in
    balance_after = models.DecimalField(max_digits=12, decimal_places=2)
    reference_id = models.CharField(max_length=64, blank=True)  # campaign_id, payment_id...
    idempotency_key = models.CharField(max_length=64, unique=True)
    metadata = models.JSONField(default=dict, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]
        indexes = [
            models.Index(fields=["wallet", "-created_at"]),
            models.Index(fields=["idempotency_key"]),
        ]

    def __str__(self):
        return f"{self.type} {self.amount} @ {self.created_at}"


class CreditPackage(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    credits_amount = models.DecimalField(max_digits=12, decimal_places=2)
    price_eur = models.DecimalField(max_digits=10, decimal_places=2)
    validity_days = models.PositiveIntegerField(default=365)
    features = models.JSONField(default=list, blank=True)
    is_active = models.BooleanField(default=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order", "price_eur"]

    def __str__(self):
        return f"{self.name} – {self.credits_amount} credits"
