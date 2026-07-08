# AGENTS.md - Computational Paper Review Deck Instructions

This repository creates HTML slide decks for computational science paper reviews.

The final output is an academic presentation deck, not a website, article, dashboard, landing page, or SaaS UI.

## Target Fields

Use this repo for papers involving:

- DFT
- AIMD
- MD
- MLIP
- computational catalysis
- batteries and electrochemistry
- surfaces and interfaces
- defects
- phase stability
- materials informatics

## Output Rules

The final `index.html` must:

- be a full-screen 16:9 slide deck
- be runnable locally by opening the file
- use plain HTML/CSS/JS unless the user explicitly asks otherwise
- use Korean explanation with English technical terms where natural
- use large, central figures
- preserve existing image paths
- include keyboard navigation with left/right arrows
- include a visible slide counter
- avoid broken image paths

## Presentation Rules

Every slide should have:

- a short section label
- a claim-style title
- one main visual or figure
- maximum 3 bullets
- optional short caption

Use claim-style titles, not topic labels.

Good:

- "Bridge O* changes the scaling relation."
- "The active site is an M-N ensemble."
- "The MLIP is accurate only inside the sampled configuration space."

Bad:

- "DFT Results"
- "Figure 3"
- "Method"
- "Discussion"

## Scientific Integrity Rules

Do not invent scientific claims.
Do not invent missing figures.
Do not overclaim beyond the paper.
Do not hide major assumptions.
Do not convert uncertainty into certainty.

Separate these clearly:

- computational claim
- experimental or benchmark validation
- limitation
- discussion question

If a requested figure is missing, state it and use a placeholder panel instead of inventing a figure.

## Strict UI Prohibitions

Do not use:

- sticky navigation
- progress bars
- product buttons
- signup sections
- dashboards
- pricing cards
- web-app sidebars
- landing-page hero sections
- decorative gradient blobs
- dense tables
- long scrolling article sections

This is a slide deck. Each section should fit on one screen.

## Standard Slide Flow

Use this order unless the paper clearly needs a different structure:

1. Title / thesis
2. Scientific problem
3. Conventional understanding
4. New idea / hypothesis
5. Computational setup
6. Main result
7. Mechanism / interpretation
8. Validation / benchmark
9. Limitations / assumptions
10. Discussion / take-home

## Workflow For Codex

Before editing:

1. Read `DESIGN.md`.
2. Read `REVIEW_FRAMEWORK.md`.
3. Read `CONTENT.md` if it exists. Otherwise read `CONTENT_TEMPLATE.md`.
4. Inspect `assets/` and identify available figures.
5. Summarize the narrative structure briefly.

When editing `index.html`:

1. Build one full-screen 16:9 slide per section.
2. Make figures large and central.
3. Keep text sparse and projector-readable.
4. Use Korean explanations with English technical terms.
5. Keep all CSS and JS local unless the user asks otherwise.

After editing:

1. Check image paths.
2. Check slide count.
3. Check that the deck does not look like a website.
4. Explain what changed and what remains missing.
