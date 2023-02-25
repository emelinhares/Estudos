const users = [
	{username: "user1", password: "pass1"},
	{username: "user2", password: "pass2"},
	{username: "user3", password: "pass3"}
  ];
  
  const loginButton = document.getElementById("login-button");
  const errorMessage = document.getElementById("error-message");
  
  loginButton.addEventListener("click", function(event) {
	event.preventDefault();
	const username = document.getElementById("username").value;
	const password = document.getElementById("password").value;
	const user = users.find(u => u.username === username && u.password === password);
	if (user) {
	  window.location.href = "pagina_secreta.html";
	} else {
	  errorMessage.textContent = "Nome de usuário ou senha incorretos.";
	}
  });
  