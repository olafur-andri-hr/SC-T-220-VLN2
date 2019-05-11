(() => {
  document.getElementById('search_button')
      .addEventListener('click', search);

  document.getElementById('page-selection-list')
      .addEventListener('click', pageClick);

  window.addEventListener('popstate', back);

  /**
   * Handle page clicks
   * @param {Event} event the event
   */
  function pageClick( event ) {
    let target = event.target;
    while (!target.classList.contains('page-link') &&
         target != event.currentTarget) {
      target = target.parentNode;
    }
    if (target.classList.contains('page-link')) {
      scrollToListings(event);
      const form = document.getElementById('search_banner_form');
      const data = new FormData(form);
      let query = '?' + new URLSearchParams(data).toString();
      query += '&page_number=' + target.value;
      const url = '/listings/api/search/';
      const listingsDiv = document.getElementById('listings_container');
      fetchListings(url + query, listingsDiv);
      updateSearchNav(Number(target.value));
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
    updateSearchNav(Number(query.page_number));
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
    updateSearchNav(1);
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

  /**
   * Update page nav after search
   * @param {Number} pageNumber the number of the active page
   */
  function updateSearchNav(pageNumber=1) {
    const pageNavList = document.getElementById('page-selection-list');
    const prevPage = pageNavList.firstElementChild.firstElementChild;
    const nextPage = pageNavList.lastElementChild.firstElementChild;
    prevPage.value = pageNumber - 1;
    nextPage.value = pageNumber + 1;
    if (prevPage.value > 0) {
      prevPage.removeAttribute('disabled');
      prevPage.parentNode.classList.remove('disabled');
    } else {
      prevPage.setAttribute('disabled', '');
      prevPage.parentNode.classList.add('disabled');
    }
    for (let element of pageNavList.childNodes) {
      element = element.firstElementChild;
      if (element) {
        if (element.value == pageNumber) {
          element.parentNode.classList.add('active');
        } else {
          element.parentNode.classList.remove('active');
        }
      }
    }
    if (nextPage.value <= pageNavList.childElementCount - 2) {
      nextPage.removeAttribute('disabled');
      nextPage.parentNode.classList.remove('disabled');
    } else {
      nextPage.setAttribute('disabled', '');
      nextPage.parentNode.classList.add('disabled');
    }
  }
})();

