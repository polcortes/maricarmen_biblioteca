addEventListener('load', () => {
    const queryString = window.location.search;
    const params = new URLSearchParams(queryString);
    const query = parseInt(params.get("succ"))

    if (query === 1) {
        notify("info", "Canvis guardats correctament.", null);
    } 
    
    if (query === 0) {
        notify("error", "Els canvis no s'han guardat correctament. Si us plau, torna a intentar-ho més tard.", null);
    }

    
})