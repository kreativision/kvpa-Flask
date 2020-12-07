// marks the active button - needs a lot of tweaking if multiple pages are involved - 
// this would work with single page only.
function activate(btn) {
    var target = document.querySelector(`#${btn}`);
    var navBtns = document.querySelectorAll('.nav-wrapper a.btn-flat');
    navBtns.forEach(nav => {
        if (nav === target) {
            nav.classList.add('active');
        } else {
            nav.classList.remove('active');
        }
    });
}

// function to initialize the sidenav for mobile devices
var sideNav;
document.addEventListener('DOMContentLoaded', function () {
    var elems = document.querySelectorAll('.sidenav');
    this.sideNav = M.Sidenav.init(elems, {});
});


// ================NavBar Manipulator Block================
const callback = (entries, observer) => {
    const entry = entries[0];
    const { intersectionRatio, isIntersecting } = entry;
    // console.log(intersectionRatio, isIntersecting);
    // toggle class depending on if content div intersects with viewport
    const navBar = document.querySelector('.nav-wrapper');
    navBar.classList.toggle('solid-nav', !entry.isIntersecting);
}

// options lets you control the circumstances under which the observer's callback is invoked
const options = {
    // no root provided - by default browser viewport used to check visibility of target
    // Uncomment below if you want the nav bar to change background color as soon as content div is scrolled
    rootMargin: "-60px 0px 0px 0px",
    // only detect if visibility of target element is 100% or not
    threshold: [1]
};

// create intersection observer
const io = new IntersectionObserver(callback, options);

// observe content div 
const target = document.querySelector('#top-separator');
io.observe(target);
// ================NavBar Manipulator Block End================