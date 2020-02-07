console.log("Hello, World! base.js");

var hamburger = document.querySelector(".hamburger");

hamburger.addEventListener("click", function () {
    hamburger.classList.toggle("is-active");
    hamburger.classList.toggle("rubberBand");
    hamburger.classList.toggle("jello");
    doubleClickDelay();
});

//disables the hamburger button one millasecond after it is clicked
//and remains disabled for half a second preventing double clicking by the user
function doubleClickDelay() {
    setTimeout(() => {
        hamburger.disabled = true;
        hamburger.attributes
        setTimeout(() => {
            hamburger.disabled = false;
        }, 500);
    }, 1);
}