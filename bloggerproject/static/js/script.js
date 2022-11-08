let time = document.getElementsByClassName("timing")[0];
let scr_info = document.getElementsByClassName("scroll-info")[0];
let con_btn = document.getElementsByClassName("continue-btn")[0];
t = 4;
timer();
function timer() {
  const myinterval = setInterval(() => {
    if (t < 9) {
      t = t - 1;
      tt = "0" + t;
    } else {
      console.log(t);
      t = t - 1;
      tt = t;
    }
    console.log(t);
    time.innerHTML = tt;
    if (t == 0) {
      scr_info.classList.remove("d-none");
      con_btn.classList.remove("d-none");
      clearInterval(myinterval);
    }
  }, 1000);
}
function circle(idx) {
  let link_img = document.getElementsByClassName("link-img")[idx];
  let card = document.getElementsByClassName("tasks")[idx];
  let card_next = document.getElementsByClassName("tasks")[idx+1];
  let link_img_next = document.getElementsByClassName("link-img")[idx + 1];
  let task_title = document.getElementsByClassName("title-task")[idx + 1];
  let progress = document.getElementsByClassName("spinner-border")[idx];
  link_img.classList.add("d-none");
  progress.classList.remove("d-none");
  setTimeout(function delay() {
    link_img.classList.remove("d-none");
    link_img.src = "/static/media/059-success.png";
    progress.classList.add("d-none");
    card.classList.toggle("disabled")
    if (idx == 3) {
      link_img_next.src = "/static/media/377-unlocked.png";
      card_next.classList.toggle("disabled");
      task_title.innerHTML = "Final Destination Opened";
    } else {
      link_img_next.src = "/static/media/287-link.png";
      card_next.classList.toggle("disabled");
    }
  }, 300);
}
