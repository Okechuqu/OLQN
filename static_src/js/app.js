const button = document.querySelector('[data-menu-button]');
const menu = document.querySelector('[data-menu]');
if (button && menu) {
  button.addEventListener('click', () => {
    const open = menu.classList.toggle('open');
    button.setAttribute('aria-expanded', String(open));
    button.textContent = open ? '×' : '☰';
  });
}
