document.addEventListener('DOMContentLoaded', function () {
  const revealElements = document.querySelectorAll('.fade-up');
  const revealObserver = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        entry.target.classList.add('reveal-visible');
        revealObserver.unobserve(entry.target);
      }
    });
  }, {
    threshold: 0.18,
  });

  revealElements.forEach((el) => revealObserver.observe(el));

  const smoothScrollLinks = document.querySelectorAll('a[data-scroll]');
  smoothScrollLinks.forEach((link) => {
    link.addEventListener('click', (event) => {
      const targetId = link.getAttribute('href');
      if (targetId && targetId.startsWith('#')) {
        event.preventDefault();
        document.querySelector(targetId)?.scrollIntoView({ behavior: 'smooth', block: 'start' });
      }
    });
  });
});
