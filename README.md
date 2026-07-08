# Computational Paper Review Deck

A reusable GitHub template + agent skill for turning **one computational-science paper into a
polished HTML slide deck** for journal club. Works with **Claude Code or Codex** (or any coding agent).

For DFT, AIMD, MD, MLIP, computational catalysis, batteries, surfaces, defects, phase stability,
and materials informatics — not websites, dashboards, or SaaS UI.

The output is a single `index.html` that:

- is a **scroll-snap deck** — mouse wheel / trackpad scrolls up/down and snaps one slide at a time,
  plus keyboard nav (↑/↓/←/→, Space, Home/End), a progress rail, and a slide counter
- is figure-first with claim-style titles and Korean text (English technical terms preserved)
- uses a warm, restrained academic style (Anthropic-inspired), fully responsive via `clamp()`
- opens offline from the file and prints to clean 16:9 PDF pages

The shipped `index.html` is a **worked reference** (Zhang et al., JACS 2025, ORR single-atom
catalysts). Use it as the quality bar and regenerate it for your own paper.

## How the agent knows what to do

- `AGENTS.md` — the single behavior contract (Codex + any agent read this).
- `CLAUDE.md` — points Claude Code to `AGENTS.md` so both agents follow identical rules.
- `DESIGN.md` — the visual system **and the reusable component library** (§4) the agent must reuse.
- `REVIEW_FRAMEWORK.md` — how to critique a computational paper (DFT/MLIP/AIMD checklists).
- `PROMPT_TEMPLATE.md` — the paste-ready kickoff prompt.

## Repo structure

```text
computational-paper-review-deck/
  index.html            # gold reference deck — reuse its components & CSS
  AGENTS.md             # behavior contract (single source of truth)
  CLAUDE.md             # Claude Code pointer -> AGENTS.md
  DESIGN.md             # design system + component library + rules + checklist
  REVIEW_FRAMEWORK.md   # computational-science critique checklist
  CONTENT_TEMPLATE.md   # per-paper narrative template -> copy to CONTENT.md
  PROMPT_TEMPLATE.md    # paste-ready prompt
  scripts/
    extract_figures.py  # pull embedded figures out of a PDF into assets/
    create_project.py   # scaffold CONTENT.md
  assets/               # figures for the current deck
  papers/               # source PDFs
  examples/             # frozen example decks
```

## Workflow for a new paper

```bash
# 1. add the PDF
cp mypaper.pdf papers/

# 2. extract embedded figures
python scripts/extract_figures.py papers/mypaper.pdf --out assets

# 3. scaffold and fill the narrative
python scripts/create_project.py            # creates CONTENT.md
#    ...fill CONTENT.md (claim per slide, which figure, why it matters)

# 4. let the agent build the deck
#    Claude Code / Codex: paste PROMPT_TEMPLATE.md (it reads AGENTS.md + DESIGN.md + CONTENT.md)

# 5. open index.html in a browser and check the DESIGN.md §9 pre-flight checklist
```

## Using it like a skill

Keep this repo on GitHub. For each new paper, clone/copy it, drop the PDF in `papers/`, extract
figures, fill `CONTENT.md`, and paste `PROMPT_TEMPLATE.md`. The agent reuses the reference deck's
components, so every deck comes out in the same high-quality, consistent style.

## Figure extraction

`scripts/extract_figures.py` pulls embedded bitmap images from a PDF into `assets/` — no OCR, no
internet, no text extraction. Vector-only figures won't extract; screenshot or export those manually.

```bash
python scripts/extract_figures.py papers/mypaper.pdf --out assets \
  --min-width 180 --min-height 120 --min-area 40000
```
