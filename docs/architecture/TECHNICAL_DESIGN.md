# Technical Design Document
## Video Discovery & Creator Advertising Platform

**Version:** 1.0  
**Date:** 2026-11-02  
**Status:** Approved for Phase 1 Implementation

---

## 1. Architecture Overview

**Style:** Modular Monolith (Django) + Headless Frontend (Next.js)

```
┌─────────────────┐     ┌──────────────────────┐     ┌─────────────┐
│   Next.js       │────▶│  Django REST API     │────▶│ PostgreSQL  │
│   (Frontend)    │     │  + Admin + Celery    │     │             │
│   EN/FR/FA      │     │                      │     └─────────────┘
└─────────────────┘     │  - Accounts          │
                        │  - Channels/Videos   │     ┌─────────────┐
                        │  - Campaigns         │────▶│   Redis     │
                        │  - Credits Ledger    │     │ (Cache+Queue)
                        │  - Payments (Stripe) │     └─────────────┘
                        │  - Analytics         │
                        │  - Moderation        │
                        └──────────────────────┘
```

**Rationale for Monolith first:**
- Complex transactional domain (wallet, budgets, campaigns)
- Strong consistency requirements for money
- Faster development & easier testing at early stage
- Can extract services later (analytics, ad serving) if traffic demands

---

## 2. Technology Choices & Justification

| Component       | Choice                  | Alternatives Considered | Why Chosen |
|-----------------|-------------------------|-------------------------|------------|
| Backend         | Django 5 + DRF          | NestJS, FastAPI, Laravel | Built-in admin, ORM, auth, security, excellent for complex domains & financial ledgers |
| Frontend        | Next.js 15 + TS + Tailwind | Remix, SvelteKit       | Best SEO + SSR for discovery pages, large ecosystem, i18n mature |
| Auth            | django-allauth + Google | Auth0, Clerk, custom    | Free, full control, Google OAuth built-in, email verification |
| DB              | PostgreSQL 16           | MySQL, MongoDB          | ACID, JSON fields, full-text search, proven for financial apps |
| Queue           | Celery + Redis          | RQ, Dramatiq            | Mature, reliable for periodic tasks (campaign status, aggregation) |
| Payments        | Stripe                  | PayPal, local gateways  | Best international + webhook reliability + EUR support |
| i18n            | Django + next-intl      | react-i18next           | Official support + RTL for Persian |

---

## 3. Core Domain Modules

### 3.1 Accounts
- Custom User model
- Roles: Guest, Registered, Creator, Advertiser, Admin (and staff)
- Google OAuth + email/password
- Profile, language preference, notification settings

### 3.2 Channels & Videos
- Manual registration of YouTube channel URL / ID
- Optional YouTube Data API for verification (read-only, within ToS)
- Video cards with “Watch on YouTube” link only (no embed autoplay, no forced watch)

### 3.3 Advertising Engine
- Campaign types: Video Promotion, Channel Promotion, Homepage Featured, Category Featured, Search Sponsored, Creator Spotlight, Brand
- Pricing models: CPM, CPC, Fixed Placement (admin configurable)
- Targeting: language, country, category
- Frequency capping
- Status machine: Draft → Pending Review → Approved → Scheduled → Active → Paused / Completed / Rejected / Cancelled

### 3.4 Credits (Internal Wallet)
- Immutable ledger (double-entry style)
- Types: Purchase, Reservation, Charge, Refund, Admin Adjustment
- Idempotency keys on all financial operations
- No negative balance
- Credits are **not** withdrawable and **not** a cryptocurrency

### 3.5 Payments
- Stripe Checkout / Payment Intents
- Webhook-driven credit granting (never trust client)
- Packages + Subscriptions
- Invoices + Refunds

### 3.6 Analytics
- Platform-only metrics: Ad Impressions, Unique Impressions, Valid Clicks, CTR, Spend
- Never claim YouTube views or watch time
- Daily aggregation jobs
- CSV export

### 3.7 Moderation
- User reports (spam, illegal, copyright, misleading ads, etc.)
- Campaign pre-moderation for sensitive content
- Admin review queue

---

## 4. Security Architecture

- Password hashing: Argon2 / PBKDF2 (Django default)
- CSRF, XSS, SQLi protection (Django defaults + DRF)
- Rate limiting (django-ratelimit or custom middleware)
- RBAC with Django permissions + custom role checks
- All financial mutations via service layer + atomic transactions
- Secrets only in environment variables
- Audit log for admin actions and money movements
- GDPR: data export / account deletion endpoints

---

## 5. Multi-language & RTL

- Backend: Django translation files (en, fr, fa)
- Frontend: next-intl with locale routing (`/en/...`, `/fr/...`, `/fa/...`)
- Persian: full RTL layout support
- Dates & numbers: locale-aware formatting

---

## 6. SEO Requirements

- Clean URLs for videos & channels
- Meta title/description + Open Graph
- Sitemap.xml + robots.txt
- Structured data (VideoObject, Organization) where accurate
- Server-side rendering for public discovery pages

---

## 7. Scalability Path

1. Vertical scaling + connection pooling
2. Read replicas for analytics queries
3. Redis for ad selection cache + frequency maps
4. Later: extract Ad Serving service if needed
5. CDN for static assets & thumbnails
6. Celery workers horizontal scale

---

## 8. Deployment Recommendation (Production)

- Backend + Celery: Railway / Render / Fly.io / AWS ECS
- Frontend: Vercel or same platform
- Database: Managed PostgreSQL (Neon, Supabase, RDS, Railway)
- Redis: Upstash or managed
- Media: Cloudflare R2 or AWS S3
- Monitoring: Sentry + basic uptime

---

## 9. Estimated Infrastructure Cost (Early Stage)

| Item                | Monthly (approx EUR) |
|---------------------|----------------------|
| Managed Postgres    | 15–40                |
| Redis               | 0–15                 |
| App hosting         | 20–60                |
| Frontend            | 0–20 (Vercel free tier) |
| Stripe fees         | 1.5% + 0.25€ per txn |
| Domain + Email      | 10–20                |
| **Total early**     | **~50–150 EUR**      |

---

## 10. Next Immediate Steps

1. Implement User + Profile + Google login
2. Channel & Video CRUD + public listing
3. Basic campaign creation + moderation
4. Credit wallet + Stripe package purchase
5. Simple ad serving middleware
6. Admin dashboard using Django Admin + custom views

All code must be real and testable. No fake stats in production.
