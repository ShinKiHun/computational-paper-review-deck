# PROMPT_TEMPLATE.md

Paste this to Claude Code or Codex to create or refactor a deck for a new paper.
(Both agents also auto-read `AGENTS.md` / `CLAUDE.md` in this repo — this prompt just kicks it off.)

```text
I am making an HTML journal-club deck for a computational science paper.

Read, in order:
- AGENTS.md   (the behavior contract — follow it exactly)
- DESIGN.md   (visual system + the component library you must reuse)
- REVIEW_FRAMEWORK.md
- CONTENT.md  (the paper's narrative; if missing, use CONTENT_TEMPLATE.md)
- assets/     (available figures)
- index.html  (the GOLD reference deck — copy its structure and CSS, do not reinvent them)

Task:
Regenerate index.html into a polished academic slide deck for THIS paper by pouring the
CONTENT.md narrative into the reference deck's existing components.

This is a research presentation for DFT / AIMD / MD / MLIP / computational materials papers —
not a website, landing page, dashboard, blog, or SaaS UI.

Hard requirements:
1. Reuse index.html's component system verbatim (see DESIGN.md §4). Do not rewrite the CSS.
2. One full-viewport <section class="slide" id="sN"> per section; the nav JS adapts automatically.
3. Claim-style titles only — reading the titles in order must tell the whole story.
4. Max 3 cues / ~45 Korean words per slide; Korean explanation, English technical terms preserved.
5. One dominant figure per content slide; alternate figure side (layout-split-l ↔ layout-split-r).
6. Captions say why the figure matters / how to read it. Never crop or stretch figures.
7. Preserve existing image paths. Do not invent figures or claims; missing figure → labeled placeholder.
8. Keep the native scroll-snap navigation intact: wheel/trackpad snaps between slides, plus
   keyboard (↑/↓/←/→, Space, Home/End), a fixed slide counter, and a progress rail. (DESIGN.md §8)
9. No external fonts/scripts/network — must open offline from the file. Keep the @media print pages.

Before editing: summarize the narrative structure you inferred from CONTENT.md.

After editing: open/verify the deck and run the DESIGN.md §9 pre-flight checklist, then report:
- what changed
- how DESIGN.md was applied
- how CONTENT.md became slides
- any missing figures or remaining limitations
```
