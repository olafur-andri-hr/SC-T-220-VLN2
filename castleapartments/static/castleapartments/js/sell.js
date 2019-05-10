document.getElementById('infonextlink').addEventListener('click', finishInfo);
document.getElementById('basicnextlink').addEventListener('click', finishBasic);
document.getElementById('detailnextlink').addEventListener('click', finishDetail);
document.getElementById('reviewnextlink').addEventListener('click', finishReview);
document.getElementById('basicprevlink').addEventListener('click', backToInfo);
document.getElementById('detailprevlink').addEventListener('click', finishInfo);
document.getElementById('reviewprevlink').addEventListener('click', finishBasic);

const infoDiv = document.getElementById('yourinfodiv');
const basicDiv = document.getElementById('basicdiv');
const detailDiv = document.getElementById('detaildiv');
const reviewDiv = document.getElementById('reviewdiv');
const confirmDiv = document.getElementById('confirmdiv');

/**
 * This function kicks ass
 */
function backToInfo() {
  infoDiv.className = 'current';
  basicDiv.className = 'navigationdivs';
}

/**
 * This function kicks ass
 */
function finishInfo() {
  infoDiv.className = 'finished';
  basicDiv.className = 'current';
  detailDiv.className = 'navigationdivs';
}

/**
 * This function kicks ass
 */
function finishBasic() {
  basicDiv.className = 'finished';
  detailDiv.className = 'current';
  reviewDiv.className = 'navigationdivs';
}

/**
 * This function kicks ass
 */
function finishDetail() {
  detailDiv.className = 'finished';
  reviewDiv.className = 'current';
  confirmDiv.className = 'navigationdivs';
}

/**
 * This function kicks ass
 */
function finishReview() {
  reviewDiv.className = 'finished';
  confirmDiv.className = 'current';
}
