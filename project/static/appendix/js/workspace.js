const wrapper = document.getElementById('wrapper');
const iconClose = document.getElementById('icon-close');
const createMenu = document.getElementById('create-menu');
const createButton = document.getElementById('create-button');


createButton.addEventListener('click', () => {
    wrapper.classList.add('active-popup');
});


createMenu.addEventListener('click', () => {
    wrapper.classList.add('active-popup');
});


iconClose.addEventListener('click', () => {
    wrapper.classList.remove('active-popup');
});