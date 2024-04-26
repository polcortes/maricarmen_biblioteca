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

function mostrar(id) {
    // Oculta todos los elementos con la clase "mostrar"
    var elementos = document.querySelectorAll('[id^="mostrar-"]');
    elementos.forEach(function(elemento) {
        elemento.style.display = 'none';
    });

    // Muestra el elemento correspondiente al ID pasado como parámetro
    var elementoMostrar = document.getElementById(id);
    if (elementoMostrar) {
        elementoMostrar.style.display = 'block';
    }
}
