

const swiper = new Swiper('.swiper', {
    // Optional parameters
    speed: 400,
    autoHeigth:true,
    allowTouchMove:true,
    slidesPerView:4,
    direction: 'horizontal',
    loop: false,

    // Responsive breakpoints
    breakpoints: {
        280: {
            slidesPerView: 2,
            spaceBetween: 5
        },
        // when window width is >= 320px
        320: {
        slidesPerView: 2,
        spaceBetween: 5
        },
        // when window width is >= 480px
        480: {
        slidesPerView: 2,
        spaceBetween: 5
        },
        // when window width is >= 640px
        640: {
            slidesPerView: 3,
            spaceBetween: 40
        },
        // when window width is >= 700px
        700: {
            slidesPerView: 4,
            spaceBetween: 40
        },
        // when window width is >= 840px
        840: {
            slidesPerView: 4,
            spaceBetween: 40
        },
        // when window width is >= 1200px
        1100: {
            slidesPerView: 5,
            spaceBetween: 40

        }
    },

    // Navigation arrows
    navigation: {
        nextEl: '.next-button',
        prevEl: '.prev-button',
    },
    
});

const swiperEmpresa = new Swiper('.swiperEmpresa', {
    // Optional parameters
    speed: 400,
    autoHeigth:true,
    allowTouchMove:true,
    slidesPerView:4,
    direction: 'horizontal',
    loop: false,

    // Responsive breakpoints
    breakpoints: {
        280: {
            slidesPerView: 2,
            spaceBetween: 5
        },
        // when window width is >= 320px
        320: {
        slidesPerView: 2,
        spaceBetween: 5
        },
        // when window width is >= 480px
        480: {
        slidesPerView: 2,
        spaceBetween: 5
        },
        // when window width is >= 640px
        640: {
            slidesPerView: 3,
            spaceBetween: 270
        },
        // when window width is >= 700px
        700: {
            slidesPerView: 4,
            spaceBetween: 270
        },
        // when window width is >= 840px
        840: {
            slidesPerView: 4,
            spaceBetween: 270
        },
        // when window width is >= 1200px
        1100: {
            slidesPerView: 5,
            spaceBetween: 270

        }
    },

    // Navigation arrows
    navigation: {
        nextEl: '.next-button-empresa',
        prevEl: '.prev-button-empresa',
    },
    
});

