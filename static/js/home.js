console.log("Hello, World! home.js");

const section = document.querySelectorAll("div.home-container");

function scrolled() {
    var cHeight = document.body.clientHeight;
    var wHeight = window.innerHeight;
    var scrollOffset = window.pageYOffset;
    var onePercentOfHeight = (cHeight - wHeight) / 100;
    var scrollPosition = scrollOffset / onePercentOfHeight;

    return {
        "scrollPosition": scrollPosition,
        "cHeight": cHeight,
        "wHeight": wHeight,
        "scrollOffset": scrollOffset
    }
}

window.addEventListener("load", function () {
    section[0].style.backgroundPositionY = `-${scrolled().scrollPosition * 3}px`;
    section[1].style.backgroundPositionY = `${scrolled().scrollPosition * 3 - 200}px`;
    section[2].style.backgroundPositionY = `-${scrolled().scrollPosition * 3 - 150}px`;

    function scrollTo(hash) {
        location.hash = "#" + hash;
    }
    scrollTo("home");
});

window.addEventListener("scroll", function () {
    section[0].style.backgroundPositionY = `-${scrolled().scrollPosition * 3}px`;
    section[1].style.backgroundPositionY = `${scrolled().scrollPosition * 3 - 200}px`;
    section[2].style.backgroundPositionY = `-${scrolled().scrollPosition * 3 - 150}px`;
});

// zenscroll settings
var defaultDuration = 2000 // ms
var edgeOffset = 0 // px
zenscroll.setup(defaultDuration, edgeOffset)