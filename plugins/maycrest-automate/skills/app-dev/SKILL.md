---
name: app-dev
description: Comprehensive application development lifecycle skill for Maycrest Group's Expo + Supabase + Stripe stack. Covers client app builds (booking apps, business tools) AND internal platform development (TIE - Threat Intelligence Engine). Triggers on mobile app development, React Native, Expo, Supabase, booking app, SaaS platform, multi-tenant, white-label app, app store submission, NativeWind, payment integration, Stripe Connect, client handoff, app maintenance agreement, TIE platform, threat modeling SaaS, cybersecurity dashboard, RBAC, RLS policies, UI/UX design system, app pricing, SOW creation, discovery sprint, EAS build, OTA updates, push notifications. Also use when the user mentions anything about building apps for small businesses, designing beautiful interfaces, creating design systems, or planning app architecture.
version: 1.0.0
---

# Maycrest App Development

## Overview

Full application development lifecycle for Maycrest Group. Covers two tracks:

1. **Client Apps** — Booking apps, business tools, and custom mobile apps for SMB clients
2. **Internal Platform** — TIE (Threat Intelligence Engine) SaaS platform

## Tech Stack

| Layer | Technology |
|-------|-----------|
| Frontend | Expo (React Native) + NativeWind |
| Backend | Supabase (Postgres, Auth, Edge Functions, Realtime) |
| Payments | Stripe / Stripe Connect |
| Build/Deploy | EAS Build, EAS Submit, OTA Updates |
| Auth | Supabase Auth + Sign in with Apple + Google |
| Push | Expo Push Notifications + APNs |
| State | Zustand or React Context |
| Navigation | Expo Router (file-based) |

## Development Phases

### Phase 1: Discovery Sprint (1-2 weeks)
- Requirements gathering
- User stories and flows
- Database schema design
- Architecture decisions
- SOW creation and pricing

### Phase 2: Foundation (1-2 weeks)
- Expo project scaffold with NativeWind
- Supabase project setup (auth, database, storage)
- Navigation structure
- Design system tokens (colors, typography, spacing)
- Core component library

### Phase 3: Feature Build (2-4 weeks)
- Screen-by-screen implementation
- API integration (Edge Functions)
- Payment flow (Stripe)
- Push notifications
- Real-time features (Supabase Realtime)

### Phase 4: Polish & QA (1 week)
- UI/UX polish pass
- Performance optimization
- Error handling and edge cases
- Accessibility review
- Device testing matrix

### Phase 5: Launch (1 week)
- EAS Build (iOS + Android)
- App Store / Play Store submission
- Client handoff documentation
- Maintenance agreement setup

## Design System

### Principles
- Mobile-first, thumb-friendly
- Dark mode as default, light mode available
- Consistent spacing scale (4, 8, 12, 16, 24, 32, 48)
- Maximum 2 font families
- Accessible contrast ratios (WCAG AA minimum)

### Component Library
- Buttons (primary, secondary, ghost, destructive)
- Cards (content, stat, action)
- Inputs (text, select, date, toggle)
- Navigation (tab bar, header, drawer)
- Modals (bottom sheet, center, full screen)
- Lists (flat, sectioned, swipeable)
- Loading states (skeleton, spinner, progress)

## Architecture Patterns

### Multi-Tenant (TIE Platform)
- Organization-scoped data with RLS
- Role-based access (admin, analyst, viewer)
- Tenant isolation at database level
- Shared infrastructure, isolated data

### Client Apps
- Single-tenant per deployment
- White-label ready (theme tokens, branding config)
- Offline-first where applicable
- Deep linking support

## Pricing Model

### Client App Builds
- Discovery Sprint: $2,500 - $5,000
- MVP Build: $8,000 - $15,000
- Full Build: $15,000 - $35,000
- Monthly Maintenance: $500 - $2,000/month

### SOW Template Structure
1. Project Overview
2. Scope of Work (in/out of scope)
3. Deliverables
4. Timeline & Milestones
5. Investment & Payment Schedule
6. Maintenance & Support Terms
7. Assumptions & Dependencies

## Rules

- Always start with a discovery sprint before quoting
- Use Expo Router file-based routing (never React Navigation directly)
- NativeWind for all styling (never inline StyleSheet unless necessary)
- Supabase RLS on every table, no exceptions
- TypeScript strict mode
- Environment variables via EAS secrets
- Never store secrets in code or git
- Test on both iOS and Android before any client demo
