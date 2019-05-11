document.getElementById('detailnextlink').addEventListener('click', showReview);

/**
 * This is so me
 */
function showReview() {
  const countryInput = document.getElementById('id_country');
  const zipCodeInput = document.getElementById('id_zip_code');
  const townInput = document.getElementById('id_town');
  const aptNumberInput = document.getElementById('aptNumberInput');
  const numOfRoomsInput = document.getElementById('id_num_of_rooms');
  const numOfToiletsInput = document.getElementById('id_num_of_toilets');
  const sizeInput = document.getElementById('id_size');
  const typeInput = document.getElementById('id_type');
  const yearBuiltInput = document.getElementById('id_year_built');
  const garageInput = document.getElementById('id_garage');
  const appraisalInput = document.getElementById('id_appraisal');
  const descriptionInput = document.getElementById('descriptionInput');
  const addressInput = document.getElementById('addressInput');

  const countrytd = document.getElementById('countrytd');
  const zipCodetd = document.getElementById('zipcodetd');
  const towntd = document.getElementById('towntd');
  const aptNumbertd = document.getElementById('aptnumbertd');
  const numOfRoomstd = document.getElementById('numofroomstd');
  const numOfToiletstd = document.getElementById('numoftoiletstd');
  const sizetd = document.getElementById('sizetd');
  const typetd = document.getElementById('typetd');
  const yearBuilttd = document.getElementById('yearbuilttd');
  const garagetd = document.getElementById('garagetd');
  const appraisaltd = document.getElementById('appraisaltd');
  const description = document.getElementById('descriptiontext');
  const addressHeader = document.getElementById('addressheader');

  aptNumbertd.textContent = aptNumberInput.value;
  countrytd.textContent = countryInput.value;
  zipCodetd.textContent = zipCodeInput.value;
  towntd.textContent = townInput.value;
  numOfRoomstd.textContent = numOfRoomsInput.value;
  numOfToiletstd.textContent = numOfToiletsInput.value;
  sizetd.textContent = sizeInput.value;
  typetd.textContent = typeInput.options[typeInput.selectedIndex].text;
  yearBuilttd.textContent = yearBuiltInput.value;
  appraisaltd.textContent = appraisalInput.value;
  description.textContent = descriptionInput.value;
  addressHeader.textContent = addressInput.value;
  garagetd.textContent = garageInput.value;

  if (garageInput.checked === true) {
    garagetd.textContent = 'Yes';
  } else {
    garagetd.textContent = 'No';
  }
}
