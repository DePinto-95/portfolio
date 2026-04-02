# Sotiri De Pinto — Personal Portfolio

Plain HTML / CSS / JavaScript portfolio. No frameworks, no build tools.

---

## File structure

```
Website/
├── index.html                      # Homepage
├── css/
│   └── style.css                   # All shared styles (CSS custom properties, components)
├── js/
│   ├── main.js                     # Hamburger nav + scroll fade-in (loaded on all pages)
│   └── band.js                     # Song player logic (loaded only on band.html)
├── pages/
│   ├── band.html                   # Irene's Circus band page
│   └── project-minesweeper.html    # Minesweeper Solver project page
├── assets/                         # Images and static files
│   └── .gitkeep
├── CLAUDE.md
└── README.md
```

---

## Placeholder table

Every placeholder has an HTML comment next to it in the source. Here's a quick reference:

| Placeholder | File | What to replace |
|---|---|---|
| Email address | `index.html` → `#contact` | `href="mailto:your.email@example.com"` |
| LinkedIn URL | `index.html` → `#contact` | `href="https://linkedin.com/in/your-username"` |
| Avatar photo | `index.html` → `#hero` | Replace the initials `div` with `<img>` inside `.avatar` |
| Minesweeper GitHub repo | `pages/project-minesweeper.html` | Both GitHub repo `href="#"` buttons |
| Minesweeper thesis PDF | `pages/project-minesweeper.html` | Both thesis PDF `href="#"` buttons |
| Band Spotify URL | `pages/band.html` → social pills | `href="https://open.spotify.com/artist/…"` |
| Band Instagram URL | `pages/band.html` → social pills | `href="https://instagram.com/…"` |
| Band SoundCloud URL | `pages/band.html` → social pills | `href="https://soundcloud.com/…"` |
| Band YouTube URL | `pages/band.html` → social pills | `href="https://youtube.com/@…"` |
| Band Bandcamp URL | `pages/band.html` → social pills | `href="https://….bandcamp.com"` |
| Song 1 embed URL | `pages/band.html` → `.song-row` | `data-embed="https://open.spotify.com/embed/track/…"` |
| Song 2 embed URL | `pages/band.html` → `.song-row` | `data-embed="https://open.spotify.com/embed/track/…"` |
| Song 3 embed URL | `pages/band.html` → `.song-row` | `data-embed="https://open.spotify.com/embed/track/…"` |
| Band photo 1 | `pages/band.html` → `.photo-slot` | See comment in HTML |
| Band photo 2 | `pages/band.html` → `.photo-slot` | See comment in HTML |
| Band photo 3 | `pages/band.html` → `.photo-slot` | See comment in HTML |

---

## How to: add a profile photo

1. Add your photo to `assets/photo.jpg` (recommended: square, at least 400×400px).
2. In `index.html`, find the `.avatar` element in the Hero section (look for the `SD` initials).
3. Replace the text content with an `<img>` tag:

```html
<div class="avatar" style="width: 110px; height: 110px;">
  <img src="assets/photo.jpg" alt="Sotiri De Pinto" />
</div>
```

---

## How to: add band photos

1. Add your images to `assets/` (e.g. `assets/band-live-1.jpg`).
2. In `pages/band.html`, find the `.photo-grid` section.
3. Replace each `.photo-slot` div with:

```html
<div style="aspect-ratio:1; border-radius: var(--radius-md); overflow: hidden;">
  <img src="../assets/band-live-1.jpg" alt="Irene's Circus live at [venue]"
       style="width:100%; height:100%; object-fit:cover;" />
</div>
```

---

## How to: add a new project page

1. Copy `pages/project-minesweeper.html` and rename it (e.g. `pages/project-myapp.html`).
2. Update the title, meta description, badges, header text, narrative, and sidebar.
3. In `index.html`, duplicate one of the `.card` blocks inside `#projects` and update:
   - the card icon, title, description, tags
   - the `href` on the "View project" button to point to your new page
4. Remove `card--coming-soon` if it's a completed project.

---

## How to: add songs to the band page

1. Open `pages/band.html` and find the `.song-list` section.
2. Duplicate any `.song-row` div.
3. Update the track number, title, and duration.
4. Set the `data-embed` attribute to the Spotify or SoundCloud embed URL:
   - **Spotify**: track page → `…` → Share → Embed → copy the `src` value from the iframe.
   - **SoundCloud**: track page → Share → Embed → copy the `src` value.

---

## Deploy to GitHub Pages

1. Create a new public GitHub repository named `DePinto-95.github.io`
   (or any name — but `username.github.io` serves at the root URL).

2. Push the files:
   ```bash
   git remote add origin https://github.com/DePinto-95/DePinto-95.github.io.git
   git branch -M main
   git push -u origin main
   ```

3. In the GitHub repository, go to **Settings → Pages**.

4. Under **Source**, select **Deploy from a branch**, choose `main`, and leave the folder as `/ (root)`.

5. Click **Save**. Your site will be live at `https://DePinto-95.github.io` within a few minutes.

> If you used a different repo name (e.g. `portfolio`), the URL will be `https://DePinto-95.github.io/portfolio`.
> In that case, update all internal links and asset paths to include the `/portfolio` prefix,
> or use relative paths consistently (which this project already does).
