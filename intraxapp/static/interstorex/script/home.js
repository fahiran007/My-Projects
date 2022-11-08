const barbtn = document.getElementById("barbtn");
const boxes = document.getElementById("sidebar");
let body = document.getElementsByTagName("body")[0]
function sidemenuopenandclose() {
  boxes.classList.toggle("open");
    body.classList.toggle("overflow")
}

