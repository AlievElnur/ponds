if (performance.navigation.type === performance.navigation.TYPE_RELOAD) {
  window.location = "";
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
      mousewheel: true,
})

new Swiper('.slider_3', {
    speed: 800,
    spaceBetween: 1,
    autoplay: {
      delay: 5000,
      disableOnInteraction: false,
  },
    pagination: {
      el: '.swiper-pagination',
      type: 'bullets',
    },
    navigation: {
        nextEl: '.swiper-button-next',
        prevEl: '.swiper-button-prev',
      },
      scrollbar: {
        el: '.swiper-scrollbar',
      },
      loop: true,
      mousewheel: true,
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
