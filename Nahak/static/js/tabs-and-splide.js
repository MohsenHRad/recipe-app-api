document.addEventListener("DOMContentLoaded", () => {
    var consultantsSwiper = new Swiper(".consultants-swiper", {
        observer: true,
        observeParents: true,
        slidesPerView: 4,
        spaceBetween: 21,
        speed: 600,
        watchSlidesProgress: true,
        watchSlidesVisibility: true,
        navigation: {
            nextEl: ".consultants-swiper-prev",
            prevEl: ".consultants-swiper-next",
        },
        breakpoints: {
            1200: {
                slidesPerView: 4,
                spaceBetween: 21,
            },
            992: {
                slidesPerView: 3,
                spaceBetween: 21,
            },
            768: {
                slidesPerView: 2,
                spaceBetween: 21,
            },
            576: {
                slidesPerView: 2,
                spaceBetween: 21,
            },
            0: {
                slidesPerView: 1,
                spaceBetween: 15,
            },
        },
    });

    var NESSwiper = new Swiper(".NES-swiper", {
        observer: true,
        observeParents: true,
        slidesPerView: 2,
        spaceBetween: 21,
        speed: 600,
        watchSlidesProgress: true,
        watchSlidesVisibility: true,
        breakpoints: {
            1200: {
                slidesPerView: 2,
                spaceBetween: 21,
            },
            992: {
                slidesPerView: 2,
                spaceBetween: 21,
            },
            768: {
                slidesPerView: 1,
                spaceBetween: 21,
            },
            576: {
                slidesPerView: 2,
                spaceBetween: 21,
            },
            0: {
                slidesPerView: 1,
                spaceBetween: 30,
            },
        },
    });

    var NESSwiper2 = new Swiper(".NES-swiper-2", {
        autoplay: {
            delay: 5000,
        },
        observer: true,
        observeParents: true,
        slidesPerView: 1,
        spaceBetween: 21,
        speed: 600,
        watchSlidesProgress: true,
        watchSlidesVisibility: true,
        pagination: {
            el: ".NES-swiper-2-pagination",
            clickable: true,
            renderBullet: function (index, className) {
                return '<span class="' + className + '"></span>';
            },
        },
        breakpoints: {
            1200: {
                slidesPerView: 1,
                spaceBetween: 21,
            },
            576: {
                slidesPerView: 1,
                spaceBetween: 21,
            },
            0: {
                slidesPerView: 1,
                spaceBetween: 21,
            },
        },
    });

    var symbolsSwiper = new Swiper(".symbols-swiper", {
        observer: true,
        observeParents: true,
        slidesPerView: 1,
        spaceBetween: 21,
        autoplay: {
            delay: 3000,
        },
        watchSlidesProgress: true,
        watchSlidesVisibility: true,
        pagination: {
            el: ".symbols-pagination",
            clickable: true,
            renderBullet: function (index, className) {
                return '<span class="' + className + '"></span>';
            },
        },
        breakpoints: {
            992: {
                slidesPerView: 1,
                spaceBetween: 21,
            },
            0: {
                slidesPerView: 2,
                spaceBetween: 21,
            },
        },
    });

    var problemsSwiper = new Swiper(".problems-sw", {
        observer: true,
        observeParents: true,
        slidesPerView: 1,
        direction: "vertical",
        speed: 1500,
        allowTouchMove: false,
        watchSlidesProgress: true,
        watchSlidesVisibility: true,
        autoplay: {
            delay: 4500,
        },
        on: {
            slideChange: function (e) {
                let parentSW = this.$el[0].parentNode;
                if (this.slides.length - 1 === this.activeIndex) {
                    parentSW.classList.add("reached-end");
                } else {
                    parentSW.classList.remove("reached-end");
                }
            },
        },
    });

    var gallerySwiper = new Swiper(".gallery-sw", {
        effect: "fade",
        fadeEffect: {
            crossFade: true,
        },
        observer: true,
        observeParents: true,
        slidesPerView: 1,
        speed: 600,
        spaceBetween: 21,
        autoplay: {
            delay: 6000,
        },
        watchSlidesProgress: true,
        watchSlidesVisibility: true,
        on: {
            init: function () {
                this.slides.forEach((slide) => {
                    slide.appendChild(slide.querySelector("img").cloneNode(true));
                });
            },
        },
        pagination: {
            el: ".gallery-pagination",
            clickable: true,
            renderBullet: function (index, className) {
                return '<span class="' + className + '"></span>';
            },
        },
        breakpoints: {
            1200: {
                slidesPerView: 1,
                spaceBetween: 21,
            },
            576: {
                slidesPerView: 1,
                spaceBetween: 21,
            },
            0: {
                slidesPerView: 1,
                spaceBetween: 0,
            },
        },
    });

    var jobsSwiper = new Swiper(".jobs-sw", {
        effect: "creative",
        creativeEffect: {
            prev: {
                // will set `translateZ(-400px)` on previous slides
                translate: ["100%", 0, -1000],
            },
            next: {
                // will set `translateX(100%)` on next slides
                translate: ["-100%", 0, -1000],
            },
        },
        slidesPerView: 1,
        speed: 800,
        spaceBetween: 21,
        // autoplay: {
        //     delay: 5000,
        // },
        watchSlidesProgress: true,
        watchSlidesVisibility: true,
        on: {
            init: function () {
                this.slides.forEach((slide) => {
                    let imgWrapper = slide.querySelector(".img-wrapper");
                    let imgCopy = imgWrapper.querySelector("img").cloneNode(true);
                    imgWrapper.appendChild(imgCopy);
                });
            },
        },
        pagination: {
            el: ".jobs-pagination",
            clickable: true,
            renderBullet: function (index, className) {
                return '<span class="' + className + '"></span>';
            },
        },
        breakpoints: {
            1200: {
                slidesPerView: 1,
                spaceBetween: 21,
            },
            576: {
                slidesPerView: 1,
                spaceBetween: 21,
            },
            0: {
                slidesPerView: 1,
                spaceBetween: 0,
            },
        },
    });
});
