# Projeto 8: Teste com Selenium

Este projeto tem como objetivo desenvolver testes automatizados para o fluxo completo de solicitação de um táxi no aplicativo Urban Routes, utilizando **Selenium WebDriver**, **Pytest** e **Page Object Model (POM)**.  

## 📌 Objetivo do Projeto
Finalizar o aplicativo de teste automatizado iniciado no **Projeto 7**, agora utilizando **Selenium** e aplicando boas práticas de automação de testes.  

Ao final, será possível:
- Executar testes automatizados que validam todo o processo de solicitação de um táxi;
- Visualizar os resultados e garantir que todas as funcionalidades principais estão funcionando corretamente.

---

## 🛠 Tecnologias Utilizadas
- **Python**
- **Selenium WebDriver**
- **Pytest**
- **Page Object Model (POM)**

---

## 🚖 Funcionalidades a Serem Testadas
Os testes automatizados devem cobrir o seguinte fluxo:

1. **Definir os endereços**:
   - Inserir endereço de partida e destino.
2. **Selecionar o plano Comfort**:
   - Implementar uma condição `if` para selecionar apenas se disponível.
3. **Preencher o número de telefone**:
   - Usar o método `retrieve_phone_code()` do arquivo `helpers.py` para obter o código SMS.
4. **Adicionar um cartão de crédito**:
   - Garantir que o botão "Adicionar" esteja habilitado apenas após o campo CVV perder o foco.
5. **Escrever um comentário para o motorista**.
6. **Pedir um cobertor e lenços**:
   - Utilizar dois seletores (um para clicar e outro para verificar via `assert`).
7. **Pedir 2 sorvetes**:
   - Implementar loop adequado no `pages.py`.
8. **Solicitar um táxi com tarifa Comfort**:
   - Confirmar que a janela modal de busca de carros aparece.

---


