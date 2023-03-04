new Swiper('.slider', {
    direction: 'vertical',
    speed: 800,
    mousewheel: true,
    spaceBetween: 1,
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