addEventListener('load', () => {
    const toggleMenu = document.getElementById('toggle-general-menu');
    const mobileMenu = document.getElementById('mobile-general-menu');
    const header = document.querySelector('body > header');
    const closeMobileMenu = document.getElementById('close-mobile-general-menu');

    // header.classList.remove('hidden');
    // mobileMenu.classList.add('hidden');

    toggleMenu.addEventListener('click', () => {
        mobileMenu.classList.remove('hidden');
        header.classList.add('hidden');
    })

    closeMobileMenu.addEventListener('click', () => {
        mobileMenu.classList.add('hidden');
        header.classList.remove('hidden');
    })
})