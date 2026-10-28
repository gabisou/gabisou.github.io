/* Native disclosure; without JavaScript the navigation remains visible. */
(() => {
  const header = document.querySelector('.site-header');
  const button = header?.querySelector('.header-menu');
  const navigation = header?.querySelector('.header-navigation');
  if (!button || !navigation) return;

  const compact = window.matchMedia('(max-width: 95em)');
  let expanded = false;

  function render() {
    const mobile = compact.matches;
    // Reveal the destination before moving focus and hiding its former owner.
    if (mobile) button.hidden = false;
    else navigation.hidden = false;
    if (mobile && !expanded && navigation.contains(document.activeElement)) button.focus();
    if (!mobile && document.activeElement === button) navigation.querySelector('a').focus();
    button.hidden = !mobile;
    button.setAttribute('aria-expanded', String(mobile && expanded));
    navigation.hidden = mobile && !expanded;
  }

  function close(returnFocus = false) {
    expanded = false;
    if (returnFocus) button.focus();
    render();
  }

  header.setAttribute('data-menu-ready', '');
  button.addEventListener('click', () => { expanded = !expanded; render(); });
  header.addEventListener('keydown', (event) => {
    if (event.key === 'Escape' && compact.matches && expanded) {
      event.preventDefault();
      close(true);
    }
  });
  navigation.addEventListener('click', (event) => {
    if (compact.matches && event.target.closest('a[href^="#"]')) close(true);
  });
  compact.addEventListener('change', () => { expanded = false; render(); });
  render();
})();
