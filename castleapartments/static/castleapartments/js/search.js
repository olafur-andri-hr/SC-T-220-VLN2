(() => {
  document.getElementById('search_button')
      .addEventListener('click', fetchListings);
  /**
   * Clear old listings from the result.
   */
  function clearListings() {}
  /**
   * Fetch listings from the server and add them to the results
   */
  function fetchListings() {
    const form = document.getElementById('search_banner_form');
    const data = new FormData(form);
    const url = '/listings/api/search/';
    const listingsDiv = document.getElementById('listings_container');

    fetch(url, {
      method: 'post',
      body: data,
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

