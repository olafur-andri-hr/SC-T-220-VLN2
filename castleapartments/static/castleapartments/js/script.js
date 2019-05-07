// Global variables
const listingHint = document.getElementById('listing-hint');
let hintIsHidden = false;

/**
 * The main function for the file
 */
function main() {
  addEventListeners();
}

/**
 * Adds event listeners to all the necessary HTML elements
 */
function addEventListeners() {
  window.addEventListener('scroll', onScroll);
}

/**
 * The window scroll event handler
 * @param {Event} e The object that represents the scroll event
 */
function onScroll(e) {
  const height = window.innerHeight;
  const bottom = listingHint.getBoundingClientRect().bottom;
  const toBottom = height - bottom;
  if (toBottom > 40) {
    if (hintIsHidden) {
      return;
    }
    hintIsHidden = true;
    listingHint.className = 'hide';
  } else {
    if (!hintIsHidden) {
      return;
    }
    listingHint.className = '';
    hintIsHidden = false;
  }
}

main();
