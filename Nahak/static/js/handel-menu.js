var Navbar = document.querySelector(".nahak-navbar");

var navbarLinks = document.querySelector(".nahak-navbar .main-navbar .menu-links");
var parentNavbarLinks = navbarLinks.parentElement;

var jobBTN = document.querySelector(".nahak-navbar .job-re");
var parentJobBTN = jobBTN.parentElement;

var toggleBox = document.querySelector(".nahak-navbar .toggle-box .main-box");

function windowResized() {
    if (window.innerWidth <= 1279) {
        toggleBox.appendChild(navbarLinks);
        toggleBox.appendChild(jobBTN);
    } else {
        parentNavbarLinks.appendChild(navbarLinks);
        parentJobBTN.appendChild(jobBTN);
    }
}

windowResized();
window.addEventListener("resize", windowResized);

//fixed navbar
window.addEventListener("scroll", function (e) {
    if (document.documentElement.scrollTop > 0) {
        Navbar.classList.add("fixed");
    } else {
        Navbar.classList.remove("fixed");
    }
});
