const theButton = document.getElementById('paymentnextlink');
theButton.addEventListener('click', showConfirm);

const offerAmount = document.getElementById('id_offer_amount');
const conveyanceMonth = document.getElementById('id_conveyance_date_month');
const conveyanceDay = document.getElementById('id_conveyance_date_day');
const conveyanceYear = document.getElementById('id_conveyance_date_year');
const creditCardNumber = document.getElementById('id_credit_card_number');
const expiryMonth = document.getElementById(
    'id_credit_card_expiration_date_month');
const expiryDay = document.getElementById('id_credit_card_expiration_date_day');
const expiryYear = document.getElementById(
    'id_credit_card_expiration_date_year');


/**
 * This is a useless comment because I'm too lazy to do something with it
 */
function showConfirm() {
  console.log('You absolute wanker!');
  const amounttd = document.getElementById('amounttd');
  const conveyancetd = document.getElementById('conveyancetd');
  const creditCardtd = document.getElementById('creditcardtd');
  const ccExpirytd = document.getElementById('ccexpirytd');

  amounttd.textContent = offerAmount.value;
  conveyancetd.textContent = conveyanceMonth.value.toString() + '/'
    + conveyanceDay.value.toString() + '/' + conveyanceYear.value.toString();
  creditCardtd.textContent = creditCardNumber.value;
  ccExpirytd.textContent = expiryMonth.value.toString() + '/' +
    expiryDay.value.toString() + '/' + expiryYear.value.toString();
}
