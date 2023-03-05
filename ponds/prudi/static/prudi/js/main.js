if (performance.navigation.type === performance.navigation.TYPE_RELOAD) {
  window.location = "http://127.0.0.1:8000";
}

new Swiper('.slider', {
    speed: 800,
    // mousewheel: true,
    // spaceBetween: 1,
    allowTouchMove: false,
})


new Swiper('.slider_2', {
    speed: 800,
    spaceBetween: 1,
    navigation: {
        nextEl: '.swiper-button-next',
        prevEl: '.swiper-button-prev',
      },
      scrollbar: {
        el: '.swiper-scrollbar',
      },
      loop: true,
})


let element_1 = document.getElementById("same");

function scrollToSame() {
  element_1.scrollIntoView({behavior: "smooth", block: "start"});
}

let element_2 = document.getElementById("price");

function scrollToPrice() {
  element_2.scrollIntoView({behavior: "smooth", block: "start"});
}

let element_3 = document.getElementById("clear");

function scrollToClear() {
  element_3.scrollIntoView({behavior: "smooth", block: "start"});
}

let element_4 = document.getElementById("main_menu");

function scrollToMain() {
  element_4.scrollIntoView({behavior: "smooth", block: "start"});
}


localStorage.setItem('same', window.pageYOffset);

window.onload = function() {
  var scrollPosition = localStorage.getItem('same');
  if (scrollPosition !== null) {
    window.scrollTo(0, scrollPosition);
  }
}

window.onbeforeunload = function () {
  window.scrollTo(0, 0);
}
