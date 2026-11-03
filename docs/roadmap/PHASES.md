# Development Roadmap

## Phase 0 – Foundation (This repository)
- [x] Technical Design Document
- [x] Database ERD & core models
- [x] Project structure + Docker
- [x] Google OAuth configuration
- [x] Environment template
- [x] Basic health endpoint

## Phase 1 – Core Platform (2–4 weeks)
- Custom User + Profile + Google login working
- Channel registration & approval flow
- Video registration & public listing
- Categories + Search + Filters
- Public video/channel detail pages (SEO ready)
- Basic Django Admin configuration

## Phase 2 – Advertising Engine (3–5 weeks)
- Campaign CRUD + status machine
- Targeting & placements
- Budget reservation from wallet
- Simple ad selection service + frequency capping
- Impression & click tracking endpoints
- Campaign moderation queue

## Phase 3 – Financial System (2–3 weeks)
- Credit wallet + immutable ledger service
- Credit packages
- Stripe Checkout + webhook (idempotent)
- Invoices & basic refunds
- Transaction history for users

## Phase 4 – Dashboards & Analytics (2–3 weeks)
- User / Creator / Advertiser dashboards
- Real charts (platform impressions, CTR, spend)
- CSV export
- Admin overview metrics

## Phase 5 – Polish & Launch Readiness (2–4 weeks)
- Full i18n (EN/FR/FA + RTL)
- Notifications (in-app + email)
- Content reporting & moderation UI
- Security hardening, rate limits, audit logs
- SEO (sitemap, meta, structured data)
- Automated tests for critical paths
- Production deployment guides
- Legal pages (Privacy, Terms, Advertising Policy)

---

**Estimated total to MVP:** 12–20 weeks with 1–2 full-time developers.  
**Critical path:** Wallet + Stripe + Campaign lifecycle must be solid before public launch.
