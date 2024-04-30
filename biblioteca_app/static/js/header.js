addEventListener('load', () => {
    const userIcon = document.getElementById('user-img');
    const userMenu = document.querySelector('.dropdown-content');

    document.addEventListener('click', (ev) => {
        if (ev.target !== userIcon && ev.target !== userMenu) userMenu.classList.remove('show');
        if (ev.target === userIcon) userMenu.classList.toggle('show');
    })
})