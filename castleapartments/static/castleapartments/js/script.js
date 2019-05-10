// Global variables
const listingHint = document.getElementById('listing-hint');
const siteHeader = document.getElementById('site_header');
const checkboxButton = document.getElementById('checkbox_button');
const checkboxes = document.getElementById('checkboxes');
const historyButton = document.getElementById('history_button');
const listingsContainer = document.getElementById('listings_container');
const searchHistory = document.getElementById('recently_viewed');
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
  const cards = document.querySelectorAll('#listings_container .card');

  window.addEventListener('scroll', onScroll);
  editSearchLink.addEventListener('click', scrollToTop);
  listingHint.addEventListener('click', scrollToListings);
  checkboxButton.addEventListener('click', showCheckboxes);
  historyButton.addEventListener('click', showHistory);
  listEventListeners(cards, 'click', registerToHistory);
}

/**
 * Adds event listeners to a NodeList (a list of HTML elements)
 * @param {NodeList} list A list of nodes to add the event listener to
 * @param {String} event The event to listen to
 * @param {function} func The event handler for the event listener
 */
function listEventListeners(list, event, func) {
  for (let i = 0; i < list.length; i++) {
    list[i].addEventListener(event, func);
  }
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
  populateHistory();
  historyButton.lastElementChild.innerText =
    historyButton.getAttribute('data-new-text');
  listingsContainer.classList.add('hide');
  historyButton.removeEventListener('click', showHistory);
  historyButton.addEventListener('click', hideHistory);

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
  historyButton.lastElementChild.innerText =
    historyButton.getAttribute('data-original-text');

  setTimeout(() => {
    searchHistory.classList.remove('create');
    listingsContainer.classList.remove('remove');

    setTimeout(() => {
      listingsContainer.classList.remove('hide');
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
      const cards = [];
      loadingMessage.firstElementChild.innerText = 'Creating cards...';
      for (let i = 0; i < response.length; i++) {
        const card = createApartmentCard(response[i]);
        cards.push(card);
      }
      loadingMessage.classList.add('remove');
      for (let i = 0; i < cards.length; i++) {
        searchHistory.appendChild(cards[i]);
      }
      historyIsLoaded = true;
    }
  };
  const IDString = arr.join(',');
  xhr.open('GET', '/listings/api/search/' + IDString);
  xhr.send();
}

/**
 * Creates and returns a new apartment card HTML element
 * @param {Object} data An object that holds the data for the apartment card
 * @return {HTMLElement} An HTML element representing the created card
 */
function createApartmentCard(data) {
  const date = new Date(data.listing_date);
  const monthNames = ['January', 'February', 'March', 'April', 'May', 'June',
    'July', 'August', 'September', 'October', 'November', 'December'];

  // .card <div></div>
  const card = document.createElement('div');
  card.classList.add('card');

  // .card-img-top <div></div>
  const cardImgTop = document.createElement('div');
  cardImgTop.classList.add('card-img-top');
  cardImgTop.style.backgroundImage = 'url(' + data.image + ')';

  // .card-listing-date <p></p>
  const cardListingDate = document.createElement('p');
  const month = monthNames[date.getMonth()];
  const day = date.getDay();
  const year = date.getFullYear();
  cardListingDate.classList.add('card-listing-date');
  cardListingDate.innerText = 'Added: ' + month + ' ' + day + ', ' + year;

  // .card-body <div></div>
  const cardBody = document.createElement('div');
  cardBody.classList.add('card-body');

  // .card-title.no-margin <h5></h5>
  const cardTitle = document.createElement('h5');
  cardTitle.classList.add('card-title');
  cardTitle.classList.add('no-margin');
  cardTitle.innerText = data.address;

  // .card-text.no-margin.text-sm <p></p>
  const p1 = document.createElement('p');
  p1.classList.add('card-text');
  p1.classList.add('no-margin');
  p1.classList.add('text-sm');
  p1.innerText = data.zip_code + ', ' + data.town;

  // .card-text.no-margin.text-sm <p></p>
  const p2 = document.createElement('p');
  p2.classList.add('card-text');
  p2.classList.add('no-margin');
  p2.classList.add('text-sm');
  p2.innerText = data.country;

  // create flag icon here!!!

  // .card-text.no-margin.text-sm <p></p>
  const p3 = document.createElement('p');
  p3.classList.add('card-text');
  p3.classList.add('no-margin');
  p3.classList.add('text-sm');
  if (data.apt_number) {
    p3.innerText = data.country;
  }

  // .card-text.card-apt-type
  const p4 = document.createElement('p');
  p4.classList.add('card-text');
  p4.classList.add('card-apt-type');
  p4.innerHTML = '<b>' + data.type + '</b> ' + data.num_rooms + ' bedrooms';

  // <hr />
  const hr1 = document.createElement('hr');


  // .card-price <h5></h5>
  const cardPrice = document.createElement('h5');
  cardPrice.classList.add('card-price');
  cardPrice.innerHTML = '<span>ISK</span> ' + data.price.toLocaleString();

  // <hr />
  const hr2 = document.createElement('hr');

  // .card-text.card-description <p></p>
  const cardDescription = document.createElement('p');
  let description = data.description;
  cardDescription.classList.add('card-text');
  cardDescription.classList.add('card-description');
  if (description.length > 100) {
    description = description.substring(0, 100) + '...';
  }
  cardDescription.innerText = description;

  // .card-link <a></a>
  const cardLink = document.createElement('a');
  cardLink.classList.add('card-link');
  cardLink.setAttribute('href', '/listing/' + data.uuid);

  // Populate card
  cardImgTop.appendChild(cardListingDate);
  card.appendChild(cardImgTop);
  cardBody.appendChild(cardTitle);
  cardBody.appendChild(p1);
  cardBody.appendChild(p2);
  cardBody.appendChild(p3);
  cardBody.appendChild(p4);
  cardBody.appendChild(hr1);
  cardBody.appendChild(cardPrice);
  cardBody.appendChild(hr2);
  cardBody.appendChild(cardDescription);
  card.appendChild(cardBody);
  card.appendChild(cardLink);
  return card;
}

/**
 * Registers a click on a card to the localStorage API
 * @param {Event} e The event object for this event handler
 */
function registerToHistory(e) {
  if (!window.localStorage.viewed) {
    window.localStorage.viewed = '[]';
  }

  const MAX_LENGTH = 10;
  const id = e.target.parentNode.getAttribute('data-id');
  let arr = JSON.parse(window.localStorage.viewed);
  arr = removeValueFromArray(arr, id);
  arr.unshift(id);
  arr = arr.slice(0, MAX_LENGTH);
  window.localStorage.viewed = JSON.stringify(arr);
}

/**
 * Removes all occurrences of a specific value from an array
 * @param {Array} array The array to remove the value from
 * @param {*} value The value which you want to remove
 * @return {Array} The new array
 */
function removeValueFromArray(array, value) {
  newArray = [];
  for (let i = 0; i < array.length; i++) {
    if (array[i] !== value) {
      newArray.push(array[i]);
    }
  }
  return newArray;
}

main();
