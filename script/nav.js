function controlNavbar () {
    var navbar = document.getElementsByTagName('nav')[0];
    // var navbar = document.getElementById('nav');
    var maincont = document.getElementById('main-container');
    var navbarState = navbar.dataset.state;
    var maincontState = maincont.dataset.navbar;

    if (maincontState != navbarState) {
        maincontState = navbarState;
        maincont.dataset.navbar = navbarState;
    }

    if (navbarState == 'opened') {
        navbar.dataset.state = 'closed';
        maincont.dataset.navbar = 'closed';
    }
    else if (navbarState == 'closed') {
        navbar.dataset.state = 'opened';
        maincont.dataset.navbar = 'opened';
    }
}