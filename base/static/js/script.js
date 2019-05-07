document.getElementById("dropdownnav").addEventListener("click", hamburger);
document.getElementById("sidebar").addEventListener("click", sidebardropdown);

function sidebardropdown() {
  document.getElementById("sidebar").classList.toggle("active");
  console.log("Hi");
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