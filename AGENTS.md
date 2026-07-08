# AGENTS.md — Computational Paper Review Deck

**This is the single source of truth for agent behavior in this repo.**
It is written for Codex, Claude Code, and any other coding agent.
(`CLAUDE.md` just points here so both agents follow the same rules.)

Your job: turn one computational-science paper into a **polished HTML slide deck**
for a journal club — the same quality and style as the reference `index.html`.

The output is an academic **presentation deck**. It is NOT a website, article,
dashboard, landing page, or SaaS UI.

---

## Target fields

DFT · AIMD · MD · MLIP · computational catalysis · batteries & electrochemistry ·
surfaces & interfaces · defects · phase stability · materials informatics.

## What "good" means here

The reference `index.html` (Zhang 2025 ORR review) is the quality bar. A good deck:

- reads as a claim-driven argument — reading only the titles tells the story
- is figure-first, with one dominant visual per content slide
- uses Korean explanation with standard English technical terms preserved
- looks like a warm, restrained academic seminar deck (see `DESIGN.md`)
- **works**: mouse-wheel/trackpad scroll snaps between slides; keyboard + rail + counter all navigate; images load; opens offline

---

## Files to read before you build (in order)

1. `DESIGN.md` — the visual + layout system and the **component library** you must reuse.
2. `REVIEW_FRAMEWORK.md` — how to critique a computational paper (DFT/MLIP/AIMD checklists).
3. `CONTENT.md` — the paper's narrative (if missing, read `CONTENT_TEMPLATE.md` and ask the user to fill it, or draft it from the PDF and confirm).
4. `assets/` — the available figures. List them and map each to a slide.
5. `index.html` — the gold reference. **Copy its structure and CSS; do not reinvent them.**

Then briefly summarize the narrative structure you inferred before editing.

## Build rules

1. Reuse the `index.html` component system verbatim (classes: `.slide`, `.slide__inner`,
   `.head`/`.label`/`.title`, `.body` + `.layout-*`, `.figure`/`.caption`,
   `.evidence`/`.cue`, `.bridge`/`.site`, `.compare`, `.takeaways`). See `DESIGN.md §4`.
2. One full-viewport slide per section, `<section class="slide" id="sN">`. The nav JS
   auto-adapts to the number of slides — you only write well-formed sections.
3. **Claim-style titles only.** The title is a sentence asserting the point, never a topic label.
4. Max 3 cues / ~45 Korean words per slide (captions excluded). No dense text.
5. One dominant figure per content slide; **alternate figure side** (`layout-split-l` ↔ `layout-split-r`).
6. Captions explain *why the figure matters / how to read it*, not what it literally is.
7. Preserve existing image paths. `object-fit: contain` — never crop or stretch figures.
8. Keep everything local — **no external fonts, scripts, or network requests.**
9. Keep the navigation contract intact (`DESIGN.md §8`): native scroll-snap for the wheel,
   keyboard nav, fixed counter + progress rail, print stylesheet. Do NOT replace scroll-snap
   with a custom wheel-hijack handler.
10. Content must be visible even if JS/IntersectionObserver fails (no content hidden behind a JS-only class).

## Scientific integrity (non-negotiable)

- Do not invent scientific claims, data, or figures.
- Do not overclaim beyond the paper; do not turn uncertainty into certainty.
- Keep these four separate on the slides: computational claim · experimental/benchmark
  validation · limitation · discussion question.
- If a needed figure is missing, say so and use a labeled placeholder panel — never fabricate one.

## Standard slide flow (default 10)

Title/Thesis · Scientific Problem · Conventional Understanding · New Idea/Hypothesis ·
Computational Setup · Main Result · Mechanism/Interpretation · Validation/Benchmark ·
Limitations/Assumptions · Discussion/Take-home. Deviate only if the paper's argument requires it.

## Strict UI prohibitions

No sticky navbars, scroll progress bars, signup/product buttons, pricing cards, dashboard
widgets, web-app sidebars, landing hero sections, decorative gradients, dense tables, or long
scrolling article sections. This is a seminar deck; each section fits one screen.

---

## Pipeline for a new paper

```bash
# 1. add the PDF
papers/<name>.pdf

# 2. extract embedded figures into assets/
python scripts/extract_figures.py papers/<name>.pdf --out assets

# 3. create CONTENT.md from the template and fill it (or draft from the PDF, then confirm)
python scripts/create_project.py

# 4. generate index.html by reusing the reference deck's components (this file + DESIGN.md + CONTENT.md)

# 5. verify (below), then open index.html in a browser
```

## Verify before you say it's done (do not skip)

Actually open the result and check — do not just assert it works. If a headless browser is
available, screenshot it; otherwise reason through each item:

- open `index.html`: no broken images, fonts render, layout is not overflowing
- wheel/trackpad scroll snaps one slide at a time; ↑/↓/←/→, Space, Home/End navigate; rail dots jump
- counter shows the right total; rail has one dot per slide
- run the `DESIGN.md §9` pre-flight checklist
- report: what changed · how DESIGN.md was applied · how CONTENT.md became slides · any missing figures/limitations

Note on headless screenshots: this deck uses scroll-snap, so deep-linking to `#sN` in headless
Chrome may capture a blank frame (a capture artifact, not a real bug). To screenshot a specific
slide, reorder it to the top in a throwaway copy, or just verify slide 1 + reason about the rest.
