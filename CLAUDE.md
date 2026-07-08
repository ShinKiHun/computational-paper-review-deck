# CLAUDE.md

This repo turns a computational-science paper into a polished HTML journal-club slide deck.

**Follow [`AGENTS.md`](AGENTS.md) exactly** — it is the single source of truth for how to build
a deck (same rules for Claude Code and Codex). Before generating or editing `index.html`, read,
in order: `AGENTS.md` → `DESIGN.md` → `REVIEW_FRAMEWORK.md` → `CONTENT.md` → the files in `assets/`.

Key reminders:

- The gold reference is `index.html`. **Reuse its components and CSS; do not reinvent them.** The
  component library and every layout class are documented in `DESIGN.md §4`.
- Titles are claims, not topic labels. One dominant figure per content slide, sides alternating.
- Keep the native scroll-snap navigation intact (wheel + keyboard + rail + counter). See `DESIGN.md §8`.
- No external fonts/scripts/network — the deck must open offline from the file.
- Never invent figures or claims. Missing figure → labeled placeholder.
- **Verify before finishing**: open the deck (screenshot with headless Chrome if possible) and run
  the `DESIGN.md §9` pre-flight checklist. See the headless scroll-snap caveat in `AGENTS.md`.
