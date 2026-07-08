# PROMPT_TEMPLATE.md

Paste this into Codex when you want to create or refactor a deck for a new paper.

```text
I am making an HTML presentation deck for a computational science journal club.

Read:
- AGENTS.md
- DESIGN.md
- REVIEW_FRAMEWORK.md
- CONTENT.md
- assets/
- index.html if it exists

Task:
Create or refactor index.html into a polished academic HTML slide deck.

Important:
This is not a website, landing page, dashboard, blog article, or SaaS UI.
This is a research presentation for DFT / AIMD / MD / MLIP / computational materials science papers.

Use DESIGN.md for:
- colors
- typography
- spacing
- visual mood

Use CONTENT.md for:
- scientific narrative
- slide order
- slide messages
- figure choices
- presenter notes

Use REVIEW_FRAMEWORK.md for:
- computational science critique
- DFT / MLIP / AIMD / MD review questions
- validation and limitation framing

Strict requirements:
1. One full-screen 16:9 slide per section.
2. Each slide must have one main scientific message.
3. Use claim-style slide titles.
4. Keep figures large and central.
5. Maximum 3 bullets per slide.
6. Maximum 45 Korean words per slide, excluding captions.
7. Use Korean explanation with English technical terms where natural.
8. Do not invent scientific claims.
9. Do not invent missing figures.
10. Preserve existing image paths.
11. Include keyboard navigation with left/right arrows.
12. Make index.html runnable locally by opening the file.
13. Avoid sticky navigation, progress bars, signup buttons, product cards, web-app components, dashboard widgets, and long scrolling article sections.

Recommended slide flow:
- Title / thesis
- Scientific problem
- Conventional understanding
- New idea / hypothesis
- Computational setup
- Main result
- Mechanism / interpretation
- Validation / benchmark
- Limitations / assumptions
- Discussion / take-home

Before editing:
Briefly summarize the likely narrative structure from CONTENT.md.

After editing:
Report:
- what changed
- how DESIGN.md was applied
- how CONTENT.md was translated into slides
- any missing figures or remaining limitations
```
