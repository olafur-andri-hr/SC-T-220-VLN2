/**
 * The function that is always run when the file is loaded
 */
function main() {
  addEventListeners();
  enableAppropriateCarouselControls();
}

/**
 * Adds all necessary event listeners to the page
 */
function addEventListeners() {
  const carouselRights =
    document.querySelectorAll('.carousel-controls .carousel-right-control');
  const carouselLefts =
    document.querySelectorAll('.carousel-controls .carousel-left-control');

  addManyListeners(carouselRights, 'click', showNextSlide);
  addManyListeners(carouselLefts, 'click', showPreviousSlide);
}

/**
 * Adds event listeners to a list of HTML elements
 * @param {NodeList} nodeList A list of HTML elements to add the listener to
 * @param {String} eventType The type of event to listen to
 * @param {function} func The event handler for the function
 */
function addManyListeners(nodeList, eventType, func) {
  for (let i = 0; i < nodeList.length; i++) {
    nodeList[i].addEventListener(eventType, func);
  }
}

/**
 * Shows the next slide on the carousel.
 * @param {Event} e The event object for this function
 */
function showNextSlide(e) {
  const carousel = document.querySelector('.carousel');
  const carouselSlides = carousel.querySelector('.carousel .carousel-slides');
  const numSlides = getNumSlides(carousel);
  let activeSlide = Number(carouselSlides.getAttribute('data-active-slide'));
  if (activeSlide + 1 >= numSlides) {
    return;
  }
  const transform = 100 + (activeSlide * 100);
  activeSlide++;
  carouselSlides.style.transform = 'translateX(-' + String(transform) + '%)';
  carouselSlides.setAttribute('data-active-slide', String(activeSlide));
  e.target.parentNode.firstElementChild.removeAttribute('disabled');
  if (activeSlide + 1 >= numSlides) {
    e.target.setAttribute('disabled', 'disabled');
  } else {
    e.target.removeAttribute('disabled');
  }
}

/**
 * Shows the previous slide on the carousel
 * @param {Event} e The event object for this function
 */
function showPreviousSlide(e) {
  const carousel = document.querySelector('.carousel');
  const carouselSlides = carousel.querySelector('.carousel-slides');
  let activeSlide = Number(carouselSlides.getAttribute('data-active-slide'));
  if (activeSlide <= 0) {
    return;
  }
  const transform = (activeSlide * 100) - 100;
  activeSlide--;
  carouselSlides.style.transform = 'translateX(-' + String(transform) + '%)';
  carouselSlides.setAttribute('data-active-slide', String(activeSlide));
  e.target.parentNode.lastElementChild.removeAttribute('disabled');
  if (activeSlide <= 0) {
    e.target.setAttribute('disabled', 'disabled');
  } else {
    e.target.removeAttribute('disabled');
  }
}

/**
 * Returns the number of carousel-slide elements in the given carousel
 * @param {HTMLElement} carousel The carousel element to check
 * @return {Number} The number of slides in the given carousel
 */
function getNumSlides(carousel) {
  return carousel.querySelectorAll('.carousel-slide').length;
}

/**
 * Looks into all carousel elements on the page and enables the right control
 * if there are more than one slides
 */
function enableAppropriateCarouselControls() {
  const carousels = document.querySelectorAll('.carousel');
  for (let i = 0; i < carousels.length; i++) {
    const carousel = carousels[i];
    const numSlides = getNumSlides(carousel);
    if (numSlides > 1) {
      const control = carousel.querySelector('.carousel-right-control');
      control.removeAttribute('disabled');
    }
  }
}

main();
