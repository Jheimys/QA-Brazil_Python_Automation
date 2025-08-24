# Projeto 8: Teste com Selenium

![Python](https://img.shields.io/badge/python-3.8-blue.svg)
![Selenium](https://img.shields.io/badge/selenium-webdriver-green.svg)
![Status](https://img.shields.io/badge/tests-passing-brightgreen)

## 📋 Índice
- [Objetivo do Projeto](#-objetivo-do-projeto)
- [Tecnologias Utilizadas](#-tecnologias-utilizadas)
- [Pré-requisitos](#-pré-requisitos)
- [Instalação](#-instalação)
- [Execução dos Testes](#-execução-dos-testes)
- [Funcionalidades a Serem Testadas](#-funcionalidades-a-serem-testadas)
- [Demonstração do Programa](#-demonstração-do-programa)
- [Contribuição](#-contribuição)
- [Licença](#-licença)
- [Contato](#-contato)

---

## 📌 Objetivo do Projeto

Este projeto tem como objetivo desenvolver testes automatizados para o fluxo completo de solicitação de um táxi no aplicativo Urban Routes, utilizando **Selenium WebDriver**, **Pytest** e **Page Object Model (POM)**.

Finalizar o aplicativo de teste automatizado iniciado no **Projeto 7**, agora utilizando **Selenium** e aplicando boas práticas de automação de testes.  

Ao final, será possível:
- Executar testes automatizados que validam todo o processo de solicitação de um táxi;
- Visualizar os resultados e garantir que todas as funcionalidades principais estão funcionando corretamente.

---

## 🛠 Tecnologias Utilizadas

- Python 3.8+
- Selenium WebDriver
- Pytest
- Page Object Model (POM)

---

## ⚙️ Pré-requisitos

Para rodar este projeto, você precisa ter instalado em sua máquina:

- Python 3.8 ou superior
- Pip (gerenciador de pacotes do Python)
- Navegador Google Chrome ou Mozilla Firefox
- ChromeDriver (para Chrome) ou GeckoDriver (para Firefox) compatíveis com a versão do navegador  
  *(Adicione o driver ao PATH ou no diretório do projeto)*

---

## 🚀 Instalação

1. Clone o repositório: https://github.com/Jheimys/QA-Brazil_Python_Automation
2. Instale as dependências: pip install -r requirements.txt
   
*Nota: O arquivo `requirements.txt` deve conter as bibliotecas necessárias como `selenium` e `pytest`.*

---

## ▶️ Execução dos Testes

Para executar todos os testes automatizados, rode o comando: pytest tests/


Os resultados da execução serão exibidos no terminal, indicando quais testes passaram ou falharam.

---

## 🚖 Funcionalidades a Serem Testadas

Os testes automatizados cobrem o seguinte fluxo do aplicativo Urban Routes:

1. **Definir os endereços**:
   - Inserir endereço de partida e destino.
2. **Selecionar o plano Comfort**:
   - Implementar uma condição `if` para selecionar somente se disponível.
3. **Preencher o número de telefone**:
   - Usar o método `retrieve_phone_code()` do arquivo `helpers.py` para obter o código SMS.
4. **Adicionar um cartão de crédito**:
   - Garantir que o botão "Adicionar" fique habilitado apenas após o campo CVV perder o foco.
5. **Escrever um comentário para o motorista**.
6. **Pedir um cobertor e lenços**:
   - Utilizar dois seletores (um para clicar e outro para verificar via `assert`).
7. **Pedir 2 sorvetes**:
   - Implementar loop adequado no `pages.py`.
8. **Solicitar um táxi com tarifa Comfort**:
   - Confirmar que a janela modal de busca de carros aparece.

---

## 📽 Demonstração do Programa

Veja abaixo uma demonstração dos testes automatizados em execução:

![Demonstração](https://github.com/Jheimys/assets/blob/master/spfinal.gif)

---

## 🤝 Contribuição

Contribuições são muito bem-vindas!  

- Abra uma issue para reportar bugs ou sugerir melhorias.
- Envie pull requests para contribuir com correções e novas funcionalidades.
- Sinta-se à vontade para ajudar a documentar ou melhorar a cobertura dos testes.

---

## 📄 Licença

Este projeto está licenciado sob a MIT License.

---

## 📞 Contato

- Nome: James Bassani 
- Email: james_bassani@yahoo.com  
- LinkedIn: [linkedin.com/in/jheimys](https://linkedin.com/in/jheimys)






