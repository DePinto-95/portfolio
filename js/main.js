/* ============================================================
   main.js — shared across all pages
   Handles: hamburger nav, scroll-triggered fade-in
   ============================================================ */

// ── Hamburger nav toggle ─────────────────────────────────────
const nav = document.querySelector('.nav');
const hamburger = document.querySelector('.nav-hamburger');

if (hamburger && nav) {
  hamburger.addEventListener('click', () => {
    nav.classList.toggle('is-open');
    const expanded = nav.classList.contains('is-open');
    hamburger.setAttribute('aria-expanded', expanded);
  });

  // Close menu when any nav link is clicked
  nav.querySelectorAll('.nav-links a').forEach(link => {
    link.addEventListener('click', () => {
      nav.classList.remove('is-open');
      hamburger.setAttribute('aria-expanded', 'false');
    });
  });
}

// ── Scroll-triggered fade-in ─────────────────────────────────
// Watches elements with class .fade-in and .fade-in-group,
// adds .is-visible when they enter the viewport.
const fadeEls = document.querySelectorAll('.fade-in, .fade-in-group');

if ('IntersectionObserver' in window && fadeEls.length) {
  const observer = new IntersectionObserver(
    (entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add('is-visible');
          observer.unobserve(entry.target); // animate once
        }
      });
    },
    { threshold: 0.1 }
  );

  fadeEls.forEach(el => observer.observe(el));
} else {
  // Fallback: show everything immediately if IntersectionObserver not supported
  fadeEls.forEach(el => el.classList.add('is-visible'));
}
