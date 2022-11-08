let sts = document.getElementById("sts");
let pass_check = document.getElementById("pass_check");
let pass_len = document.getElementById("len");
let refer = document.getElementById("refer");

if (refer.innerText == 'invalid') {
refer.innerText = "Referral code is invalid";
refer.style.color = "aqua";
refer.style.fontWeight = "bold";
  refer.style.display = "block";
  setTimeout(function () {
    refer.style.display = 'none'
  },3000)
}
if (sts.innerText == "invalid") {
  sts.innerText = "The email address is already used";
  sts.style.color = "aqua";
  sts.style.fontWeight = "bold";
  sts.style.display = "block";
} else {
  sts.style.display = "none";
}
if (pass_check.innerText == "notmatch") {
  pass_check.innerText = "Password Not Match";
  pass_check.style.display = "block";
  pass_check.style.color = "aqua";
  pass_check.style.fontWeight = "bold";
  pass_check.style.margin = "0.7rem 0 0.7rem 0";
}
if (pass_len.innerText == 'too') {
  pass_len.style.display = 'block'
  pass_len.style.color = "aqua";
  pass_len.style.fontWeight = "bold";
  pass_len.innerText = 'Your password is too short'
}
else {
  pass_len.style.display = 'none'
}
function change_page() {
  location.href = '/userlogin'
}