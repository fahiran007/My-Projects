let idx = document.getElementById("idx").innerText;
let replies = document.getElementsByClassName("massage-box-full")[0];
let norep = document.getElementById("norep");
let inv = document.getElementById("inv");
if (replies.innerText == "") {
  norep.style.display = "block";
}
if (inv.innerText == 'invalid') {
  inv.innerText = 'Write minimum 20 Character'
  inv.style.margin = '0.3rem auto 0.3rem auto'
  inv.style.display = 'block'
  inv.style.width = '90vw'
  inv.style.color = 'aqua'
  setTimeout(function () {
    inv.style.display = 'none'
  },2000)
}
else {
  inv.style.display = 'none'
}
function go_back() {
  location.href = "/Account/" + idx;
}
function change_location() {
  document.getElementById("textareas").value = ''
}
