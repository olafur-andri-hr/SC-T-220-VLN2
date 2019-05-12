(() => {
  document.getElementById('search_button')
      .addEventListener('click', search);

  document.getElementById('page-selection-list')
      .addEventListener('click', pageClick);

  window.addEventListener('popstate', back);

  document.getElementById('id_order_by')
      .addEventListener('change', search);

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
      history.pushState(
          {}, 'Search', query
      );
      const url = '/listings/api/search/';
      const listingsDiv = document.getElementById('listings_container');
      fetchListings(url + query, listingsDiv);
      updateSearchNavPage(Number(target.value));
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
    updateSearchNavPage(Number(query.page_number));
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
    updateSearchNavPage(1);
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
      updateSearchNav(obj.meta);
      for (const listing of obj.listings) {
        createCard(listingsDiv, listing);
      }
    });
  }

  /**
   * Update page nav after search
   * @param {Number} pageNumber the number of the active page
   */
  function updateSearchNavPage(pageNumber=1) {
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

  /**
   * Update page nav after search
   * @param {Object} meta metadata for page info
   */
  function updateSearchNav(meta) {
    const listingCount = document.getElementById('listing-count');
    listingCount.textContent = meta.result_count;
    const pageNavList = document.getElementById('page-selection-list');
    const prevPage = pageNavList.firstElementChild;
    const nextPage = pageNavList.lastElementChild;
    while (pageNavList.firstElementChild) {
      pageNavList.removeChild(pageNavList.firstElementChild);
    }
    pageNavList.appendChild(prevPage);


    for (let index = 1; index <= meta.page_count; index++) {
      const li = document.createElement('li');
      li.classList.add('page-item');
      const link = document.createElement('input');
      link.className = 'page-link';
      link.href = '#search-results';
      link.type = 'submit';
      link.form = 'search_banner_form';
      link.value = index;
      link.name = 'page_number';
      li.appendChild(link);
      if (index == meta.page_number) {
        li.classList.add('active');
        const span = document.createElement('span');
        span.className = 'sr-only';
        span.textContent = '(current)';
        li.appendChild(span);
      }
      pageNavList.appendChild(li);
    }
    pageNavList.appendChild(nextPage);
    updateSearchNavPage(meta.page_number);
  }
})();

