// Globals
const acceptConfirmMessage = document.getElementById('accept_pop_up');
const declineConfirmMessage = document.getElementById('decline_pop_up');

/**
 * The function that is always run when the website is loaded
 */
function main() {
  addEventListeners();
}

/**
 * Adds all necessary event listeners to the various elements on the page
 */
function addEventListeners() {
  const acceptOfferButton = document.getElementById('accept_offer_button');
  const declineOfferButton = document.getElementById('decline_offer_button');

  acceptOfferButton.addEventListener('click', showAcceptConfirmMessage);
  declineOfferButton.addEventListener('click', showDeclineConfirmMessage);
}

/**
 * Shows a confirmation message when the user clicks the 'accept offer' button
 * @param {Event} e The click event object
 */
function showAcceptConfirmMessage(e) {
  const cancelButton = acceptConfirmMessage.querySelector('.cancel');

  acceptConfirmMessage.classList.add('show');
  cancelButton.addEventListener('click', closeAcceptConfirmMessage);
}

/**
 * Closes the accept confirmation message
 * @param {Event} e The event object for this click event handler
 */
function closeAcceptConfirmMessage(e) {
  e.target.removeEventListener('click', closeAcceptConfirmMessage);
  acceptConfirmMessage.classList.remove('show');
}

/**
 * Shows a confirmation message when the user clicks the 'decline offer' button
 * @param {Event} e The click event object
 */
function showDeclineConfirmMessage(e) {
  const cancelButton = declineConfirmMessage.querySelector('.cancel');

  declineConfirmMessage.classList.add('show');
  cancelButton.addEventListener('click', closeDeclineConfirmMessage);
}

/**
 * Closes the decline confirm message
 * @param {Event} e The event object for this click event handler
 */
function closeDeclineConfirmMessage(e) {
  e.target.removeEventListener('click', closeDeclineConfirmMessage);
  declineConfirmMessage.classList.remove('show');
}

main();
