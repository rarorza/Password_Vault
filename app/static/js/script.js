document.addEventListener('DOMContentLoaded', function() {
  const passwordList = document.getElementById('password-list');
  const detailsPassword = document.getElementById('details');
  const inputName = document.getElementById('input-name');
  const inputUsername = document.getElementById('input-username');
  const inputUrl = document.getElementById('input-url');
  const inputPassword = document.getElementById('input-password');
  const btnAdd = document.getElementById('btn-add');
  const btnRemove = document.getElementById('btn-remove');

  // Array para armazenar as senhas
  const passwords = [
    { name: 'Senha 1', username: 'usuario1', url: 'http://example.com', password: 'senha123' },
  ];

  // Função para atualizar o valor exibido ao lado dos sliders
  function updateSliderValue(sliderId, spanId) {
    const slider = document.getElementById(sliderId);
    const span = document.getElementById(spanId);
    span.textContent = slider.value;
  }

  // Atualizar o valor exibido ao carregar a página
  updateSliderValue('slider-length', 'current-length');
  updateSliderValue('slider-character', 'current-character');
  updateSliderValue('slider-nums', 'current-nums');

  // Event listener para atualizar o valor ao mover os sliders
  document.getElementById('slider-length').addEventListener('input', function() {
    updateSliderValue('slider-length', 'current-length');
  });

  document.getElementById('slider-character').addEventListener('input', function() {
    updateSliderValue('slider-character', 'current-character');
  });

  document.getElementById('slider-nums').addEventListener('input', function() {
    updateSliderValue('slider-nums', 'current-nums');
  });

  // Função para exibir os detalhes de uma senha
  function showDetails(index) {
    const password = passwords[index];
    inputName.value = password.name;
    inputUsername.value = password.username;
    inputUrl.value = password.url;
    inputPassword.value = password.password;
    detailsPassword.style.display = 'block';
  }

  // Event listener para mostrar detalhes ao clicar em uma senha da lista
  passwordList.addEventListener('click', function(event) {
    const target = event.target;
    if (target.tagName === 'LI') {
      const index = Array.from(passwordList.children).indexOf(target);
      if (index >= 0) {
        showDetails(index);
        // Remover a classe 'active' dos outros itens e adicionar ao item clicado
        Array.from(passwordList.children).forEach((item, i) => {
          if (i === index) {
            item.classList.add('active');
          } else {
            item.classList.remove('active');
          }
        });
      }
    }
  });

  // Função para adicionar uma nova senha à lista
  function addPassword() {
    const newPassword = { nome: 'Nova Senha', username: 'novousuario', url: 'http://example.com', password: 'novasenha123' };
    passwords.push(newPassword);
    // Atualizar a lista de senhas
    const newLi = document.createElement('li');
    newLi.classList.add('list-group-item');
    newLi.textContent = newPassword.nome;
    passwordList.appendChild(newLi);
  }

  // Event listener para adicionar nova senha ao clicar no botão "Adicionar"
  btnAdd.addEventListener('click', function() {
    addPassword();
  });

  // Função para remover a senha selecionada
  function removerSenhaSelecionada() {
    const selectedLi = passwordList.querySelector('.list-group-item.active');
    if (selectedLi) {
      const index = Array.from(passwordList.children).indexOf(selectedLi);
      passwords.splice(index, 1); // Remover a senha do array
      passwordList.removeChild(selectedLi); // Remover o elemento da lista
      detailsPassword.style.display = 'none'; // Ocultar os detalhes da senha
    }
  }

  // Event listener para remover a senha selecionada ao clicar no botão "Remover Senha"
  btnRemove.addEventListener('click', function() {
    removerSenhaSelecionada();
  });
});
