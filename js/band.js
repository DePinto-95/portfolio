/* ============================================================
   band.js — loaded only on pages/band.html
   Handles the song player:
   - Click row  → mark active, load embed URL into iframe
   - Click again → deactivate, clear iframe
   - Click different row → deactivate previous, activate new
   ============================================================ */

(function () {
  const rows = document.querySelectorAll('.song-row');
  const player = document.getElementById('song-player');

  if (!rows.length || !player) return;

  let activeRow = null;

  rows.forEach(row => {
    row.addEventListener('click', () => {
      const embedUrl = row.dataset.embed;

      if (row === activeRow) {
        // Clicking the active row again — deactivate
        deactivate(row);
        activeRow = null;
        return;
      }

      // Deactivate previous row first
      if (activeRow) {
        deactivate(activeRow);
      }

      // Activate this row
      activate(row, embedUrl);
      activeRow = row;
    });
  });

  function activate(row, embedUrl) {
    row.classList.add('is-active');
    const playBtn = row.querySelector('.song-play-btn');
    if (playBtn) {
      playBtn.innerHTML = pauseIcon();
      playBtn.setAttribute('aria-label', 'Pause');
    }
    // Load the embed URL into the iframe
    if (embedUrl && embedUrl !== '#') {
      player.src = embedUrl;
      player.style.display = 'block';
    }
  }

  function deactivate(row) {
    row.classList.remove('is-active');
    const playBtn = row.querySelector('.song-play-btn');
    if (playBtn) {
      playBtn.innerHTML = playIcon();
      playBtn.setAttribute('aria-label', 'Play');
    }
    player.src = '';
    player.style.display = 'none';
  }

  function playIcon() {
    return `<svg viewBox="0 0 24 24" fill="currentColor" width="16" height="16">
      <path d="M8 5v14l11-7z"/>
    </svg>`;
  }

  function pauseIcon() {
    return `<svg viewBox="0 0 24 24" fill="currentColor" width="16" height="16">
      <path d="M6 19h4V5H6zm8-14v14h4V5z"/>
    </svg>`;
  }
})();
