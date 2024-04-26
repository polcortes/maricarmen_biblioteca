function appendLogToQueue(data) {
    const logQueue = JSON.parse(window.localStorage.getItem('logQueue')) ?? []
    logQueue.push(data)
    window.localStorage.setItem('logQueue', JSON.stringify(logQueue))
}

function sendData() {
    const logQueue = JSON.parse(window.localStorage.getItem('logQueue')) || [];

    // const csrfToken = document.querySelector('meta[name="csrf-token"]').getAttribute('content');

    const csrfToken = document.cookie.split('; ').find(row => row.startsWith('csrftoken=')).split('=')[1];

    if (logQueue.length === 0) return;

    logQueue.forEach(log => {
        fetch('/api/create_log', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json', // Especifica que los datos son JSON
                'X-CSRFToken': csrfToken // Agrega el token CSRF a la cabecera de la solicitud
            },
            // body: JSON.stringify(log) // Convierte los datos a JSON antes de enviarlos
            body: JSON.stringify(log)
        })
            .then(res => {
                if (res.ok) { // Cambiado de res.status a res.ok para verificar si la solicitud fue exitosa
                    window.localStorage.setItem('logQueue', JSON.stringify([]));
                    console.log('Funciona: ', res);
                } else {
                    console.log('No funciona');
                    return res.json(); // Parsea la respuesta JSON para acceder a los datos
                }
            })
    });
}

document.addEventListener('click', (ev) => {
    appendLogToQueue({
        type: 'info', 
        title: `${ev.type} event registered on: ${ev.target}`, 
        description: '', 
        date: new Date(),
        pathname: window.location.pathname
    })

    console.log('Has hecho click en el documento, exactamente en: ', ev.target)
})

addEventListener('load', () => {
    // alert('Page loaded')
    setInterval(() => sendData(), 20000)
})