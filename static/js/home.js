console.log("Hello, World! home.js");

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
    progress[0].style.backgroundPositionY = `-${pageValues().scrollPosition * 3}px`;
    progress[1].style.backgroundPositionY = `${pageValues().scrollPosition * 3 - 200}px`;
    progress[2].style.backgroundPositionY = `-${pageValues().scrollPosition * 3 - 150}px`;
});

window.addEventListener("scroll", function () {
    progress[0].style.backgroundPositionY = `-${pageValues().scrollPosition * 3}px`;
    progress[1].style.backgroundPositionY = `${pageValues().scrollPosition * 3 - 200}px`;
    progress[2].style.backgroundPositionY = `-${pageValues().scrollPosition * 3 - 150}px`;
});