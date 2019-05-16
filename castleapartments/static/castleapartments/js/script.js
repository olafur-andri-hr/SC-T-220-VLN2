// Global variables
const listingHint = document.getElementById('listing-hint');
const siteHeader = document.getElementById('site_header');
const checkboxButton = document.getElementById('checkbox_button');
const checkboxes = document.getElementById('checkboxes');
const historyButton = document.getElementById('history_button');
const listingsContainer = document.getElementById('listings_container');
const searchHistory = document.getElementById('recently_viewed');
const pagination = document.getElementById('page-selection-nav');
let hintIsHidden = false;
let historyIsLoaded = false;

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
  editSearchLink.addEventListener('click', ( event) => {
    setTimeout(() => {
      document.getElementById('id_address').focus();
    }, 1000);
    scrollToTop(event);
  });
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
    const header = document.getElementById('frontpage-div');
    const headerHeight = siteHeader.getBoundingClientRect().height;
    const headerOffsetTop = header.getBoundingClientRect().height;
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
  populateHistory();
  document.getElementById('page-selection-div').classList.add('d-none');
  historyButton.lastElementChild.innerText =
    historyButton.getAttribute('data-new-text');
  listingsContainer.classList.add('hide');
  historyButton.removeEventListener('click', showHistory);
  historyButton.addEventListener('click', hideHistory);
  pagination.classList.add('hide');

  setTimeout(() => {
    listingsContainer.classList.add('remove');
    searchHistory.classList.add('create');

    setTimeout(() => {
      searchHistory.classList.add('show');
    }, 100);
  }, 200);
}

/**
 * The click event handler when the user wants to hide his/her history
 * @param {Event} e The event object for this click event handler
 */
function hideHistory(e) {
  searchHistory.classList.remove('show');
  pagination.classList.remove('hide');
  historyButton.lastElementChild.innerText =
    historyButton.getAttribute('data-original-text');

  setTimeout(() => {
    searchHistory.classList.remove('create');
    listingsContainer.classList.remove('remove');

    setTimeout(() => {
      listingsContainer.classList.remove('hide');
      document.getElementById('page-selection-div').classList.remove('d-none');
      historyButton.removeEventListener('click', hideHistory);
      historyButton.addEventListener('click', showHistory);
    }, 200);
  }, 200);
}

/**
 * Adds all of the user's recently viewed apartments to the #recently_viewed
 * container
 */
function populateHistory() {
  if (historyIsLoaded) {
    return;
  }
  const emptyMessage = document.getElementById('recently_viewed_empty_message');
  const loadingMessage =
  document.getElementById('recently_viewed_loading_message');
  const viewed = window.localStorage.viewed;

  if (!viewed) {
    emptyMessage.classList.add('create');
    loadingMessage.classList.add('remove');
    return;
  }

  const arr = JSON.parse(window.localStorage.viewed);
  emptyMessage.classList.remove('create');
  loadingMessage.classList.remove('remove');
  loadingMessage.firstElementChild.innerText = 'Fetching your history...';
  const xhr = new XMLHttpRequest();
  xhr.onreadystatechange = () => {
    if (xhr.readyState !== 4) {
      return;
    }
    if (xhr.status === 200) {
      const response = JSON.parse(xhr.responseText);
      loadingMessage.classList.add('remove');
      for (let i = 0; i < response.length; i++) {
        createCard(searchHistory, response[i]);
      }
      historyIsLoaded = true;
    }
  };
  const IDString = arr.join(',');
  xhr.open('GET', '/listings/api/search/' + IDString);
  xhr.send();
}

main();
