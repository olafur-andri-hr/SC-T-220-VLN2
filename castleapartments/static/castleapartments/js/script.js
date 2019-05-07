// Global variables
const listingHint = document.getElementById('listing-hint');
const siteHeader = document.getElementById('site_header');
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
  const editSearchLink = document.getElementById('edit_search');

  window.addEventListener('scroll', onScroll);
  editSearchLink.addEventListener('click', scrollToTop);
  listingHint.addEventListener('click', scrollToListings);
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

/**
 * Scrolls the user to the top of the website in a smoooth manner
 * @param {Event} e The event object for this function
 */
function scrollToTop(e) {
  try {
    window.scroll({
      top: 0,
      left: 0,
      behavior: 'smooth',
    });
    e.preventDefault();
  } catch (_) {
    // Do nothing
  }
}

/**
 * Scrolls the user in a smooth manner down to the recent listings page
 * @param {Event} e The event object for this function
 */
function scrollToListings(e) {
  try {
    const header = document.getElementById('search_results_header');
    const headerHeight = siteHeader.getBoundingClientRect().height;
    const headerOffsetTop = header.getBoundingClientRect().top;
    const offsetTop = headerOffsetTop - headerHeight;

    window.scroll({
      top: offsetTop,
      left: 0,
      behavior: 'smooth',
    });
  } catch (_) {
    // Do nothing
  }
}

main();
