let with_type = document.getElementsByClassName("with_type");
let stat = document.getElementsByClassName("stat");
let amount = document.getElementsByClassName("amnt");
let idx = document.getElementById("idx");
for (let index = 0; index < amount.length; index++) {
  let with_type = document.getElementsByClassName("with_type")[index];
  let stat = document.getElementsByClassName("stat")[index];
  let amount = document.getElementsByClassName("amnt")[index];
  if (with_type.innerText == "w") {
    amount.innerText = "-" + amount.innerText;
    amount.classList.add("namount");
    stat.style.color = "aqua";
    with_type.innerText = "Withdrawal";
  } else if (with_type.innerText == "r") {
    amount.innerText = "+" + amount.innerText;
    amount.classList.add("pamount");
    with_type.innerText = "Received";
    stat.style.color = "rgb(13, 248, 13)";
    stat.innerText = "Success";
  }
  if (stat.innerText == "p") {
    stat.innerText = "Pending";
  }
  if (stat.innerText == "s") {
    stat.innerText = "Success";
  }
}
function go_back() {
  location.href = "/Account/" + idx.innerText;
}
