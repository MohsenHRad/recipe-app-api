var ParentMyVideo = document.querySelector(".about-video");
var myVideo = document.querySelector(".about-video video");
var btnElement = document.querySelector(".about-video .parent-icon");

btnElement.addEventListener("click", function () {
    if (myVideo.paused) {
        myVideo.play();
        myVideo.controls = true;

        if (typeof btnElement.classList !== "undefined" || btnElement.classList !== null) {
            ParentMyVideo.classList.add("active-video");
        }
    }
});
