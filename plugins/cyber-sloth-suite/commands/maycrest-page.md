---
description: "Design and build a Maycrest website page or component. Usage: /maycrest-page [page name or component]"
---

# Maycrest Page Builder

You are designing and building a page or component for the Maycrest website. The user has specified which page or component they need.

## Step 1: Context
Invoke `cyber-sloth-suite:maycrest-web-design` skill to load the full design system (colors, typography, spacing, component patterns, brand guidelines).

## Step 2: Page Specification
Based on the requested page/component, define:
- **Purpose**: What this page needs to accomplish
- **Target user**: Who lands here and what they're looking for
- **Key sections**: Ordered list of content blocks
- **Primary CTA**: The one thing we want the visitor to do
- **Content needs**: Copy, images, data, or assets required

## Step 3: Design
Create the page using Maycrest design tokens:
- Dark mode primary experience
- Accent colors from the design system
- Component patterns from the library
- Motion/animation specifications
- Responsive breakpoints (mobile, tablet, desktop)

## Step 4: Build
Generate production-ready code:
- React/Next.js component with Tailwind CSS
- Responsive layout
- Accessibility attributes
- Animation with Framer Motion (respecting prefers-reduced-motion)
- SEO meta tags

## Step 5: Review Checklist
- [ ] Matches Maycrest brand aesthetic
- [ ] Dark mode looks premium, not muddy
- [ ] Clear visual hierarchy
- [ ] Single clear CTA
- [ ] Mobile-first responsive
- [ ] Accessible (WCAG AA)
- [ ] Performance optimized (lazy loading, optimized images)
- [ ] Looks nothing like a generic MSP site

Present the design specification and code together.
