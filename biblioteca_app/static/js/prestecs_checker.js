const meses = {
    'gener': 1,
    'febrer': 2,
    'març': 3,
    'abril': 4,
    'maig': 5,
    'juny': 6,
    'juliol': 7,
    'agost': 8,
    'setembre': 9,
    'octubre': 10,
    'novembre': 11,
    'desembre': 12
}

addEventListener('load', () => {
    const table = document.querySelector('table')
    const rows = table.querySelectorAll('tbody > tr')

    rows.forEach(row => {
        const retorn = row.querySelector('.data-retorn')
        const prestec = row.querySelector('.data-prestec')
        const limit = row.querySelector('.data-limit')

        let dateLimit = limit.textContent.split(' ').slice(0, 4)
        dateLimit = new Date(dateLimit[3], Number(meses[dateLimit[1]]) - 1, dateLimit[0])
        
        const today = new Date()
        today.setHours(0, 0, 0, 0)

        console.log(`DateLimit: ${dateLimit < today}`)

        console.log("retorn.textContent == 'None'", retorn.textContent == 'None')

        if (dateLimit < today && retorn.textContent == 'None') {
            row.style.backgroundColor = 'rgba(255, 0, 0, 0.5)'
        }
    })
})