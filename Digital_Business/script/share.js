let idx = document.getElementById("idx");
let button = document.getElementById("Copy");
let text = document.getElementById("text");
let copied = document.getElementById("copy-alert");

function copy_text() {
    copied.style.display = "block";
    text.select()
    document.execCommand("Copy")
    setTimeout(function () {
        copied.style.display = 'none'
    },1500)
}
function go_back() {
  location.href = "/Account/" + idx.innerText;
}
