(() => {
  document.getElementById('search_button')
      .addEventListener('click', (event) => {
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
          obj = JSON.parse(obj);
          console.log(obj);
          for (const listing of obj) {
            createListing(listingsDiv, listing);
          }
        });
      });

  /**
   * Add a listing to the listingDiv
   * @param {HTMLDivElement} listingsDiv DOM node containing listings
   * @param {Object} listing Listing object
   */
  function createListing(listingsDiv, listing) {
    const cardImgTop = document.createElement('div');
    cardImgTop.classList.add('card-img-top');
    const imgURI = listing.apartment.apartmentimage_set[0].image;
    cardImgTop.style.backgroundImage = 'url("' + imgURI + '")';

    const uglyDate = Date.parse(listing.listing_date);
    const dateOptions = {year: 'numeric', month: 'long', day: 'numeric'};
    const prettyDate = uglyDate.toLocaleString('en-US', dateOptions);
    makeParagraph(prettyDate, cardImgTop, ['card-listing-date']);

    const cardBody = document.createElement('div');
    const cardTitle = document.createElement('h5');
    cardTitle.textContent = listing.apartment.address;
    cardTitle.classList.add('card-title', 'no-margin');
    cardBody.appendChild(cardTitle);
    const postalCode = listing.apartment.postal_code;
    makeParagraph(
        postalCode.zip_code + ', ' + postalCode.city,
        cardBody, ['card-text', 'no-margin', 'text-sm']
    );
    makeParagraph(
        postalCode.zip_code + ', ' + postalCode.city,
        cardBody, ['card-text', 'no-margin', 'text-sm']
    );
    makeParagraph(
        postalCode.country,
        cardBody, ['card-text', 'no-margin', 'text-sm']
    );


    const card = document.createElement('div');
    card.classList.add('card');

    card.appendChild(cardImgTop);
    listingsDiv.appendChild(card);
  }

  /**
   * Make a paragraph and append it to the parent node.
   * @param {String} textContent Text content of the paragraph
   * @param {HTMLElement} parentNode Node to append the paragraph to
   * @param {Array<String>} classList optional list of classes for the paragraph
   * @return {HTMLParagraphElement} the paragraph created
   */
  function makeParagraph(textContent, parentNode, classList=[]) {
    const para = document.createElement('p');
    para.textContent = textContent;
    for (const className of classList) {
      para.classList.add(className);
    }
    parentNode.appendChild(para);
    return para;
  }
})();

