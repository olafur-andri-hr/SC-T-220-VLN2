// Global variables
const listingHint = document.getElementById('listing-hint');
const siteHeader = document.getElementById('site_header');
const checkboxButton = document.getElementById('checkbox_button');
const checkboxes = document.getElementById('checkboxes');
const historyButton = document.getElementById('history_button');
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
  checkboxButton.addEventListener('click', showCheckboxes);
  historyButton.addEventListener('click', showHistory);
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
    e.preventDefault();
  } catch (_) {
    // Do nothing
  }
}

/**
 * The event handler a click event on the checkbox button
 * @param {Event} e The event object for this function
 */
function showCheckboxes(e) {
  checkboxButton.firstElementChild.innerText = 'Click away to close';
  checkboxes.className = 'active';
  checkboxButton.removeEventListener('click', showCheckboxes);
  setTimeout(() => {
    window.addEventListener('click', hideCheckboxes);
  }, 0);
}

/**
 * Hides the 'apartment type' checkboxes if user clicks away
 * @param {Event} e The event object for this function
 */
function hideCheckboxes(e) {
  if (checkboxes.contains(e.target)) {
    return;
  }
  checkboxButton.firstElementChild.innerText = 'Choose Type(s)';
  checkboxes.className = '';
  checkboxButton.addEventListener('click', showCheckboxes);
  window.removeEventListener('click', hideCheckboxes);
}

/**
 * An event handler for when the user wants to view his/her search history
 * @param {Event} e The event object for this click event handler
 */
function showHistory(e) {
  const listings = document.getElementById('listings_container');
  const searchHistory = document.getElementById('search_history');

  historyButton.lastElementChild.innerText = 'Go back to listings';
  listings.classList.add('hide');
  searchHistory.classList.add('show');
  historyButton.removeEventListener('click', showHistory);

  setTimeout(() => {
    listings.classList.add('remove');
  }, 200);
}

main();
