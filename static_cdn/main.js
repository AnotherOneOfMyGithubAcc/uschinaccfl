const about = document.querySelector("li[data-data-id='dataItem-jfporqwm']");
const about_ul = about.children[1];

about.addEventListener("mouseover", () => {
  about_ul.style.visibility = "visible";
});
about.addEventListener("mouseout", () => {
  about_ul.style.visibility = "hidden";
});

const events = document.querySelector("li[data-data-id='dataItem-jfvp24k3']");
const events_ul = events.children[1];

events.addEventListener("mouseover", () => {
  events_ul.style.visibility = "visible";
});
events.addEventListener("mouseout", () => {
  events_ul.style.visibility = "hidden";
});

const resources = document.querySelector(
  "li[data-data-id='dataItem-jgmm4ayh']"
);
const resources_ul = resources.children[1];

resources.addEventListener("mouseover", () => {
  resources_ul.style.visibility = "visible";
});
resources.addEventListener("mouseout", () => {
  resources_ul.style.visibility = "hidden";
});



let slideIndex = 0;

function slideShow() {
  let i;
  let slides = document.getElementsByClassName("mySlides");
  for (i = 0; i < slides.length; i++) {
    slides[i].style.display = "none";  
  }

  slideIndex++;
  if (slideIndex > slides.length) {slideIndex = 1}    

  slides[slideIndex-1].style.display = "block";  
  setTimeout(slideShow(), 2500)
}