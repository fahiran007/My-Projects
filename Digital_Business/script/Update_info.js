let idx = document.getElementById("idx").innerText;
function go_back() {
  location.href = "/Account/" + idx;
}
let stat = document.getElementById("status");
if (stat.innerText == "invalid") {
  stat.innerText = "Email address is already exist";
  stat.style.display = "block";
}
setTimeout(hide, 5000);
function hide() {
  stat.style.display = "none";
}
