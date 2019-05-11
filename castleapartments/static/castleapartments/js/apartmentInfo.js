/**
 * The function that is always run when the file is loaded
 */
function main() {
  addEventListeners();
  enableAppropriateCarouselControls();
  activateFirstCarouselIndicator();
}

/**
 * Adds all necessary event listeners to the page
 */
function addEventListeners() {
  const carouselRights =
    document.querySelectorAll('.carousel-controls .carousel-right-control');
  const carouselLefts =
    document.querySelectorAll('.carousel-controls .carousel-left-control');
  const carouselIndicators =
    document.querySelectorAll('.carousel-indicators .carousel-indicator');

  addManyListeners(carouselRights, 'click', showNextSlide);
  addManyListeners(carouselLefts, 'click', showPreviousSlide);
  addManyListeners(carouselIndicators, 'click', showSlide);
  addManyListeners(carouselIndicators, 'mouseover', indicatorExpand);
  addManyListeners(carouselIndicators, 'mouseout', indicatorShrink);
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
  const carousel = e.target.parentNode.parentNode;
  const carouselContainer = carousel.parentNode;
  const carouselSlides = carousel.querySelector('.carousel .carousel-slides');
  const numSlides = getNumSlides(carousel);
  let activeSlide = Number(carouselSlides.getAttribute('data-active-slide'));
  if (activeSlide + 1 >= numSlides) {
    return;
  }
  const transform = 100 + (activeSlide * 100);
  const oldIndicator =
    carouselContainer.querySelector(
        '.carousel-indicator.active'
    );
  oldIndicator.classList.remove('active');
  activeSlide++;
  const newIndicator =
      carouselContainer.querySelector(
          '.carousel-indicator[data-indicator-num="' +
          String(activeSlide + 1) + '"]'
      );
  newIndicator.classList.add('active');
  carouselSlides.style.transform = 'translateX(-' + String(transform) + '%)';
  carouselSlides.setAttribute('data-active-slide', String(activeSlide));
  e.target.parentNode.firstElementChild.removeAttribute('disabled');
  if (activeSlide + 1 >= numSlides) {
    e.target.setAttribute('disabled', 'disabled');
  } else {
    e.target.removeAttribute('disabled');
  }

  newIndicator.scrollIntoView(false);
}

/**
 * Shows the previous slide on the carousel
 * @param {Event} e The event object for this function
 */
function showPreviousSlide(e) {
  const carousel = e.target.parentNode.parentNode;
  const carouselContainer = carousel.parentNode;
  const carouselSlides = carousel.querySelector('.carousel-slides');
  let activeSlide = Number(carouselSlides.getAttribute('data-active-slide'));
  if (activeSlide <= 0) {
    return;
  }
  const transform = (activeSlide * 100) - 100;
  const oldIndicator =
    carouselContainer.querySelector('.carousel-indicator.active');
  oldIndicator.classList.remove('active');
  activeSlide--;
  const newIndicator =
    carouselContainer.querySelector(
        '.carousel-indicator[data-indicator-num="' +
        String(activeSlide + 1) + '"]'
    );
  newIndicator.classList.add('active');
  carouselSlides.style.transform = 'translateX(-' + String(transform) + '%)';
  carouselSlides.setAttribute('data-active-slide', String(activeSlide));
  e.target.parentNode.lastElementChild.removeAttribute('disabled');
  if (activeSlide <= 0) {
    e.target.setAttribute('disabled', 'disabled');
  } else {
    e.target.removeAttribute('disabled');
  }

  // Scroll the indicator into view
  newIndicator.scrollIntoView(false);
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
 * if there are more than one slides in said carousel
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

/**
 * Sets the first .carousel-indicator element of every .carousel element to
 * active
 */
function activateFirstCarouselIndicator() {
  const carouselContainers = document.querySelectorAll('.carousel-container');
  for (let i = 0; i < carouselContainers.length; i++) {
    const carouselContainer = carouselContainers[i];
    carouselContainer
        .querySelector('.carousel-indicator')
        .classList.add('active');
  }
}

/**
 * Shows the appropriate slide when a carousel indicator is clicked
 * @param {Event} e The event object for this event handler
 */
function showSlide(e) {
  // Prevent relocation with the link
  e.preventDefault();

  // Do nothing if the indicator is already active
  const indicator = e.target.parentNode;
  if (indicator.classList.contains('active')) {
    return;
  }

  // Switch the active indicator
  const indicators = indicator.parentNode;
  const oldIndicator = indicators.querySelector('.carousel-indicator.active');
  oldIndicator.classList.remove('active');
  indicator.classList.add('active');

  // Transform to correct slide
  const slideNumber = Number(indicator.getAttribute('data-indicator-num')) - 1;
  const carouselContainer = indicators.parentNode;
  const carouselSlides = carouselContainer.querySelector('.carousel-slides');
  const transform = String(slideNumber * 100 * -1);
  carouselSlides.style.transform = 'translateX(' + transform + '%)';
  carouselSlides.setAttribute('data-active-slide', String(slideNumber));

  // Update visibility of carousel controls
  const carousel = carouselContainer.querySelector('.carousel');
  const leftControl = carousel.querySelector('.carousel-left-control');
  const rightControl = carousel.querySelector('.carousel-right-control');
  const numSlides = getNumSlides(carousel);
  if (slideNumber + 1 >= numSlides) {
    leftControl.removeAttribute('disabled');
    rightControl.setAttribute('disabled', 'disabled');
  } else if (slideNumber <= 0) {
    leftControl.setAttribute('disabled', 'disabled');
    rightControl.removeAttribute('disabled');
  } else {
    leftControl.removeAttribute('disabled');
    rightControl.removeAttribute('disabled');
  }

  // Scroll the indicator into view
  indicator.scrollIntoView(false);
}

/**
 * Expands a .carousel-indicator element when the user hovers over it
 * @param {Event} e The event object for this event handler
 */
function indicatorExpand(e) {
  e.target.parentNode.classList.add('hover');
}

/**
 * Shrinks a .carousel-indicator element when the user moves the cursor away
 * from it
 * @param {Event} e The event object for this event handler
 */
function indicatorShrink(e) {
  e.target.parentNode.classList.remove('hover');
}

main();
