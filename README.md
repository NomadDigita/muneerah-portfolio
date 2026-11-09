# Muneerah Muhammad Thalith — Professional Portfolio

Live: **https://muneerah-cv.vercel.app** · Contact: contact@muneerah.page · Telegram: @DNeerah · X: @Dneerah_

An original, mobile-first eleven-page portfolio for community management, digital marketing, customer support and related remote opportunities.

## Contents

- `index.html` — homepage and selected work
- `about/`, `experience/`, `work/` — profile, experience and three project case studies
- `evidence/` — screenshot-backed evidence archive with filters and accessible lightbox
- `evidence/studio/` — **local-only** evidence preparation tool (no public server uploads)
- `resume/`, `contact/` — four role-focused ATS-readable PDF downloads and direct contact methods
- `data/evidence.json` — approved additions. Add one object per uploaded proof image; upload the matching `<slug>.webp` into `assets/media/`
- `make_resume.py`, `build_site.py` — deterministic source generators. Regenerate PDFs first, then pages.

## Evidence workflow

1. Visit `/evidence/studio/`, choose a screenshot Muneerah has permission to publish and **redact financial or personal details before loading**.
2. Supply a short, accurate title and description and download the optimized WebP and entry JSON.
3. Upload the WebP to `assets/media/` using GitHub and append the JSON object to `data/evidence.json`.
4. Commit to `main`, and the linked Vercel project publishes the change.

This deliberately avoids an unauthenticated public image upload endpoint. The website does not collect form messages or user files. If a private owner-only upload dashboard is required later, add authenticated storage and server-side publishing controls.

## Local development

Any static server works; for example: `python -m http.server 4173`, then open `http://localhost:4173/`. Running `python make_resume.py && python build_site.py` regenerates PDFs and pages. Dependencies: Pillow, reportlab. The portfolio itself has zero npm dependencies.

## Source authenticity

Work history is presented as independent affiliate and community projects. Images are supporting snapshots, not independently audited statements. Don’t claim professional Discord moderation, previous exchange employment, or third-party testimonials without evidence/permission.

## Deploy

Vercel project name: `muneerah-cv`. GitHub repository: `NomadDigita/muneerah-portfolio`. No environment variables are required for the static website.
