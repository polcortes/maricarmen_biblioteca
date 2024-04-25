// Función para cargar dinámicamente los usuarios
function cargarUsuarios() {
    // Realizar una solicitud AJAX al servidor para obtener los usuarios
    $.ajax({
        url: '/cargar-usuarios/', // URL de la vista Django que devuelve los usuarios
        method: 'GET',
        success: function(response) {
            // Actualizar el contenido del contenedor de usuarios con la respuesta del servidor
            $('#usuarios-container').html(response);
        },
        error: function(xhr, status, error) {
            console.error('Error al cargar usuarios:', error);
        }
    });
}
