document.addEventListener('DOMContentLoaded', function(event) {
  const options = document.querySelectorAll('#id_country option');
  options.forEach((element) => {
    const image = document.createElement('img');
    image.src = `/static/flags/${element.value}.gif`;
    element.appendChild(image);
  });
});
