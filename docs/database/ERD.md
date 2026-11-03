# Database Design (ERD Summary)

PostgreSQL – Normalized with proper indexes and soft-delete where needed.

## Core Tables

### users (extends AbstractUser)
- id (UUID or BigAuto)
- email (unique)
- password
- is_active, is_staff, is_superuser
- date_joined, last_login
- role (choices or separate Role model)
- preferred_language
- created_at, updated_at

### user_profiles
- user (OneToOne)
- display_name, avatar_url, bio
- country, timezone
- notification_preferences (JSON)

### channels
- id
- owner (FK users)
- name, youtube_url, youtube_channel_id (unique)
- avatar_url, description
- category (FK), primary_language
- target_country (optional)
- status (pending/approved/rejected)
- is_verified (optional via YT API)
- created_at, updated_at

### videos
- id
- channel (FK)
- title, youtube_url, youtube_video_id (unique)
- thumbnail_url, description
- category (FK), language
- tags (M2M)
- status (draft/pending/approved/published/rejected)
- published_at, created_at, updated_at

### categories
- id, slug, name_en, name_fr, name_fa
- icon, is_active, order

### campaigns
- id
- owner (FK users)
- name, campaign_type (choices)
- target_video / target_channel (nullable FKs)
- creative_image, creative_text, destination_url
- status (draft → … → completed)
- start_date, end_date
- budget_amount (Decimal), spent_amount (Decimal)
- pricing_model (CPM/CPC/FIXED)
- created_at, updated_at

### campaign_targeting
- campaign (FK)
- languages (Array or M2M)
- countries (Array)
- categories (M2M)

### campaign_placements
- campaign (FK)
- placement (homepage, category, search, etc.)

### credit_wallets
- user (OneToOne)
- balance (Decimal, precision 12,2)
- reserved_balance (Decimal)
- updated_at

### credit_transactions (Immutable Ledger)
- id
- wallet (FK)
- type (purchase, reservation, charge, refund, adjustment)
- amount (Decimal, signed or absolute + direction)
- balance_after
- reference_id (campaign / payment / etc.)
- idempotency_key (unique)
- metadata (JSON)
- created_at (immutable)

### credit_packages
- id, name, credits_amount, price_eur, validity_days
- features (JSON), is_active, order

### subscriptions
- user, package / plan
- status, current_period_start/end
- stripe_subscription_id

### payments
- id, user, amount, currency, status
- stripe_payment_intent_id / checkout_session_id
- package (FK nullable)
- created_at, updated_at

### invoices / refunds
- Standard fields + links to payments

### ad_impressions
- id, campaign, user (nullable for anonymous)
- session_id / fingerprint (hashed)
- placement, created_at
- Indexes for unique + frequency

### ad_clicks
- id, impression (FK optional), campaign, user
- is_valid (bot detection later)
- created_at

### reports (moderation)
- reporter, content_type, object_id
- reason, description, status
- reviewed_by, reviewed_at

### notifications
- user, type, title, body, is_read, data (JSON), created_at

### system_settings
- key, value (JSON), description

---

## Important Constraints

- credit_transactions never updated/deleted (append-only)
- wallet.balance never changed without a corresponding transaction
- campaign.spent_amount updated only inside atomic reservation/charge
- Unique constraints on youtube_channel_id, youtube_video_id
- Proper indexes on (campaign, created_at), (user, created_at), status fields

## Decimal Precision
All money fields: `max_digits=12, decimal_places=2` (or 4 for intermediate CPM calculations if needed).
