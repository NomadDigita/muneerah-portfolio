# Muneerah Muhammad Thalith · Portfolio

A professional portfolio for Muneerah Muhammad Thalith, focused on digital marketing, community management, and customer experience.

**Live site:** https://cv.muneerah.top  
**Contact:** contact@muneerah.top  
**X:** https://x.com/Dneerah_ · **Telegram:** https://t.me/DNeerah

## Site

Eleven responsive pages: Home, About, Experience, Work, three case studies, Recognition & Results, Evidence Studio, Résumé, and Contact. The site includes a portrait-based brand icon, a sticky Liquid Glass navigation, dark/light themes, accessible keyboard navigation, restrained motion, a filterable image gallery, and downloadable résumé PDFs.

## Résumés

Four job-targeted, single-page, text-based PDFs are generated from `make_resume.py` and stored in `assets/`: general, community management, customer support, and digital marketing. The documents use a single-column layout and conventional headings suitable for recruitment workflows.

The résumé's experience represents independent digital marketing and community initiatives. LearnerFlex recognition refers to affiliate performance, not employment by LearnerFlex. Sales and audience figures are presented in their specific award or community context.

## Update workflow

- Update website content in `build_site.py` and regenerate the 11 static pages: `python build_site.py`.
- Regenerate PDF résumés: `python make_resume.py` (requires ReportLab and Lato font installed on the builder).
- Adjust CSS and behavior in `assets/site.css` and `assets/site.js`.
- Commit to `main` to trigger the connected Vercel production deployment.
- Add approved public proof images to `assets/media`, and review information before publishing. Evidence Studio prepares local exports; it does not accept public server-side uploads.

## Accessibility and design

No frontend build dependency is required. The site uses semantic HTML, a skip link, focus-visible outlines, reduced-motion fallbacks, responsive grids, native theme controls, and graceful backdrops where supported. Typography and layout favor clarity over decorative effects.

## Experience timeline (confirmed 9 November 2026)

Muneerah began digital marketing on 3 December 2023. Independent digital product and affiliate marketing platform history:

- Digitstem — January 2024 to November 2024
- ZenithStake — December 2024 to May 2025
- Selar — January 2025 to June 2025
- LearnerFlex — June 2025 to May 2026

These are platform experience periods, **not asserted company employment contracts**. Overlapping date ranges are intentional. The interactive Experience page features accessible arrow/tab and swipe navigation and displays every card when JavaScript is unavailable. To edit the experience, update the `platforms` data in `build_site.py` and the PDF role descriptions in `make_resume.py`, then regenerate both.
