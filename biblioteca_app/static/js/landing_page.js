document.addEventListener("DOMContentLoaded", function() {
    // Función para manejar el envío del formulario
    /*
    document.querySelector("form").addEventListener("submit", function(event) {
        event.preventDefault(); // Evitar el envío del formulario por defecto
        
        // Obtener los valores de usuario y contraseña
        var username = document.getElementById("username").value;
        var password = document.getElementById("password").value;

        // Determinar el tipo de usuario
        var isAdmin = isUserAdmin(username);

        // Redirigir según el tipo de usuario
        if (isAdmin) {
            window.location.href = "http://127.0.0.1:8000/dashboard/admin/";
        } else {
            window.location.href = "http://127.0.0.1:8000/dashboard/general/";
        }
    });
    */

    // Función para determinar si el usuario es administrador o no
    function isUserAdmin(username) {
        // Supongamos que el usuario es admin si el nombre de usuario contiene la palabra "admin"
        return username.toLowerCase().includes("admin");
    }
});
