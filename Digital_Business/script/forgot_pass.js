let idx = document.getElementById("idx").innerText;
let stat = document.getElementById("status");
let pas_stat = document.getElementById("pas_stat");
let changed = document.getElementById("changed");
if (changed.innerText == "changed") {
  changed.classList.remove("dis-none");
  changed.innerText = "Your password was suucessfully changed";
  changed.style.textAlign = "center";
}
if (stat.innerText == "notmatch") {
  stat.innerText = "New Passwords not match";
  stat.classList.remove("dis-none");
}
if (stat.innerText == "short") {
  stat.innerText = "Your New Password is too short";
  stat.classList.remove("dis-none");
}
if (pas_stat.innerText == "wrong") {
  pas_stat.innerText = "Your old password is wrong";
}
function go_back() {
  location.href = "/Account/" + idx;
}
