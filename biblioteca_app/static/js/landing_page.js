document
  .getElementById("login-form")
  .addEventListener("submit", function (event) {
    event.preventDefault(); // Evita que el formulario se envíe automáticamente

    var formData = new FormData(this); // Obtiene los datos del formulario
    var url = "/api/login_api/"; // URL de tu endpoint de login

    fetch(url, {
      method: "POST",
      body: formData,
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
