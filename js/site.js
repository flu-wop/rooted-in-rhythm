(function () {
  var btn = document.querySelector('[data-menu]');
  var nav = document.getElementById('site-nav');
  if (!btn || !nav) return;
  btn.addEventListener('click', function () {
    var open = btn.getAttribute('aria-expanded') === 'true';
    btn.setAttribute('aria-expanded', String(!open));
    document.body.classList.toggle('menu-open', !open);
  });
  nav.addEventListener('click', function (e) {
    if (e.target.tagName === 'A') { btn.setAttribute('aria-expanded', 'false'); document.body.classList.remove('menu-open'); }
  });
  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape') { btn.setAttribute('aria-expanded', 'false'); document.body.classList.remove('menu-open'); }
  });
})();
