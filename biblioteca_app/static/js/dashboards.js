addEventListener('load', () => {
    const queryString = window.location.search;
    const params = new URLSearchParams(queryString);
    const query = parseInt(params.get("succ"))

    if (query === 1) {
        Toastify({
            text: 'Canvis guardats correctament.',
            gravity: 'top',
            position: 'left',
            close: true,
            stopOnFocus: true,
            autoclose: 5000,
            style: {
                'background': '#4D8434',
                'color': 'white',
            }
        }).showToast();
    } 
    
    if (query === 0) {
        Toastify({
            text: 'Els canvis no s\'han guardat correctament. Si us plau, torna a intentar-ho més tard.',
            gravity: 'top',
            position: 'left',
            close: true,
            stopOnFocus: true,
            autoclose: 5000,
            style: {
                'background': '#CE1B1B',
                'color': 'white',
            }
        }).showToast();
    }

    
})