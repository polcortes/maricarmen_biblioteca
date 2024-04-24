function appendLogToQueue(data) {
    const logQueue = JSON.parse(window.localStorage.getItem('logQueue')) ?? []
    logQueue.push(data)
    window.localStorage.setItem('logQueue', JSON.stringify(logQueue))
}

function sendData() {
    const logQueue = JSON.parse(window.localStorage.getItem('logQueue')) ?? []

    if (logQueue.length === 0) return

    logQueue.forEach(log => {
        fetch('/api/create_log', {
            method: 'POST',
            data: log
        }).then(res => {
            // console.log('res: ', res)
            if (res.status === 'OK') window.localStorage.setItem('logQueue', JSON.stringify([]))
            if (res.status === 'KO') throw new Error('Data couldn\'t be saved. Error: ' + res.message)
        })
          .catch(err => console.error('Data couldn\'t be saved. Error: ', err))
    })
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

// addEventListener('beforeunload', (ev) => {
//     ev.preventDefault()
//     const settingLogs = new Promise(sendData())
//     settingLogs
//         .then(() => {
//             return true
//         })
// })
