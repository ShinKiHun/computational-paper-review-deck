# DESIGN.md — Academic Presentation Design System

This is the visual + layout contract for the deck. The point of this file is to
make "reference a great presentation, then place figures and words accordingly"
into **concrete, checkable rules** — so the agent does not have to browse for
inspiration each time, and so every deck looks like it came from the same hand.

The gold reference implementation is `index.html` (the Zhang 2025 deck). It already
implements this entire system. **Do not reinvent the CSS.** Reuse the components
below and pour new content into them.

---

## 1. Visual Mood (Anthropic-inspired academic)

- warm, restrained, intellectual — a research seminar, not a SaaS landing page
- off-white paper surfaces, rust accent, dark ink text, generous whitespace
- figure-first, minimal ornament, quiet confidence
- one screen = one idea

## 2. Color Palette (locked)

```css
--primary:      #C2522D;  /* rust — section labels, key terms, dividers, emphasis. Use sparingly. */
--primary-hover:#A8421F;
--ink:          #1A1A18;  /* main text */
--ink-muted:    #6B6B63;  /* captions, metadata, secondary text */
--canvas:       #FAF9F7;  /* slide background */
--surface-1:    #F2F0EC;  /* callout / cue panels */
--surface-2:    #E8E5E0;
--border:       #D8D4CC;
--accent-warm:  #D4A574;  /* secondary accent — the "old / caution" side of a contrast */
```

Rust vs warm accent carries **meaning**: rust = the paper's new idea / the point;
warm = the old assumption, the caution, the secondary note. Keep that mapping consistent.

Avoid saturated blues, neon, harsh gradients, colorful dashboard palettes, heavy shadows.

## 3. Typography

- Stack: `Inter, ui-sans-serif, system-ui, -apple-system, "Segoe UI", "Noto Sans KR", "Malgun Gothic", sans-serif`
- **No web fonts / no external requests** — the deck must open offline from a file.
- Sizes are fluid via `clamp()` (already wired in `:root`). Do not hard-code px font sizes on new content; reuse the `--fs-*` variables and existing classes so text scales on any projector.
- Korean body text with standard English technical terms inline (DFT, O*, scaling, MLIP…). Do not translate established terms.

---

## 4. Component Library (reuse these — they are in `index.html`)

Every slide is:

```html
<section class="slide" id="sN" aria-label="...">
  <div class="slide__inner">
    <header class="head"> section label + claim title (+ optional paper-meta) </header>
    <div class="body LAYOUT"> figure(s) + evidence </div>
    <footer class="foot"> <span class="rule"></span> <span>section tag</span> </footer>
  </div>
</section>
```

**Header**
- `.label[data-step="0N"]` — small-caps section label with a numbered ring. `data-step` = slide number.
- `.title` — the claim. Modifiers: `.lg` (title slide), `.wide` (longer claims). Titles wrap via `text-wrap: balance`; keep them to ~1–2 lines.
- `.paper-meta` — top-right authors/journal/title block. Title slide only.

**Body layouts** (set on the `.body` element)
- `.layout-hero` — title slide: thesis block + hero figure, vertically centered.
- `.layout-split-l` — figure LEFT (wider) + evidence RIGHT.
- `.layout-split-r` — evidence LEFT + figure RIGHT (wider).
- `.layout-figure` — one big centered figure, no side column.
- `.layout-compare` — two `.compare` columns (old vs new).

**Figure**
- `.figure` (add `.paper` for a tinted panel) wraps `<img>` + `<figcaption class="caption">`.
- Image is `object-fit: contain` — never cropped or distorted.
- Caption explains **why the figure matters or how to read it**, not what it literally is. Lead with a bold rust cue like `<b>읽는 법:</b>` or `<b>핵심:</b>` when helpful.

**Evidence cues** (the right/left text column)
- `.evidence` wraps 2–3 `.cue` blocks. Add `.warm` to the last one for the caution/question/interpretation.
- Each `.cue` = `<b>LABEL</b><span>one sentence</span>`. The `<b>` is a 1–3 word tag (Expected / Observed / Mechanism / Caution…). Wrap a key term in `<em>` inside the span to emphasize in rust.

**Specialty blocks**
- `.bridge` + `.site.old` / `.arrow` / `.site.new` — an "old → new" transition (title slide).
- `.tags` — method chips (DFT, solvation, MLIP…).
- `.compare.old` / `.compare.new` — two-column contrast (`<h3>` + `<p>`), for the New-Idea or Conventional slides.
- `.takeaways` + `.takeaway` (`<b>label</b><span>point</span>`) — the final discussion slide.

---

## 5. Figure Placement Rules (this is where most decks fail)

1. **Every content slide has exactly one dominant visual.** If there is no figure, the slide is a contrast/takeaway slide (`.layout-compare` / `.takeaways`) — never a wall of text.
2. **The figure is the evidence for the title's claim.** Choose the figure that literally shows what the title asserts. If none does, change the title.
3. **Alternate the figure side** across consecutive slides (`split-l`, then `split-r`, then `split-l`…). This creates rhythm and stops the deck from looking like a form. The Zhang deck alternates on slides 2→3→4→5→6→7→8→9.
4. **Do not crop or stretch scientific figures.** `object-fit: contain` only. Preserve aspect ratio and existing image paths.
5. **Reuse a figure deliberately, not lazily.** The same figure may anchor the title and the take-home (as Fig 2 does in Zhang) — that is a callback, and it should be intentional.
6. **If a needed figure is missing**, say so and leave a `.figure.paper` placeholder panel with a caption stating what belongs there. Never invent a figure.

## 6. Word Placement Rules

1. **Assertion–evidence, always.** The title is a full-sentence claim, not a topic label. A reader who reads only the titles in order should get the whole argument.
   - Good: "Bridge O* makes the N ligand part of the active ensemble."
   - Bad: "Results", "Figure 3", "Method", "Discussion".
2. **≤ 3 cues per slide, one sentence each.** Max ~45 Korean words on a slide (captions excluded). No paragraph longer than 2 lines.
3. **Label → sentence.** Every cue leads with a 1–3 word tag so the eye can scan the structure before reading.
4. **Separate the four registers** and never blur them: computational claim · experimental/benchmark validation · limitation · discussion question. The `.warm` cue is usually the caution/limitation/question.
5. **Emphasis is rare.** One `<em>` (rust) per slide at most. If everything is emphasized, nothing is.
6. **Captions do work.** They say why the figure matters or how to read an unfamiliar plot — they are not decoration.

## 7. Slide Flow (default 10)

Title/Thesis · Scientific Problem · Conventional Understanding · New Idea/Hypothesis ·
Computational Setup · Main Result · Mechanism/Interpretation · Validation/Benchmark ·
Limitations/Assumptions · Discussion/Take-home.

Deviate only when the paper's argument genuinely needs it — then keep the assertion-evidence spine.

---

## 8. Navigation Contract (must keep — this is what Codex kept breaking)

The deck is a **native scroll-snap** deck. Keep all of this working:

- `html { scroll-snap-type: y mandatory; scroll-behavior: smooth; }`
- `.slide { min-height: 100vh; scroll-snap-align: start; scroll-snap-stop: always; }`
- **Mouse wheel / trackpad**: vertical scroll moves between slides and snaps (this is native — do not intercept the wheel with custom JS; scroll-snap handles it).
- **Keyboard**: ↑/↓, ←/→, PageUp/Down, Space, Home, End all navigate (JS `goTo`).
- **Prev/next buttons** + **progress rail** (one dot per slide) + **slide counter**, all `position: fixed`, driven by an `IntersectionObserver`.
- Content is **always visible by default**; the entrance animation only *adds* motion to the active slide. Never hide slide content behind a class that JS must add — if the observer fails, the slide must still show.
- `@media print` turns each slide into one page for PDF export.

If you add slides, the JS auto-adapts (it reads `.slide` count and builds the rail) — you only need well-formed `<section class="slide" id="sN">` blocks.

## 9. Pre-flight Checklist (run before declaring done)

- [ ] Every `<img>` path resolves to a file in `assets/` (open the deck; no broken images).
- [ ] Slide count matches the counter; the rail has one dot per slide.
- [ ] Wheel scroll snaps one slide at a time; arrows + rail dots jump correctly.
- [ ] Every title is a claim sentence; reading titles top-to-bottom tells the story.
- [ ] No slide exceeds 3 cues / ~45 Korean words.
- [ ] Figure sides alternate; no figure is cropped or stretched.
- [ ] Opens offline (no external fonts/scripts/network requests).
- [ ] Prints to clean 16:9 pages (Ctrl/Cmd-P preview).

## 10. Hard "Avoid" List

Sticky navbars · scroll progress bars · signup/product buttons · pricing cards ·
dashboard widgets · web-app sidebars · landing hero sections · decorative gradient blobs ·
dense tables (convert to 2–3 cards) · long scrolling article text · many rounded cards ·
external web fonts · anything that makes it read as a website instead of a seminar deck.
