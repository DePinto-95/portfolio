# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project overview

Personal portfolio for Sotiri De Pinto. Plain HTML / CSS / JavaScript — no frameworks, no build tools, no package managers.

## Architecture

- **`css/style.css`** — single stylesheet for all pages. Uses CSS custom properties (`--color-*`, `--font-*`, `--space-*`) for theming. Edit variables at the top of the file to retheme globally.
- **`js/main.js`** — loaded on every page. Handles hamburger nav toggle and IntersectionObserver-based `.fade-in` → `.is-visible` scroll animations.
- **`js/band.js`** — loaded only on `pages/band.html`. Manages the song player (click-to-play, active row state, iframe embed loading).
- **`pages/`** — each project or topic gets its own HTML file. Page-specific styles go in a `<style>` block in the page's `<head>`; shared styles stay in `style.css`.
- **`assets/`** — images and static files. Reference from pages as `../assets/filename` or `assets/filename` from the root.

## Key conventions

- All colors, spacing, and font families are CSS custom properties — never hard-code values that already exist as variables.
- Buttons use shared classes: `.btn .btn-primary`, `.btn .btn-outline`, `.btn .btn-ghost` (for dark backgrounds), `.btn .btn-sm`.
- Scroll animations: add class `fade-in` to an element and `main.js` will add `.is-visible` when it enters the viewport. Use `fade-in-group` on a parent to stagger children.
- Every placeholder link (`href="#"`) has an HTML comment directly next to it explaining exactly what to replace it with.
- Nav and footer markup is duplicated across pages (no server-side includes) — keep them in sync manually.

## Git & GitHub workflow

**Commit and push after every meaningful change.** This project is version-controlled at `https://github.com/DePinto-95/portfolio`. Never leave significant work uncommitted.

- Use clean, descriptive commit messages: what changed and why (e.g. `"Add PermissionPruner project page"`, `"Update contact email and LinkedIn link"`).
- Push to `origin main` after each commit so there is always a recoverable remote state.
- If making multiple related small changes, group them into one logical commit rather than committing every single file save.

```bash
git add <files>
git commit -m "Short description of what changed"
git push
```
