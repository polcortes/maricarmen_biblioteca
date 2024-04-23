document.getElementById("login-form").addEventListener("submit", function (event) {
  event.preventDefault(); // Evita que el formulario se envíe automáticamente

  var formData = {
      email: document.getElementById("email").value,
      password: document.getElementById("password").value
  };

  var url = "/api/login_api/"; // URL de tu endpoint de login
  const csrfToken = document.cookie.split('; ').find(row => row.startsWith('csrftoken=')).split('=')[1];

  fetch(url, {
      method: "POST",
      headers: {
          'Content-Type': 'application/json', // Especifica que los datos son JSON
          'X-CSRFToken': csrfToken // Agrega el token CSRF a la cabecera de la solicitud
      },
      body: JSON.stringify(formData), // Convierte el objeto JSON a una cadena JSON
  })
  .then((response) => {
      if (response.ok) {
          return response.json(); // Convierte la respuesta en JSON
      }
      throw new Error("Error en la solicitud: " + response.statusText);
  })
  .then((data) => {
      // Maneja la respuesta de la API
      if (data.redirect_url) {
          window.location.href = data.redirect_url; // Redirige según la URL proporcionada por la API
      } else {
          console.error("Error en la respuesta de la API:", data.error);
      }
  })
  .catch((error) => { 
      console.error("Error en la solicitud:", error);
  });
});
