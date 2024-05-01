addEventListener('load', () => {
    const table = document.querySelector('table')
    const rows = table.querySelectorAll('tr')

    rows.forEach(row => {
        const retorn = row.querySelector('.data-retorn')
        const prestec = row.querySelector('.data-prestec')
        const limit = row.querySelector('.data-limit')

        if (new Date(limit.innerHTML) < new Date() && prestec.innerHTML === 'None') {
            row.style.backgroundColor = 'rgba(255, 0, 0, 0.5)'
        }
    })
})