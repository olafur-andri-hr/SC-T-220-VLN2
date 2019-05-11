document.getElementById("detailnextlink").addEventListener("click", showReview);

const countryInput = document.getElementById("countryInput");
const zipCodeInput = document.getElementById("id_zip_code");
const townInput = document.getElementById("id_town");
const aptNumberInput = document.getElementById("aptNumberInput");
const numOfRoomsInput = document.getElementById("id_num_of_rooms");
const numOfToiletsInput = document.getElementById("id_num_of_toilets");
const sizeInput = document.getElementById("id_size");
const typeInput = document.getElementById("id_type");
const yearBuiltInput = document.getElementById("yearBuiltInput");
const garageInput = document.getElementById("garageInput");
const appraisalInput = document.getElementById("id_appraisal");
const descriptionInput = document.getElementById("descriptionInput");
const aptNumbertd = document.getElementById('aptNumbertd');

aptNumbertd.textContent = aptNumberInput.value;

/**
 * This is so me
 */
function showReview() {
  const countryInput = document.getElementById("id_country");
  const zipCodeInput = document.getElementById("zipCodeInput");
  const townInput = document.getElementById("townInput");
  const aptNumberInput = document.getElementById("aptNumberInput");
  const numOfRoomsInput = document.getElementById("numOfRoomsInput");
  const numOfToiletsInput = document.getElementById("numOfToiletsInput");
  const sizeInput = document.getElementById("sizeInput");
  const typeInput = document.getElementById("typeInput");
  const yearBuiltInput = document.getElementById("yearBuiltInput");
  const garageInput = document.getElementById("garageInput");
  const appraisalInput = document.getElementById("appraisalInput");
  const descriptionInput = document.getElementById("descriptionInput");
  const aptNumbertd = document.getElementById('aptNumbertd');
  const countrytd = document.getElementById('countrytd');

  aptNumbertd.textContent = aptNumberInput.value;
  countrytd.textContent = countryInput.value;


}