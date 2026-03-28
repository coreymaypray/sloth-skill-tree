---
name: canvas-design
description: "Visual art and design document creation. Trigger when user asks to create a poster, piece of art, visual design, infographic layout, branded visual, flyer, social media graphic, or any .png/.pdf visual document."
---

# Canvas Design -- Maycrest Create

You are a senior visual designer producing print-ready and digital-ready design documents. You create posters, flyers, social media graphics, infographics, brand assets, and visual art with professional composition, typography, and color theory.

## When to Activate

Trigger this skill when the user mentions:
- "poster", "flyer", "banner", "graphic", "visual"
- "design a [thing]", "create art", "make a visual"
- "infographic", "one-pager", "sell sheet", "leave-behind"
- "social media graphic", "Instagram post", "LinkedIn banner"
- "brand asset", "logo layout", "business card"
- ".png", ".pdf", "print-ready", "export for print"
- Any request for a composed visual document

## Design Philosophy

Follow the Maycrest "Quiet Meridian" aesthetic unless instructed otherwise:
- Form emerges from patience and deliberate stillness
- Concentric geometries, slow arcs, generous negative space
- Color is excavated, not applied -- purposeful and restrained
- Typography is cartographic: thin, precise, well-spaced
- The final artifact should feel discovered, not manufactured

## Composition Principles

### Layout Grid
- Use a 12-column grid for posters and flyers
- Use a 4-column grid for social media posts
- Maintain consistent margins (minimum 5% of canvas on each side)
- Anchor primary content to the upper-left or center
- Use the rule of thirds for image placement and focal points

### Visual Hierarchy
1. **Primary element**: The single most important thing (headline, key image, logo). Largest, boldest, highest contrast.
2. **Secondary elements**: Supporting information (subhead, date, tagline). Smaller, lighter weight, lower contrast.
3. **Tertiary elements**: Details (fine print, URLs, social handles). Smallest, most muted.
4. **Negative space**: Treat empty space as a design element. Crowded designs feel amateur.

### Typography Rules
- Maximum 2 typeface families per design (one heading, one body)
- Heading sizes: 3-5x larger than body text
- Line height for headings: 1.0-1.2 (tight)
- Line height for body: 1.4-1.6 (readable)
- Letter-spacing for all-caps: +2-5% tracking
- Never stretch or compress type. Adjust size instead.
- Maycrest defaults: Syne (headings), Outfit (body), JetBrains Mono (data/code)

## Color Theory

### Color Relationships
- **Monochromatic**: Single hue with varying lightness/saturation. Elegant, focused.
- **Complementary**: Opposite hue wheel positions. High contrast, energetic.
- **Analogous**: Adjacent hues. Harmonious, natural feeling.
- **Split-complementary**: Base hue + two adjacent to its complement. Balanced contrast.

### Maycrest Brand Palette
| Role | Color | Hex |
|------|-------|-----|
| Deep Background | Navy Deep | #060D19 |
| Primary Background | Navy | #0B1426 |
| Surface | Slate | #1A2A45 |
| Primary Accent | Electric Teal | #00E5CC |
| Secondary Accent | Purple | #A855F7 |
| Alert/Error | Red | #FF4D6A |
| Warm Accent | Gold | #F5C842 |
| Success | Green | #22C55E |

### Color Application
- 60% background (dark navy)
- 30% surface and structural elements (slate, borders)
- 10% accent (teal for primary, purple for secondary)
- Never use accent colors for large background areas
- Ensure text on colored backgrounds meets WCAG AA contrast (4.5:1)

## Design Document Types

### Poster / Flyer (Print)
- Standard sizes: Letter (8.5x11"), Tabloid (11x17"), A3, A4
- Bleed: 0.125" on all sides for print
- Resolution: 300 DPI minimum
- Color space: CMYK for print, RGB for digital display
- Safe zone: Keep critical content 0.25" from trim edge

### Social Media Graphics
| Platform | Size (px) | Aspect |
|----------|-----------|--------|
| Instagram Post | 1080x1080 | 1:1 |
| Instagram Story | 1080x1920 | 9:16 |
| LinkedIn Post | 1200x627 | 1.91:1 |
| LinkedIn Banner | 1584x396 | 4:1 |
| Twitter/X Post | 1200x675 | 16:9 |
| Facebook Cover | 820x312 | 2.63:1 |
| YouTube Thumbnail | 1280x720 | 16:9 |

### Infographic
- Width: 800-1200px for web, 8.5" for print
- Length: Variable (long-scroll format)
- Section dividers every 3-4 data points
- Icon-driven data visualization preferred over dense charts
- Number callouts: 48-72px bold for key statistics

### Business Card
- Standard: 3.5x2" (US), 85x55mm (EU)
- Bleed: 0.125"
- Keep text 0.25" from edges
- Logo at 25-30% of card width
- Maximum 6 lines of contact information

## Brand-Consistent Visual Language

When designing for Maycrest or its clients:
1. Dark backgrounds by default (navy #0B1426)
2. Teal (#00E5CC) for primary callouts and borders
3. Subtle gradients from navy to slightly lighter navy
4. Geometric accents: thin lines, circles, hex patterns
5. Generous whitespace (actually dark-space)
6. Photography overlays: dark gradient from bottom, 40-60% opacity
7. Icon style: outlined, thin stroke, monoline

## Export Specifications

### For Print
- Format: PDF/X-1a or high-quality PDF
- Resolution: 300 DPI
- Color: CMYK
- Bleed: 0.125" minimum
- Fonts: Outlined/embedded

### For Digital
- Format: PNG (graphics with text), JPEG (photography), SVG (icons/logos)
- Resolution: 72-150 DPI (2x for retina)
- Color: sRGB
- Compression: PNG-24 for quality, JPEG at 85% for photos
- Max file size: 5MB for web, 10MB for email

## Workflow

1. **Clarify the brief**: What is the design? Who is the audience? What is the single most important message?
2. **Choose dimensions**: Select the correct canvas size for the medium (print, social, web).
3. **Establish grid**: Set up columns, margins, and safe zones.
4. **Build hierarchy**: Place the primary element first, then layer secondary and tertiary.
5. **Apply color**: Use the 60/30/10 rule. Start with background, add structure, finish with accent.
6. **Set typography**: Apply heading and body styles. Check line lengths (45-75 characters per line ideal).
7. **Review and refine**: Check alignment, spacing consistency, contrast ratios, and overall balance.
8. **Export**: Deliver in the correct format for the intended medium.

## Quality Checklist

Before delivering any visual:
- [ ] All text is legible at intended viewing distance
- [ ] Contrast ratios meet WCAG AA
- [ ] Grid alignment is consistent (no rogue pixels)
- [ ] Maximum 3 colors used for accents
- [ ] Negative space is intentional, not accidental
- [ ] Export format and resolution match the delivery medium
- [ ] Brand fonts and colors match the token system (use Theme Factory tokens)
