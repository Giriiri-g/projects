for (let i = 0; i <= 100; i++) {
  setTimeout(() => {
    const div = document.querySelector('.loadertext');
    const loader = document.querySelector('.loaderbar');
    loader.style.width = i * 5 + "px";
    div.textContent = i + '%';
    if (i === 100) {
      setTimeout(() => {
        load();
      }, 500);
    }
  }, i * 30);
}

function load() {
  const loader = document.querySelector('.loader');
  const wrapper = document.querySelector('.wrapper');
  loader.classList.add("fade");
  wrapper.classList.add("fadein");
  setTimeout(() => { loader.style.display = 'none'; }, 500);
  setTimeout(() => { wrapper.style.display = 'flex'; }, 500);
}

const theme = document.getElementById('theme');

theme.addEventListener('click', function () {
  document.body.classList.toggle('light');
  if (document.body.classList.contains('light')) {
    theme.innerHTML = '■&nbsp;LIGHT&#9;□&nbsp;DARK';
  } else {
    theme.innerHTML = '□&nbsp;LIGHT&#9;■&nbsp;DARK';
  }
});

const menuItems = document.querySelectorAll(".menua");

menuItems.forEach(function(item) {
  item.addEventListener("click", function(e) {
    e.preventDefault();
    const target = this.getAttribute("data-target");

    document.querySelectorAll(".intro, .education, .experience, .contact").forEach(function(element) {
      element.style.display = "none";
    });

    document.querySelector("." + target).style.display = "flex";
  });
});


let innercursor = document.querySelector(".dot");
let outercursor = document.querySelector(".circle");

document.addEventListener("mousemove", movecursor);

function movecursor(e) {
  let x = e.clientX;
  let y = e.clientY;
  innercursor.style.left = `${x}px`;
  innercursor.style.top = `${y}px`;
  outercursor.style.left = `${x}px`;
  outercursor.style.top = `${y}px`;
}

let hovers = Array.from(document.getElementsByClassName("hoverable"));
hovers.forEach((i) =>{
  i.addEventListener("mouseover", ()=>{
    innercursor.classList.add("grow");
    outercursor.classList.add("grow");
  });
  i.addEventListener("mouseleave", ()=>{
    innercursor.classList.remove("grow");
    outercursor.classList.remove("grow");
  });
});