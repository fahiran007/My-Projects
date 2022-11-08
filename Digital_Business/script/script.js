let profile_icon = document.getElementById("profile-picture");
let idx = document.getElementById("idx").innerText
profile_icon.addEventListener("click", function () {
  location.href = "/Account/"+idx;
});