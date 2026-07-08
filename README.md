# Computational Paper Review Deck

Reusable GitHub template for making HTML presentation decks for computational science paper reviews.

This repository is for journal-club style academic presentations, not websites, landing pages, dashboards, or SaaS UI. It is designed for DFT, AIMD, MD, MLIP, computational catalysis, batteries, surfaces, defects, phase stability, and materials informatics papers.

The intended output is a local `index.html` slide deck with:

- Korean explanations with standard English technical terms preserved
- large paper figures
- claim-style slide titles
- a consistent warm academic visual style
- a reusable scientific review structure

## Repo Structure

```text
computational-paper-review-deck/
  README.md
  AGENTS.md
  DESIGN.md
  CONTENT_TEMPLATE.md
  REVIEW_FRAMEWORK.md
  PROMPT_TEMPLATE.md
  index.html
  scripts/
    extract_figures.py
    create_project.py
  assets/
    .gitkeep
  papers/
    .gitkeep
  examples/
    .gitkeep
```

## Workflow For A New Paper

1. Put the paper PDF in `papers/`.
2. Run the figure extraction script:

```bash
python scripts/extract_figures.py papers/example.pdf --out assets
```

3. Create a paper-specific `CONTENT.md`:

```bash
python scripts/create_project.py
```

4. Fill `CONTENT.md` using the paper's scientific story:

- What problem is unresolved?
- What old model or descriptor is incomplete?
- What new hypothesis, method, or mechanism is proposed?
- What computation supports the claim?
- What validates it?
- What assumptions or limitations matter?

5. Ask Codex to generate or refactor `index.html` using:

- `AGENTS.md`
- `DESIGN.md`
- `REVIEW_FRAMEWORK.md`
- `CONTENT.md`
- `assets/`

The paste-ready prompt is in `PROMPT_TEMPLATE.md`.

6. Open `index.html` locally in a browser.

## Figure Extraction

The script extracts embedded bitmap images from the PDF into `assets/`.

```bash
python scripts/extract_figures.py papers/my_paper.pdf --out assets
```

Optional filters:

```bash
python scripts/extract_figures.py papers/my_paper.pdf --out assets --min-width 180 --min-height 120 --min-area 40000
```

The script does not use OCR, does not require internet, and does not extract text. It only extracts embedded images. If a publisher PDF stores figures as vector graphics, use screenshots or manual export for those figures.

## How To Use This Like A Skill

Keep this repository on GitHub. For each new paper:

1. Clone or copy this repo.
2. Add the PDF to `papers/`.
3. Extract figures into `assets/`.
4. Fill `CONTENT.md`.
5. Paste `PROMPT_TEMPLATE.md` into Codex.

`AGENTS.md` is the main behavior guide for Codex. It tells Codex what kind of deck to make, what to avoid, and how to structure computational science reviews.

## What To Customize First

- `CONTENT.md`: paper-specific scientific story
- `assets/`: extracted or manually selected figures
- `DESIGN.md`: visual style only if you want to change the look
- `REVIEW_FRAMEWORK.md`: lab-specific review criteria

Keep `AGENTS.md` strict. That file prevents Codex from turning the deck into a generic website.
