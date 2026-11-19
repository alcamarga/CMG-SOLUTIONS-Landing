document.addEventListener('DOMContentLoaded', function () {
    // Agregar eventos de clic o cambios de estado aquí

    // Animación de entrada para la Vitrina Comercial.
    // La clase .pre-reveal solo se aplica vía JS: sin JS el contenido queda visible.
    var revealTargets = document.querySelectorAll('[data-reveal]');
    var prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

    if (!revealTargets.length) return;

    if (prefersReducedMotion || !('IntersectionObserver' in window)) {
        return;
    }

    revealTargets.forEach(function (el) {
        el.classList.add('pre-reveal');
    });

    var observer = new IntersectionObserver(function (entries) {
        entries.forEach(function (entry) {
            if (entry.isIntersecting) {
                entry.target.classList.add('is-visible');
                observer.unobserve(entry.target);
            }
        });
    }, { threshold: 0.15, rootMargin: '0px 0px -40px 0px' });

    revealTargets.forEach(function (el) {
        observer.observe(el);
    });
});
