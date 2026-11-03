# Security & Compliance Notes

## Mandatory Practices

1. **Never store card data** – Stripe handles all PCI.
2. **Webhook verification** – Always verify Stripe signatures.
3. **Idempotency** – Every money-moving operation requires a unique idempotency key.
4. **Immutable ledger** – CreditTransaction rows are append-only.
5. **No negative balances** – Enforced in service layer + DB constraints where possible.
6. **RBAC** – Users only access their own resources; staff have explicit permissions.
7. **Rate limiting** – On login, registration, ad click, report endpoints.
8. **Input validation** – All URLs, IDs, amounts validated server-side.
9. **Secrets** – Only via environment variables / secret manager.
10. **Audit** – Log admin actions and all financial mutations.

## GDPR

- Account deletion endpoint that anonymizes / removes personal data.
- Data export endpoint.
- Cookie consent management on frontend.
- Privacy Policy & Terms must be reviewed by a lawyer before launch.

## YouTube Compliance

- No auto-play embeds that force watch.
- No rewards for watching / liking / subscribing.
- Clear separation: platform stats ≠ YouTube stats.
- Optional YouTube API usage only for verification within official ToS.

## Recommended Tools

- django-axes or similar for login protection
- Sentry for error tracking
- Regular dependency updates (`pip-audit` / `safety`)
