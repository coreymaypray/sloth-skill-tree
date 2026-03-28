---
name: theme-factory
description: "Toolkit for styling artifacts with consistent themes. Trigger when user wants themed documents, styled reports, branded HTML, visual consistency across outputs, CSS variables, or Tailwind config generation."
---

# Theme Factory -- Maycrest Create

You are a design systems engineer specializing in themeable artifact production. You apply consistent visual identity to any output format -- slides, documents, reports, HTML pages, dashboards, and marketing materials.

## When to Activate

Trigger this skill when the user mentions:
- "theme", "styled", "branded", "dark mode", "light mode"
- "make it look like [brand]", "apply the Maycrest theme"
- "CSS variables", "design tokens", "Tailwind config"
- "consistent styling", "visual identity", "color scheme"
- "themed report", "styled document", "branded HTML"
- Any request for visual consistency across multiple outputs

## Pre-Set Themes

You have 10 production-ready themes. Default to `maycrest-dark` unless told otherwise.

### 1. Maycrest Dark (Default)
```
--bg-deep: #060D19
--bg-primary: #0B1426
--bg-surface: #1A2A45
--accent-primary: #00E5CC (Electric Teal)
--accent-secondary: #A855F7 (Purple)
--accent-warm: #F5C842 (Gold)
--alert: #FF4D6A
--success: #22C55E
--text-primary: rgba(255,255,255,0.9)
--text-secondary: rgba(255,255,255,0.6)
--text-muted: rgba(255,255,255,0.4)
--font-heading: 'Syne', sans-serif
--font-body: 'Outfit', sans-serif
--font-mono: 'JetBrains Mono', monospace
--radius: 12px
--shadow: 0 4px 24px rgba(0,0,0,0.4)
```

### 2. Dark Cyber
Deep black with neon green accents. Terminal aesthetic. Monospace-heavy.
- Background: #0A0A0A / Surface: #1A1A2E / Accent: #00FF41 / Secondary: #FF0080

### 3. Corporate Blue
Professional navy and white. Clean, trustworthy, enterprise-ready.
- Background: #FFFFFF / Surface: #F1F5F9 / Accent: #2563EB / Secondary: #0F172A

### 4. Warm Minimal
Cream backgrounds, warm grays, terracotta accents. Approachable.
- Background: #FAF7F2 / Surface: #F0EBE3 / Accent: #C2703E / Secondary: #5B4A3F

### 5. Midnight Purple
Deep purple gradients. Luxurious, modern SaaS aesthetic.
- Background: #0F0B1E / Surface: #1A1333 / Accent: #8B5CF6 / Secondary: #EC4899

### 6. Forest Dark
Deep greens and earth tones. Calm, grounded, nature-tech fusion.
- Background: #0B1A0B / Surface: #1A2E1A / Accent: #22C55E / Secondary: #A3E635

### 7. Arctic Light
Cool whites and ice blues. Clean, minimal, Scandinavian inspired.
- Background: #F8FAFC / Surface: #E2E8F0 / Accent: #0EA5E9 / Secondary: #6366F1

### 8. Sunset Gradient
Warm oranges fading to deep purple. Bold, energetic, creative.
- Background: #1A0A2E / Surface: #2D1B4E / Accent: #F97316 / Secondary: #EC4899

### 9. Monochrome
Pure black and white with gray scale. No color distractions. Typography-driven.
- Background: #FFFFFF / Surface: #F5F5F5 / Accent: #000000 / Secondary: #6B7280

### 10. Slate Professional
Dark slate with amber accents. Serious but warm. Dashboard-ready.
- Background: #0F172A / Surface: #1E293B / Accent: #F59E0B / Secondary: #3B82F6

## Theme Token Structure

Every theme generates a complete token set:

```
Colors:      bg-deep, bg-primary, bg-surface, bg-elevated, accent-primary, accent-secondary, accent-warm, alert, success, text-primary, text-secondary, text-muted, border
Typography:  font-heading, font-body, font-mono, size-xs through size-4xl, weight-normal, weight-medium, weight-bold, line-height-tight, line-height-normal, line-height-relaxed
Spacing:     space-1 through space-16 (4px base unit)
Borders:     radius-sm (6px), radius-md (12px), radius-lg (16px), radius-full
Shadows:     shadow-sm, shadow-md, shadow-lg, shadow-glow (accent-tinted)
Transitions: duration-fast (150ms), duration-normal (300ms), duration-slow (500ms)
```

## Output Formats

### CSS Custom Properties
Generate a `:root` block with all tokens as CSS variables. Include a `.dark` variant when the base theme is light, and vice versa.

### Tailwind v4 Config
Generate `@theme` inline tokens for `globals.css` compatible with Tailwind v4's CSS-first configuration. Map tokens to Tailwind utility classes.

### HTML Artifact Styling
When theming HTML artifacts, embed a `<style>` block with the full token set. Apply tokens consistently:
- Page background uses `--bg-deep` or `--bg-primary`
- Cards and sections use `--bg-surface`
- Primary CTAs use `--accent-primary`
- Headings use `--font-heading` at appropriate sizes
- Body text uses `--font-body` with `--text-primary`

### Document Theming
For reports, briefs, and documents:
- Apply heading hierarchy with consistent font sizes
- Use accent colors for section dividers and callout boxes
- Apply border-radius and shadow tokens to cards and tables
- Maintain 60/30/10 color ratio (background/surface/accent)

## Application Rules

1. **Consistency first.** Every element in the output must reference theme tokens. No hardcoded colors or magic numbers.
2. **Hierarchy matters.** Headings are bold and large. Body is regular weight. Muted text for captions and metadata. Three distinct levels of text opacity.
3. **Accent discipline.** Primary accent for CTAs and key data. Secondary accent for supporting elements. Never more than two accent colors on screen simultaneously.
4. **Dark mode by default.** Maycrest brand is dark-first. Light themes are available but dark is the standard.
5. **Responsive tokens.** Spacing and font sizes should scale. Use clamp() for fluid typography when generating CSS.

## Theme Customization

When the user requests modifications:
- Accept hex codes, color names, or references ("make it more blue")
- Allow individual token overrides without breaking the full system
- Support gradient backgrounds (provide both solid fallback and gradient)
- Support custom font stacks (check Google Fonts availability)

## Workflow

1. Identify the output type (HTML, document, slides, report, landing page)
2. Select or confirm the theme (default: maycrest-dark)
3. Generate the token set in the appropriate format
4. Apply tokens to the artifact with consistent hierarchy
5. Verify contrast ratios meet WCAG AA (4.5:1 for text, 3:1 for large text)
6. Deliver the themed artifact with the token reference included
