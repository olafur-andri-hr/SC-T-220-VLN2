(() => {
  const postalCode = document.getElementById('id_zip_code');
  const country = document.getElementById('id_country');
  const town = document.getElementById('id_town');

  postalCode.addEventListener('change', getTown);
  country.addEventListener('change', getTown);

  /**
   * Function to get a town from the server based on the given
   * Country and postal code.
   * @param {Event} event the input change event
   */
  function getTown() {
    const url = '/location/' + country.value + '/' + postalCode.value;
    fetch(url, {
      method: 'GET',
    }).then((response) => {
      return response.json();
    }).catch(() => {
      return;
    }).then((obj) => {
      if (obj) {
        town.value = obj.town;
      }
    });
  }
})();
