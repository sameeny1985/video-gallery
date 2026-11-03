# Video Discovery & Creator Advertising Platform

**Project Name:** Video Discovery & Creator Advertising Platform  
**Type:** International Video Discovery & Advertising Marketplace  
**Status:** Phase 0 – Technical Design + Project Skeleton (Ready for GitHub)

This repository contains the complete technical foundation for an independent, scalable, international platform that connects video creators, YouTube channels, audiences, and advertisers.

**Important:** This is **not** a YouTube view/watch-time/subscriber boosting service.  
All advertising is platform-internal (impressions & clicks on *this* site only).  
Full compliance with YouTube Terms of Service and API policies is mandatory.

---

## 1. Vision

A professional SaaS marketplace where:

- Creators register channels & videos
- Users discover content
- Creators & advertisers run paid promotion campaigns (CPM / CPC / Fixed Placement)
- Internal credit wallet + Stripe payments
- Full analytics of *platform* impressions & clicks only
- Multi-language (EN / FR / FA) with RTL support
- Google OAuth login

---

## 2. Tech Stack (Recommended & Implemented in Skeleton)

| Layer              | Technology                          | Reason |
|--------------------|-------------------------------------|--------|
| Backend            | Django 5 + Django REST Framework    | Complex business logic, roles, ledger, admin, security, rapid development |
| Auth               | django-allauth + Google OAuth2      | Secure Google login + email/password |
| Database           | PostgreSQL 16                       | ACID, strong consistency for financial ledger |
| Cache / Queue      | Redis + Celery                      | Background jobs, frequency capping, analytics aggregation |
| Frontend           | Next.js 15 (App Router) + TypeScript + Tailwind CSS | SEO, SSR, modern UI, i18n |
| Payments           | Stripe                              | EUR primary currency |
| Storage            | Local (dev) / S3-compatible (prod)  | Thumbnails, reports |
| i18n               | Django i18n + next-intl             | EN / FR / FA + RTL |
| Container          | Docker + Docker Compose             | Local & production parity |

**Why Django over pure Node?**  
Heavy transactional logic (credit ledger, campaign budgets, moderation, audit logs), built-in admin, mature RBAC, excellent security defaults. Frontend remains modern with Next.js.

---

## 3. Project Structure

```
video-discovery-platform/
├── backend/                 # Django project
│   ├── apps/
│   │   ├── accounts/        # Users, profiles, roles, Google OAuth
│   │   ├── channels/        # YouTube channels
│   │   ├── videos/          # Video metadata
│   │   ├── campaigns/       # Ad campaigns + targeting + placements
│   │   ├── credits/         # Wallet + immutable ledger
│   │   ├── payments/        # Stripe + packages + invoices
│   │   ├── analytics/       # Impressions, clicks, reports
│   │   ├── moderation/      # Reports + content review
│   │   ├── notifications/   # In-app + email
│   │   └── core/            # Shared utilities, categories, settings
│   ├── config/              # Settings, urls, wsgi/asgi
│   └── manage.py
├── frontend/                # Next.js application
├── docs/                    # Full technical documentation
├── docker/                  # Dockerfiles
├── docker-compose.yml
├── .env.example
└── README.md
```

---

## 4. Quick Start (Local Development)

### Prerequisites
- Docker & Docker Compose
- Node.js 20+
- Python 3.12+
- Google Cloud Console project (for OAuth)
- Stripe account (test mode)

### 1. Clone & Configure

```bash
git clone <your-repo>
cd video-discovery-platform
cp .env.example .env
# Edit .env with your secrets
```

### 2. Start services

```bash
docker compose up -d --build
```

### 3. Backend setup

```bash
docker compose exec backend python manage.py migrate
docker compose exec backend python manage.py createsuperuser
docker compose exec backend python manage.py loaddata initial_categories  # if provided
```

### 4. Frontend

```bash
cd frontend
npm install
npm run dev
```

- Backend API: http://localhost:8000  
- Frontend: http://localhost:3000  
- Admin: http://localhost:8000/admin  

---

## 5. Environment Variables

See `.env.example` for the complete list. Critical ones:

```env
# Django
SECRET_KEY=...
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

# Database
DATABASE_URL=postgres://vdp:vdp@db:5432/vdp

# Redis
REDIS_URL=redis://redis:6379/0

# Google OAuth
GOOGLE_CLIENT_ID=...
GOOGLE_CLIENT_SECRET=...

# Stripe
STRIPE_PUBLIC_KEY=pk_test_...
STRIPE_SECRET_KEY=sk_test_...
STRIPE_WEBHOOK_SECRET=whsec_...

# Frontend
NEXT_PUBLIC_API_URL=http://localhost:8000/api/v1
NEXT_PUBLIC_SITE_URL=http://localhost:3000
```

---

## 6. Google Login Setup

1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create project → APIs & Services → Credentials → Create OAuth 2.0 Client ID
3. Application type: Web application
4. Authorized redirect URIs:
   - `http://localhost:8000/accounts/google/login/callback/`
   - `https://yourdomain.com/accounts/google/login/callback/`
5. Copy Client ID & Secret into `.env`
6. In Django admin → Social Applications → Add Google app (or use settings-based config already prepared)

---

## 7. Development Phases (from original requirements)

| Phase | Focus                          | Status in this repo |
|-------|--------------------------------|---------------------|
| 1     | Analysis + Architecture + DB   | ✅ Complete docs    |
| 2     | Core (Auth, Channels, Videos)  | Skeleton ready      |
| 3     | Advertising Engine             | Models + stubs      |
| 4     | Credits + Stripe               | Models + stubs      |
| 5     | Dashboards                     | Structure ready     |
| 6     | i18n, SEO, Security, Tests     | Planned             |

---

## 8. Key Compliance Rules (Non-negotiable)

- No reward for watching YouTube videos
- No selling/buying watch time, views, likes, subscribers, comments
- No forced engagement
- All stats shown are **platform-only** (Ad Impressions / Valid Clicks)
- Clear “Sponsored” labeling
- GDPR-ready data handling
- YouTube API used only within official terms (optional channel verification)

---

## 9. Documentation

- `docs/architecture/TECHNICAL_DESIGN.md` – Full architecture
- `docs/database/ERD.md` + models
- `docs/roadmap/PHASES.md`
- `docs/security/SECURITY.md`
- `docs/api/API_OVERVIEW.md`

---

## 10. License & Legal

Before commercial launch:
- Have Privacy Policy, Terms, Advertising Policy, Cookie Policy reviewed by a lawyer
- Ensure GDPR compliance (EU users)
- Review YouTube API Services Terms

---

**Next steps after cloning:**
1. Fill `.env`
2. Run `docker compose up`
3. Create superuser
4. Implement Phase 2 features following the models and docs

This foundation is designed to grow into a real independent digital business.
