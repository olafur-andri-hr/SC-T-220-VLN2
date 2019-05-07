document.getElementById("hamburger").addEventListener("click", hamburger);
document.getElementById("accountdiv").addEventListener("click", sidebardropdown);

function sidebardropdown() {
  document.getElementById("sidebar").classList.toggle("active");
}

function hamburger() {
  navbar = document.getElementById("dropdownnav");
  if (navbar.className === "active") {
    navbar.className = "notActive";
  }
  else {
    navbar.className = "active";
  }
}