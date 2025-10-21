# 🐍 Sistema Bancário em Python

![Status](https://img.shields.io/badge/Status-Concluído-brightgreen)
![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)

## 📝 Descrição do Projeto

Este projeto, desenvolvido como parte do bootcamp **"Santander 2025 - Back-End com Python"** da [DIO](https://www.dio.me/), consiste na criação de um sistema bancário em Python. A versão inicial focava em operações básicas de depósito, saque e extrato.

Esta versão representa uma **evolução do sistema original**, que foi refatorado para incluir a gestão de usuários e contas, organizando o código em funções para melhorar a modularidade, legibilidade e manutenção.

## ✨ Funcionalidades

O sistema agora permite ao usuário interagir com um menu para realizar as seguintes operações:

### Gestão de Usuários e Contas
* **Criar Usuário:** Cadastra um novo usuário no sistema solicitando nome, data de nascimento, CPF e endereço. O sistema impede a criação de usuários com CPF duplicado.
* **Criar Conta Corrente:** Vincula uma nova conta a um usuário existente através do CPF. Cada nova conta é criada com um número sequencial e associada à agência padrão.
* **Listar Contas:** Exibe uma lista com todas as contas cadastradas, mostrando a agência, o número da conta e o nome do titular.

### Operações Bancárias
* **Depositar:** Permite adicionar valores positivos ao saldo da conta.
* **Sacar:** Permite retirar valores da conta, respeitando as seguintes regras:
    * Limite máximo de **3 saques diários**.
    * Valor máximo de **R$ 500,00 por saque**.
    * O usuário não pode sacar um valor maior do que o saldo em conta.
* **Extrato:** Exibe o histórico de transações (depósitos e saques) e o saldo atual da conta.
* **Sair:** Encerra a aplicação.

## 🏗️ Estrutura do Projeto

O código foi refatorado e organizado nas seguintes funções principais para separar responsabilidades:

* `main()`: Função principal que gerencia o loop do programa e o menu de opções.
* `menu()`: Exibe as opções e captura a escolha do usuário.
* `sacar()`: Lida com toda a lógica da operação de saque.
* `depositar()`: Controla a lógica de depósito.
* `criar_usuario()`: Gerencia o fluxo de cadastro de novos usuários.
* `criar_conta()`: Responsável pela criação de novas contas.
* `listar_contas()`: Formata e exibe a lista de contas.
* `filtrar_usuario()`: Função utilitária para buscar um usuário pelo CPF.

## 🚀 Como Executar o Projeto

1.  Faça o clone do repositório:
    ```bash
    git clone [https://github.com/andradmarcel/projeto_sistema_bancario_DIO.git](https://github.com/andradmarcel/projeto_sistema_bancario_DIO.git)
    ```
2.  Navegue até o diretório do projeto:
    ```bash
    cd projeto_sistema_bancario_DIO
    ```
3.  Execute o script principal:
    ```bash
    python sistema_bancario.py
    ```

## ✒️ Autor

**Marcel Andrade**

[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/andradmarcel/)
