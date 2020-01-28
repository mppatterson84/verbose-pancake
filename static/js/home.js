console.log("Hello, World! home.js");

// const body = document.querySelector("body");
const progress = document.querySelectorAll("div.home-container");

function pageValues() {
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
    // body.style.backgroundPositionY = 0;
    progress[0].style.backgroundPositionY = `-${pageValues().scrollPosition * 5}px`;
    progress[2].style.backgroundPositionY = `-${pageValues().scrollPosition * 5 + 550}px`;
});

window.addEventListener("scroll", function () {
    // body.style.backgroundPositionY = 0;
    progress[0].style.backgroundPositionY = `-${pageValues().scrollPosition * 5}px`;
    progress[2].style.backgroundPositionY = `-${pageValues().scrollPosition * 5 + 550}px`;
});