# DESIGN.md - Anthropic-inspired Academic Presentation Style

## Purpose

This design system is for HTML-based academic presentation decks.
The deck is for a computational science journal club, not a startup landing page or SaaS website.

Use an Anthropic-inspired visual language: warm, restrained, intellectual, off-white paper surfaces, rust accents, dark ink text, generous whitespace, and calm typography.

## Core Visual Mood

- warm academic
- restrained and thoughtful
- research-seminar appropriate
- figure-first
- minimal ornament
- quiet confidence
- closer to an academic journal or seminar deck than a product website

## Color Palette

```css
:root {
  --primary: #C2522D;
  --primary-hover: #A8421F;
  --ink: #1A1A18;
  --ink-muted: #6B6B63;
  --canvas: #FAF9F7;
  --surface-1: #F2F0EC;
  --surface-2: #E8E5E0;
  --border: #D8D4CC;
  --accent-warm: #D4A574;
}
```

## Color Usage

- Use `--canvas` as the main slide background.
- Use `--ink` for main text.
- Use `--ink-muted` for captions, metadata, and secondary text.
- Use `--primary` sparingly for section labels, dividers, key terms, and emphasis.
- Use `--surface-1` and `--surface-2` for figure panels or subtle callout boxes.
- Avoid saturated blues, neon colors, harsh gradients, and colorful dashboard palettes.

## Typography

Use a clean humanist sans-serif stack:

```css
font-family: Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", "Noto Sans KR", sans-serif;
```

Rules:

- Slide titles should be large, confident, and claim-like.
- Body text should be sparse and readable from a projector.
- Korean text should use natural academic phrasing.
- English technical terms are allowed when standard in the field.
- Avoid dense paragraphs.

Recommended sizes:

- Slide title: 40-56px
- Section label: 13-15px, uppercase or small caps
- Body text: 22-28px
- Figure captions: 14-16px
- Metadata: 14-16px

## Slide Format

- One full-screen slide per section.
- Use a 16:9 layout.
- Each slide must fit in one screen.
- Avoid long scrolling pages.
- Avoid sticky navigation bars.
- Avoid web progress bars.
- Avoid landing-page hero sections.
- Avoid SaaS-style cards unless used very sparingly.
- Add keyboard navigation with left/right arrow keys.

## Layout Principles

Each slide should have:

- a short section label
- a strong claim-style title
- one main figure or visual structure
- maximum 2-3 supporting bullets
- optional short caption

Good slide titles:

- "Weak-binding activity comes from site switching."
- "The active site is an M-N ensemble, not just a metal center."
- "Bridge O* changes scaling and interface response."
- "The interface model is the soft spot."

Bad slide titles:

- "DFT Results"
- "Figure 3"
- "Background"
- "Discussion"

## Content Density

Strict rules:

- Maximum 3 bullets per slide.
- Maximum 45 Korean words per slide, excluding figure captions.
- No paragraph longer than 2 lines.
- No dense tables.
- If a table exists, convert it into 2-3 discussion cards.
- Prefer figure annotations over long text explanations.

## Figure Rules

Figures are the main content.

- Make figures large and central.
- Use subtle paper-like panels for figures.
- Do not crop scientific figures unless necessary.
- Do not invent new figures.
- Preserve existing image paths.
- Captions should explain why the figure matters, not merely describe what it is.
- If a figure is unfamiliar, introduce how to read it before interpreting it.

## Allowed Components

- section label
- claim title
- large figure panel
- two-column comparison
- three short takeaway cards
- minimal caption
- final take-home list
- small slide counter
- previous/next arrow controls

## Avoid

- product buttons
- signup forms
- web app navbars
- pricing cards
- dashboard widgets
- decorative gradients
- excessive shadows
- many rounded cards
- scroll progress bars

## Scientific Communication Rules

Every slide must answer:

"What should the audience remember?"

Separate:

- computational claim
- experimental validation
- limitation
- discussion question

Do not overclaim beyond the paper.

## Source-backed Rules

Use assertion-evidence structure:

- The slide title should be the claim, not a topic label.
- The body should provide visual evidence for that claim.
- A good deck can often be understood by reading only the titles in sequence.

Useful sources:

- Assertion-Evidence Approach: https://www.assertion-evidence.com/
- MIT/Broad Communication Lab, Slideshow: https://mitcommlab.mit.edu/broad/commkit/slideshow/
- MIT/Broad Communication Lab, Figure Design: https://mitcommlab.mit.edu/broad/commkit/figure-design/
- DesignMD Anthropic visual reference: https://www.designmd.co/d/anthropic
