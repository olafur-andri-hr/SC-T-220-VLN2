document.getElementById('hamburger').addEventListener('click', hamburger);
document.getElementById('closeicon').addEventListener('click', hamburger);
// document.getElementById('accountdiv')
//     .addEventListener('click', sidebardropdown);

/**
 * function for sliding the sidebar nav menu
 */
// function sidebardropdown() {
//   document.getElementById('sidebar').classList.toggle('active');
// }

/**
 * function for the hamburger menu
 */
function hamburger() {
  const navbar = document.getElementById('dropdownnav');
  const ham = document.getElementById('hamburger');
  const close = document.getElementById('closeicon');
  if (navbar.className === 'active') {
    navbar.className = 'notActive';
    close.style.display = 'none';
  } else {
    navbar.className = 'active';
    close.style.display = 'flex';
  }
  ham.classList.toggle('humbergur90');
}

window.addEventListener('click', function(event) {
  let target = event.target;
  const overlay = document.getElementById('sidebar');
  const div = document.getElementById('accountdiv');
  while (target != document.body) {
    if (target == div) {
      overlay.classList.toggle('active');
      return;
    } else if (target == overlay) {
      return;
    }
    target = target.parentNode;
  }
  overlay.classList.remove('active');
});
