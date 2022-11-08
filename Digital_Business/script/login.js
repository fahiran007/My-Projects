let login = document.getElementById("login_check");
if (login.innerText == 'not') {
  login.style.display = 'block'
  login.innerText = "We cannot find an account with that email/password";
}
setTimeout(hide2, 4000);
function hide2() {
  login.style.display = "none";
}