(() => {
  document.getElementById('search_button')
      .addEventListener('click', search);

  document.getElementById('page-selection-nav')
      .addEventListener('click', pageClick);

  window.addEventListener('popstate', back);

  /**
   * Handle page clicks
   * @param {Event} event the event
   */
  function pageClick( event ) {
    if (event.target.classList.contains('page-link')) {
      
      scrollToListings(event);
    }
  }

  /**
   * Clear old listings from the result.
   * @param {Event} event the event
   */
  function back( event ) {
    const search = event.target.location.search;
    const query = '?' + new URLSearchParams(search).toString();
    const url = '/listings/api/search/';
    const listingsDiv = document.getElementById('listings_container');
    fetchListings(url + query, listingsDiv);
  }

  /**
   * Clear old listings from the result.
   * @return {Array} the removed listings
   */
  function clearListings() {
    const listings = document.getElementById('listings_container');
    const childNodes = [];
    while (listings.firstChild) {
      childNodes.push(listings.firstChild);
      listings.removeChild(listings.firstChild);
    }
    return childNodes;
  }
  /**
   * Fetch listings from the server and add them to the results
   * @param {Event} event the click event
   */
  function search( event ) {
    const form = document.getElementById('search_banner_form');
    const data = new FormData(form);
    const url = '/listings/api/search/';
    const listingsDiv = document.getElementById('listings_container');
    const queryString = '?' + new URLSearchParams(data).toString();
    history.pushState(
        {}, 'Search', queryString
    );

    fetchListings(url + queryString, listingsDiv);
    event.preventDefault();
    scrollToListings(event);
  }

  /**
   * Fetch listings from the server and add them to the results
   * @param {String} url the url with query parameter
   * @param {HTMLElement} listingsDiv the div to fill with listings
   */
  function fetchListings(url, listingsDiv) {
    fetch(url, {
      method: 'GET',
    }).then((response) => {
      return response.json();
    }).catch(() => {
      return;
    }).then((obj) => {
      console.log(obj);
      clearListings();
      for (const listing of obj.listings) {
        createCard(listingsDiv, listing);
      }
    });
  }
})();

