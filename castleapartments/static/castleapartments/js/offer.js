const theButton = document.getElementById('paymentnextlink');
theButton.addEventListener('click', showConfirm);

const offerAmount = document.getElementById('id_offer_amount');
const conveyance = document.getElementById('id_conveyance_date');
const creditCardNumber = document.getElementById('id_credit_card_number');
const expiry = document.getElementById('id_credit_card_expiration_date');


/**
 * This is a useless comment because I'm too lazy to do something with it
 */
function showConfirm() {
  const amounttd = document.getElementById('amounttd');
  const conveyancetd = document.getElementById('conveyancetd');
  const creditCardtd = document.getElementById('creditcardtd');
  const ccExpirytd = document.getElementById('ccexpirytd');

  amounttd.textContent = offerAmount.value;
  conveyancetd.textContent = conveyance.value;
  creditCardtd.textContent = creditCardNumber.value;
  ccExpirytd.textContent = expiry.value;
}
