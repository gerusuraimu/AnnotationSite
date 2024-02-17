const wrapper = document.getElementById('wrapper');
const createButton = document.getElementById('create-button');


createButton.addEventListener('click', () => {
    wrapper.classList.add('active-popup');
});