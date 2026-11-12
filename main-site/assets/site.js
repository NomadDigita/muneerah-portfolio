(() => {
  const header = document.querySelector('[data-header]');
  const progress = document.querySelector('[data-progress]');
  const mobileMenu = document.querySelector('[data-mobile-menu]');
  const menuToggle = document.querySelector('[data-menu-toggle]');
  const navLinks = [...document.querySelectorAll('.desktop-nav .nav-link')];
  const sections = [...document.querySelectorAll('main section[id]')];

  const updateScroll = () => {
    const y = window.scrollY || 0;
    header?.classList.toggle('is-scrolled', y > 20);
    const max = document.documentElement.scrollHeight - window.innerHeight;
    if (progress) progress.style.width = `${max > 0 ? Math.min(100, y / max * 100) : 0}%`;
  };
  window.addEventListener('scroll', updateScroll, { passive: true });
  updateScroll();

  const setMenu = (open) => {
    menuToggle?.setAttribute('aria-expanded', String(open));
    menuToggle?.setAttribute('aria-label', open ? 'Close navigation' : 'Open navigation');
    mobileMenu?.classList.toggle('is-open', open);
    if (mobileMenu) mobileMenu.inert = !open;
    document.body.classList.toggle('menu-open', open);
  };
  menuToggle?.addEventListener('click', () => setMenu(menuToggle.getAttribute('aria-expanded') !== 'true'));
  mobileMenu?.querySelectorAll('a').forEach(link => link.addEventListener('click', () => setMenu(false)));
  document.addEventListener('keydown', event => {
    if (event.key === 'Escape') setMenu(false);
  });

  const revealObserver = new IntersectionObserver(entries => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('is-visible');
        revealObserver.unobserve(entry.target);
      }
    });
  }, { threshold: 0.14 });
  document.querySelectorAll('[data-reveal]').forEach(el => revealObserver.observe(el));

  const sectionObserver = new IntersectionObserver(entries => {
    entries.forEach(entry => {
      if (!entry.isIntersecting) return;
      const current = `#${entry.target.id}`;
      navLinks.forEach(link => link.classList.toggle('is-active', link.getAttribute('href') === current));
    });
  }, { rootMargin: '-35% 0px -50% 0px' });
  sections.forEach(section => sectionObserver.observe(section));

  const slides = [...document.querySelectorAll('[data-project]')];
  const currentIndex = document.querySelector('[data-project-current]');
  const currentName = document.querySelector('[data-project-name]');
  const names = ['One month. 600+ sales.', 'Good work keeps compounding.', 'Make it useful. Make it welcoming.', 'Clarity is a kind of care.'];
  let activeIndex = 0;
  const showSlide = index => {
    activeIndex = (index + slides.length) % slides.length;
    slides.forEach((slide, i) => {
      slide.hidden = i !== activeIndex;
      slide.classList.toggle('is-current', i === activeIndex);
      slide.setAttribute('aria-hidden', String(i !== activeIndex));
    });
    if (currentIndex) currentIndex.textContent = String(activeIndex + 1).padStart(2, '0');
    if (currentName) currentName.textContent = names[activeIndex];
  };
  document.querySelector('[data-project-next]')?.addEventListener('click', () => showSlide(activeIndex + 1));
  document.querySelector('[data-project-prev]')?.addEventListener('click', () => showSlide(activeIndex - 1));
  const viewport = document.querySelector('.project-viewport');
  let touchStartX = null;
  viewport?.addEventListener('touchstart', event => { touchStartX = event.changedTouches[0].screenX; }, { passive: true });
  viewport?.addEventListener('touchend', event => {
    if (touchStartX === null) return;
    const delta = event.changedTouches[0].screenX - touchStartX;
    if (Math.abs(delta) > 48) showSlide(activeIndex + (delta < 0 ? 1 : -1));
    touchStartX = null;
  }, { passive: true });
  showSlide(0);

  const evidence = {
    award: ['/assets/learnerflex-award.webp', 'MARCH 2026 · TOP AFFILIATE'],
    dashboard: ['/assets/learnerflex-dashboard.webp', 'LEARNERFLEX · SALES DASHBOARD'],
    community: ['/assets/community-survey.webp', 'TELEGRAM · COMMUNITY SNAPSHOT'],
    feedback: ['/assets/learner-feedback.webp', 'LEARNER FEEDBACK · PRIVATE DETAILS OMITTED'],
    recognition: ['/assets/social-recognition.webp', 'PUBLIC RECOGNITION · 600+ SALES'],
    volume: ['/assets/volume-summary.webp', 'CAMPAIGN SNAPSHOT · MULTI-CURRENCY VOLUME'],
    reamb: ['/assets/reamb-channel.webp', 'REAMB · LEARNING COMMUNITY']
  };
  const modal = document.querySelector('[data-evidence-modal]');
  const modalImage = document.querySelector('[data-modal-image]');
  const modalLabel = document.querySelector('[data-modal-label]');
  const openEvidence = key => {
    const item = evidence[key];
    if (!item || !modal || !modalImage) return;
    modalImage.src = item[0];
    modalImage.alt = item[1].toLowerCase().replaceAll('·', ',');
    if (modalLabel) modalLabel.textContent = item[1];
    modal.showModal();
  };
  document.querySelectorAll('[data-evidence]').forEach(button => button.addEventListener('click', () => openEvidence(button.dataset.evidence)));
  document.querySelector('[data-open-feedback]')?.addEventListener('click', event => {
    event.preventDefault();
    openEvidence('feedback');
  });
  modal?.querySelector('.modal-close')?.addEventListener('click', () => modal.close());
  modal?.addEventListener('click', event => {
    if (event.target === modal) modal.close();
  });
  modal?.addEventListener('close', () => { if (modalImage) modalImage.removeAttribute('src'); });
})();
