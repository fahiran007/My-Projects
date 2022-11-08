let amnt_ch = document.getElementById("amnt_ch");
let idx = document.getElementById("idx").innerText;
let amnt_valid = document.getElementById("amountvalid");
let nomoney = document.getElementById("nomoney");
let statu = document.getElementById("status");
function change_page() {
  location.href = "/Account/" + idx;
}
if (nomoney.innerText == "nomoney") {
  nomoney.innerText = "Insufficient Balance";
  nomoney.style.margin = "0.3rem auto 0 auto";
  nomoney.style.width = "90%";
  nomoney.style.color = "aqua";
  nomoney.style.display = "block";
}
if (statu.innerText == "success") {
  statu.innerText = "Congrats Withdrawal Successfull";
  statu.style.margin = "0.3rem auto 0 auto";
  statu.style.width = "90%";
  statu.style.color = "rgb(13, 248, 13)";
  statu.style.display = "block";
  setTimeout(function () {
    statu.style.display = 'none'
  },2000)
}
if (amnt_ch.innerText == "invalid") {
  amnt_ch.innerText = "Minimum withdrawal amount is ₹300rs";
  amnt_ch.style.margin = "0.3rem auto 0 auto";
  amnt_ch.style.width = "90%";
  amnt_ch.style.color = "aqua";
  amnt_ch.style.display = "block";
}
setTimeout(hide, 4000);
function hide() {
  amnt_ch.style.display = "none";
}
if (amnt_valid.innerText == "invalid") {
  amnt_valid.innerText = "Please enter valid amount";
  amnt_valid.style.margin = "0.3rem auto 0 auto";
  amnt_valid.style.width = "90%";
  amnt_valid.style.color = "aqua";
  amnt_valid.style.display = "block";
}
setTimeout(hide2, 4000);
function hide2() {
  amnt_valid.style.display = "none";
}
let with_type = document.getElementsByClassName("with_type");
let stat = document.getElementsByClassName("stat");
let amount = document.getElementsByClassName("amnt");
for (let index = 0; index < amount.length; index++) {
  let with_type = document.getElementsByClassName("with_type")[index];
  let stat = document.getElementsByClassName("stat")[index];
  let amount = document.getElementsByClassName("amnt")[index];
  if (with_type.innerText == "w") {
    amount.innerText = "-" + amount.innerText;
    amount.style.color = "red";
    with_type.innerText = "Withdrawal";
  }
  if (stat.innerText == "p") {
    stat.innerText = "Pending";
    stat.style.color = "aqua";
  }
  if (stat.innerText == "s") {
    stat.innerText = "Success";
    stat.style.color = "rgb(13, 248, 13)";
  }
}
