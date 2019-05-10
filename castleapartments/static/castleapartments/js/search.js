(() => {
  document.getElementById('search_button')
      .addEventListener('click', fetchListings);
  /**
   * Clear old listings from the result
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
      obj = JSON.parse(obj);
      console.log(obj);
      clearListings();
      for (const listing of obj.listings) {
        createListing(listingsDiv, listing);
      }
    });
  }

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

    const uglyDate = new Date(Date.parse(listing.listing_date));
    const dateOptions = {year: 'numeric', month: 'long', day: 'numeric'};
    const prettyDate = uglyDate.toLocaleString('en-US', dateOptions);
    makeParagraph(prettyDate, cardImgTop, ['card-listing-date']);

    const cardBody = document.createElement('div');
    cardBody.classList.add('card-body');
    
    const cardTitle = document.createElement('h5');
    cardTitle.textContent = listing.apartment.address;
    cardTitle.classList.add('card-title', 'no-margin');
    cardBody.appendChild(cardTitle);

    const postalCode = listing.apartment.postal_code;
    makeParagraph(
        postalCode.zip_code + ', ' + postalCode.town,
        cardBody, ['card-text', 'no-margin', 'text-sm']
    );

    const countryPara = makeParagraph(
        ' ' + postalCode.country.name,
        cardBody, ['card-text', 'no-margin', 'text-sm']
    );
    const countryFlag = document.createElement('img');
    countryFlag.src = postalCode.country.flag;
    countryPara.insertBefore(countryFlag, countryPara.firstChild);

    makeParagraph(
        listing.apartment.apartment_type.name + ', ' +
        listing.apartment.num_rooms + ' bedrooms',
        cardBody, ['card-text', 'card-apt-type']
    );
    const cardPrice = document.createElement('h5');
    cardPrice.classList.add('card-price');
    cardPrice.textContent = ' ' + listing.apartment.appraisal.toLocaleString();
    const priceSpan = document.createElement('span');
    priceSpan.textContent = 'ISK';
    cardPrice.insertBefore(priceSpan, cardPrice.firstChild);

    const hr1 = document.createElement('hr');
    const hr2 = document.createElement('hr');
    cardBody.appendChild(hr1);
    cardBody.appendChild(cardPrice);
    cardBody.appendChild(hr2);

    makeParagraph(listing.apartment.description, cardBody,
        ['card-text', 'card-description']
    );

    listingLink = document.createElement('a');
    listingLink.classList = 'card-link';
    listingLink.href = '/listing/' + listing.uuid;
    cardBody.appendChild(listingLink);


    const card = document.createElement('div');
    card.classList.add('card');

    card.appendChild(cardImgTop);
    card.appendChild(cardBody);
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

