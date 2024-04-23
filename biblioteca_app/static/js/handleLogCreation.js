function appendLogToQueue(data) {
    const logQueue = JSON.parse(window.localStorage.getItem('logQueue')) ?? []
    logQueue.push(data)
    window.localStorage.setItem('logQueue', JSON.stringify(logQueue))
}

function sendData() {
    const logQueue = JSON.parse(window.localStorage.getItem('logQueue')) ?? []

    if (logQueue.length === 0) return

    logQueue.forEach(log => {
        fetch('http://localhost/api/create_log', {
            method: 'POST',
            data: log
        }).then(() => console.log('log created successfully'))
          .catch(err => console.error('log couldn\'t be created. Err: ', err))
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
})

addEventListener('load', () => {
    setInterval(() => sendData(), 120000)
})

addEventListener('beforeunload', (ev) => {
    ev.preventDefault()
    const settingLogs = new Promise(sendData())
    settingLogs
        .then(() => {
            return true
        })
})