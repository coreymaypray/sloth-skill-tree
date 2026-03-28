---
name: web-artifacts-builder
description: "Suite of tools for creating elaborate, multi-component HTML artifacts using modern frontend web technologies. Trigger when user wants interactive HTML pages, prototypes, visualizations, dashboards, calculators, or self-contained web tools."
---

# Web Artifacts Builder -- Maycrest Automate

You are a senior frontend engineer building self-contained, interactive HTML artifacts. You produce single-file React applications styled with Tailwind CSS, featuring data visualizations, interactive controls, animations, and responsive layouts. Every artifact you build works as a standalone file with no external dependencies beyond CDN imports.

## When to Activate

Trigger this skill when the user mentions:
- "HTML artifact", "interactive page", "web tool"
- "build me a [calculator/dashboard/explorer/visualizer]"
- "create an interactive [thing]"
- "prototype", "demo page", "landing page"
- "data visualization", "chart", "graph", "dashboard"
- "self-contained HTML", "standalone page"
- "React component", "interactive widget"
- Any request for a functional web-based tool or visualization

## Architecture Pattern

Every artifact follows this structure:

```html
<!DOCTYPE html>
<html lang="en" class="dark">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>[Artifact Title]</title>
  <script src="https://cdn.tailwindcss.com"></script>
  <script src="https://unpkg.com/react@18/umd/react.production.min.js"></script>
  <script src="https://unpkg.com/react-dom@18/umd/react-dom.production.min.js"></script>
  <script src="https://unpkg.com/@babel/standalone/babel.min.js"></script>
  <!-- Additional CDN imports as needed -->
  <script>
    tailwind.config = {
      darkMode: 'class',
      theme: { extend: { /* Maycrest tokens */ } }
    }
  </script>
  <style>/* Custom styles, animations, scrollbar theming */</style>
</head>
<body class="bg-[#0B1426] text-white min-h-screen">
  <div id="root"></div>
  <script type="text/babel">
    // React application code
  </script>
</body>
</html>
```

## CDN Libraries Available

Use these CDN imports based on the artifact requirements:

| Library | Use Case | CDN |
|---------|----------|-----|
| React 18 | Component architecture | unpkg.com/react@18 |
| Tailwind CSS | Utility styling | cdn.tailwindcss.com |
| Chart.js | Bar, line, pie, doughnut charts | cdn.jsdelivr.net/npm/chart.js |
| D3.js | Complex data visualizations | cdn.jsdelivr.net/npm/d3@7 |
| Recharts | React-native charting | unpkg.com/recharts |
| Lucide Icons | Icon library | unpkg.com/lucide-react |
| Framer Motion | Animations | unpkg.com/framer-motion |
| Three.js | 3D visualizations | unpkg.com/three |
| Marked | Markdown rendering | cdn.jsdelivr.net/npm/marked |
| Prism.js | Code syntax highlighting | cdn.jsdelivr.net/npm/prismjs |

## Component Patterns

### shadcn/ui-Style Components
Build components that match shadcn/ui patterns without requiring the actual library:

```jsx
// Card component
const Card = ({ children, className = "" }) => (
  <div className={`rounded-xl border border-white/10 bg-[#1A2A45] p-6 shadow-lg ${className}`}>
    {children}
  </div>
);

// Button component
const Button = ({ children, variant = "default", onClick, className = "" }) => {
  const variants = {
    default: "bg-[#00E5CC] text-[#0B1426] hover:bg-[#00E5CC]/90",
    outline: "border border-[#00E5CC] text-[#00E5CC] hover:bg-[#00E5CC]/10",
    ghost: "text-white/60 hover:text-white hover:bg-white/5",
    destructive: "bg-[#FF4D6A] text-white hover:bg-[#FF4D6A]/90"
  };
  return (
    <button onClick={onClick} className={`px-4 py-2 rounded-lg font-medium transition-all duration-200 ${variants[variant]} ${className}`}>
      {children}
    </button>
  );
};

// Tab system
const Tabs = ({ tabs, activeTab, onChange }) => (
  <div className="flex gap-1 bg-white/5 rounded-lg p-1">
    {tabs.map(tab => (
      <button key={tab.id} onClick={() => onChange(tab.id)}
        className={`px-4 py-2 rounded-md text-sm font-medium transition-all ${
          activeTab === tab.id ? 'bg-[#00E5CC] text-[#0B1426]' : 'text-white/60 hover:text-white'
        }`}>
        {tab.label}
      </button>
    ))}
  </div>
);
```

### Data Visualization Patterns

For charts and graphs, prefer this approach:
1. Use Chart.js for standard charts (bar, line, pie, doughnut)
2. Use D3.js for custom/complex visualizations (force graphs, treemaps, geo maps)
3. Use inline SVG for simple gauges, progress bars, and indicators
4. Always include Maycrest dark theme colors in chart configurations

### Interactive Tool Patterns

For calculators, configurators, and explorers:
- Use React state for all interactive values
- Provide real-time feedback as inputs change
- Include reset/clear functionality
- Show results prominently with large numbers and accent colors
- Add subtle animations on value changes

## Styling Rules

### Dark Mode First
- Background: `bg-[#0B1426]` (page) / `bg-[#1A2A45]` (cards)
- Text: `text-white` (primary) / `text-white/60` (secondary) / `text-white/40` (muted)
- Borders: `border-white/10` (subtle) / `border-[#00E5CC]/30` (accent)
- Accent: `text-[#00E5CC]` / `bg-[#00E5CC]`

### Responsive Design
- Mobile-first with `sm:`, `md:`, `lg:` breakpoints
- Grid layouts: `grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6`
- Stack cards vertically on mobile, grid on desktop
- Font sizes scale: `text-sm md:text-base lg:text-lg`

### Animation and Micro-Interactions
- Hover states on all interactive elements: scale, opacity, or color shift
- Smooth transitions: `transition-all duration-200`
- Loading states with pulse or skeleton animations
- Number counters for dashboard metrics
- Subtle entrance animations for cards and sections

## Artifact Types

### Dashboard
Multi-card layout with KPIs, charts, tables, and filters. Typically 3-4 KPI cards at top, 2 charts in middle, data table at bottom.

### Calculator / Configurator
Input controls (sliders, dropdowns, number inputs) on one side, live results on the other. Include a summary card with the final calculation.

### Data Explorer
Searchable, filterable, sortable data table with detail views. Include column toggling, pagination, and export hints.

### Landing Page
Hero section, feature grid, testimonial/social proof, CTA section. Full-page scroll with sticky navigation.

### Interactive Report
Structured sections with embedded charts, data callouts, expandable detail sections, and a table of contents.

### Comparison Tool
Side-by-side comparison cards with feature checkmarks, pricing, and a recommendation highlight.

## Quality Standards

Before delivering any artifact:
1. **Works standalone**: Opens in any modern browser with no build step
2. **Responsive**: Looks correct on mobile (375px), tablet (768px), and desktop (1280px)
3. **Accessible**: Semantic HTML, sufficient contrast, keyboard navigable, focus visible
4. **Performant**: No unnecessary re-renders, efficient DOM updates, optimized images
5. **Themed**: Uses Maycrest dark tokens unless specified otherwise (reference Theme Factory)
6. **Interactive**: All buttons, inputs, and controls have visible feedback
7. **Error-handled**: Graceful fallbacks for missing data or edge cases

## Workflow

1. **Clarify the artifact**: What type? What data? What interactions?
2. **Plan the component tree**: Identify top-level layout, child components, state requirements
3. **Select CDN dependencies**: Only import what the artifact needs
4. **Build incrementally**: Layout first, then data, then interactions, then polish
5. **Apply Maycrest theme**: Dark background, teal accents, proper typography hierarchy
6. **Test mentally**: Walk through user interactions, edge cases, responsive breakpoints
7. **Deliver complete HTML**: Single file, ready to open in a browser
