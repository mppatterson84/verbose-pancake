console.log('Hello, World! base.js');

var hamburger = document.querySelector('.hamburger');

hamburger.addEventListener('click', function () {
    hamburger.classList.toggle('is-active');
    hamburger.classList.toggle('animate__rubberBand');
    hamburger.classList.toggle('animate__jello');
    doubleClickDelay();
});

//disables the hamburger button one millasecond after it is clicked
//and remains disabled for half a second preventing double clicking by the user
function doubleClickDelay() {
    setTimeout(() => {
        hamburger.disabled = true;
        setTimeout(() => {
            hamburger.disabled = false;
        }, 500);
    }, 1);
}

// Hide the navbar when scrolling down.
// Show the navbar when scrolling up.
var a = window.pageYOffset; // 'a' is assigned an initial value
var $nav = $('nav.navbar');
$(document).scroll(() => {
    var b = a; // 'b' is assigned the value of 'a' to hold
    console.log(`Old Number: ${b}`);
    a = window.pageYOffset; // 'a' is assigned a new value
    console.log(`New Number: ${a}`);

    setTimeout(() => {
        if (pageYOffset >= 10) {
            // show navbar if 'a' is less than 'b'
            $nav.toggleClass('animate__slideInDown', a <= b);
            // hide the navbar if 'a' is greater than 'b'
            $nav.toggleClass('animate__slideOutUp', a > b);
        } else {
            $nav.removeClass('animate__slideOutUp').removeClass(
                'animate__slideInDown'
            );
        }
    }, 500);
});
