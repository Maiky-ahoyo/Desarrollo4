const menuButton = document.getElementById('menu-button');
const menuClosed = document.getElementById('menu-closed');
const menuOpened = document.getElementById('menu-opened');
const menu = document.getElementById('mobile-menu');
const input = document.getElementById('input');
const inputMobile = document.getElementById('input-mobile');
const search = document.getElementById('search');
const searchMobile = document.getElementById('search-mobile');
const burger = document.getElementById('burger');
const navbar = document.getElementById('navbar');
const index = document.getElementById('index');
const searchBar = document.getElementById('searchbar');
const home = document.getElementById('home');
const magazines = document.getElementById('magazines');
const areas = document.getElementById('areas');
const categories = document.getElementById('categories');
const homeMobile = document.getElementById('home-mobile');
const magazinesMobile = document.getElementById('magazines-mobile');
const areasMobile = document.getElementById('areas-mobile');
const categoriesMobile = document.getElementById('categories-mobile');
const page = window.location.pathname;
console.log(page);

search.addEventListener('click', function() {
    let inputValue = input.value;
});

searchMobile.addEventListener('click', function() {
    let inputValue = inputMobile.value;
    window.location.href = '/initial/' + inputValue;
});

input.addEventListener('keypress', function(e) {
    if (e.key == 'Enter') {
        let inputValue = input.value;
        console.log(inputValue);
    }
});

inputMobile.addEventListener('keypress', function(e) {
    if (e.key == 'Enter') {
        let inputValue = inputMobile.value;
        console.log(inputValue);
    }
});

menuButton.addEventListener('click', function() {
    if (menuClosed.style.display == 'block') {
        menuClosed.style.display = 'none';
        menuOpened.style.display = 'block';
        menu.style.display = 'block';
    } else {
        menuClosed.style.display = 'block';
        menuOpened.style.display = 'none';
        menu.style.display = 'none';
    }
});

window.addEventListener('load', function() {
    if (page == '/') {
        home.style.backgroundColor = '#141f3a';
        homeMobile.style.backgroundColor = '#141f3a';
    } else {
        home.style.backgroundColor = 'transparent';
        hover(home);
        homeMobile.style.backgroundColor = 'transparent';
        hover(homeMobile);
    }
    if (page == '/magazines') {
        magazines.style.backgroundColor = '#141f3a';
        magazinesMobile.style.backgroundColor = '#141f3a';
    } else {
        magazines.style.backgroundColor = 'transparent';
        hover(magazines);
        magazinesMobile.style.backgroundColor = 'transparent';
        hover(magazinesMobile);
    }
    if (page == '/areas') {
        areas.style.backgroundColor = '#141f3a';
        areasMobile.style.backgroundColor = '#141f3a';
    } else {
        areas.style.backgroundColor = 'transparent';
        hover(areas);
        areasMobile.style.backgroundColor = 'transparent';
        hover(areasMobile);
    }
    if (page == '/categories') {
        categories.style.backgroundColor = '#141f3a';
        categoriesMobile.style.backgroundColor = '#141f3a';
    } else {
        categories.style.backgroundColor = 'transparent';
        hover(categories);
        categoriesMobile.style.backgroundColor = 'transparent';
        hover(categoriesMobile);
    }
    let titulo = this.document.getElementById('titulo');
    if (this.window.innerWidth < 416) {
        titulo.style.fontSize = '1em';
        if (this.window.innerWidth < 360) {
            titulo.style.fontSize = '0.8em';
        }
    } else {
        titulo.style.fontSize = '1.5em';
    }
    if (this.window.innerWidth > 1144) {
        burger.style.display = 'none';
        navbar.style.justifyContent = 'space-between';
        index.style.display = 'block';
        searchBar.style.display = 'flex';
    } else {    
        burger.style.display = 'flex';
        navbar.style.justifyContent = 'center';
        index.style.display = 'none';
        searchBar.style.display = 'none';
    }
});

window.addEventListener('resize', function() {
    if (this.window.innerWidth > 1144) {
        menu.style.display = 'none';
        burger.style.display = 'none';
        navbar.style.justifyContent = 'space-between';
        index.style.display = 'block';
        searchBar.style.display = 'flex';
        if (menuOpened.style.display == 'block') {
            menuOpened.style.display = 'none';
            menuClosed.style.display = 'block';
        }
        if (input.value != '') {
            inputMobile.value = input.value;
            input.value = '';
        }
        if (inputMobile.value != '') {
            input.value = inputMobile.value;
            inputMobile.value = '';
        }
    } else {
        burger.style.display = 'flex';
        navbar.style.justifyContent = 'center';
        index.style.display = 'none';
        searchBar.style.display = 'none';
        if (input.value != '') {
            inputMobile.value = input.value;
            input.value = '';
        }
        if (menuOpened.style.display == 'block') {
            menu.style.display = 'block';
        }
    }
    let titulo = this.document.getElementById('titulo');
    if (this.window.innerWidth < 416) {
        titulo.style.fontSize = '1em';
        if (this.window.innerWidth < 360) {
            titulo.style.fontSize = '0.8em';
        }
    } else {
        titulo.style.fontSize = '1.5em';
    }
});

function hover(target) {
    target.addEventListener('mouseover', function() {
        target.style.backgroundColor = '#496EA5';
    });
    target.addEventListener('mouseout', function() {
        target.style.backgroundColor = 'transparent';
    });
}