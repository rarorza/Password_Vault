// Função para copiar a senha para a área de transferência
function copyPassword() {
  const passwordInput = document.getElementById("password");
  passwordInput.select();
  document.execCommand("copy");
}

// Função para gerar uma nova senha
function generatePassword() {
  // Obter os valores dos parâmetros
  const length = document.getElementById("length").value;
  const numbers = document.getElementById("numbers").value;
  const specialChars = document.getElementById("specialChars").value;

  // Fazer uma requisição ao backend para gerar a senha
  // Substitua "URL_DO_BACKEND" pela URL real do seu backend
  fetch("URL_DO_BACKEND", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ length, numbers, specialChars }),
  })
    .then(response => response.json())
    .then(data => {
      const passwordInput = document.getElementById("password");
      passwordInput.value = data.password;
    })
    .catch(error => {
      console.error("Erro ao gerar a senha:", error);
    });
}

// Função para salvar os dados do usuário e adicionar à lista
function saveData() {
  // Obter os valores dos campos de entrada
  const name = document.getElementById("name").value;
  const username = document.getElementById("username").value;
  const url = document.getElementById("url").value;
  const category = document.getElementById("category").value;

  // Criar um novo item de lista
  const listItem = document.createElement("li");
  listItem.innerHTML = `
    <strong>Name:</strong> ${name}<br>
    <strong>Username:</strong> ${username}<br>
    <strong>URL:</strong> ${url}<br>
    <strong>Category:</strong> ${category}<br>
    <strong>Password:</strong> <br></br>
    `;


  // Criar os botões de editar e excluir
  const editButton = document.createElement("button");
  editButton.textContent = "Edit";
  editButton.addEventListener("click", () => {
    // Lógica para editar o item da lista
    console.log("Editar item:", listItem.textContent);
  });

  const deleteButton = document.createElement("button");
  deleteButton.textContent = "Delete";
  deleteButton.addEventListener("click", () => {
    // Lógica para excluir o item da lista
    listItem.remove();
  });

  // Adicionar os botões ao item da lista
  listItem.appendChild(editButton);
  listItem.appendChild(deleteButton);

  // Adicionar o novo item à lista de senhas
  const passwordList = document.getElementById("passwordList");
  passwordList.appendChild(listItem);
}

// Adicionar os manipuladores de eventos aos botões
document.getElementById("copyButton").addEventListener("click", copyPassword);
document.getElementById("generatePassword").addEventListener("click", generatePassword);
document.getElementById("save").addEventListener("click", saveData);

