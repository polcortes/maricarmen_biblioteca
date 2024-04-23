document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('change-pass-form');

    form.addEventListener('submit', function(event) {
        event.preventDefault(); // Evita que el formulario se envíe automáticamente

        const currentPassword = document.getElementById('current_password').value;
        const newPassword = document.getElementById('new_password').value;
        const confirmPassword = document.getElementById('confirm_password').value;

        // Validar que las contraseñas nuevas coincidan
        if (newPassword !== confirmPassword) {
            alert('Les contrasenyes noves no coincideixen.');
            return;
        }

        // Enviar solicitud al servidor para cambiar la contraseña
        fetch('/cambiar-contrasenya/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCookie('csrftoken') // Obtener el token CSRF de la cookie
            },
            body: JSON.stringify({
                current_password: currentPassword,
                new_password: newPassword
            })
        })
        .then(response => {
            if (response.ok) {
                alert('Contrasenya canviada amb èxit.');
                form.reset(); // Limpiar el formulario después de un cambio exitoso
            } else {
                throw new Error('Error al cambiar la contrasenya.');
            }
        })
        .catch(error => {
            console.error('Error:', error);
            alert('Hi ha hagut un error en canviar la contrasenya. Si us plau, intenta-ho de nou més tard.');
        });
    });

    // Función para obtener el token CSRF de la cookie
    function getCookie(name) {
        const value = `; ${document.cookie}`;
        const parts = value.split(`; ${name}=`);
        if (parts.length === 2) return parts.pop().split(';').shift();
    }
});