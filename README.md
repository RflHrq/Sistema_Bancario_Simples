# Projeto de Gerenciamento Bancário em Python

## Descrição

Este projeto é uma aplicação simples de gerenciamento bancário desenvolvida em Python. O código simula um sistema bancário básico, permitindo operações de depósito, saque e visualização de extrato. O objetivo principal deste projeto é aprimorar o conhecimento da linguagem Python através da implementação de funcionalidades típicas de sistemas bancários.

## Funcionalidades

O sistema oferece as seguintes funcionalidades:

1. **Depósito**: Permite ao usuário depositar um valor na conta. O valor deve ser positivo.
2. **Saque**: Permite ao usuário sacar um valor da conta, respeitando as seguintes regras:
   - O valor do saque deve ser positivo.
   - O valor máximo de saque é R$ 500,00.
   - O saldo disponível deve ser suficiente para o saque.
3. **Extrato**: Exibe o histórico de transações realizadas, incluindo depósitos e saques, e o saldo atual da conta.
4. **Saída**: Encerra o programa.

## Código

O código é dividido em três funções principais:

1. **`deposito()`**: Solicita ao usuário o valor a ser depositado e valida a entrada. Retorna o valor do depósito se for válido.
2. **`saque(saldo)`**: Solicita ao usuário o valor a ser sacado e valida a entrada. Retorna o valor do saque se for válido e possível. O saldo da conta é atualizado conforme o valor sacado.
3. **`menu()`**: Exibe o menu principal e gerencia a lógica do sistema bancário, incluindo operações de depósito e saque, controle de limites de saques diários e exibição do extrato.

## Requisitos

- Python 3.x

## Como Executar

Para executar o código, siga os seguintes passos:

1. Certifique-se de que o Python está instalado em seu sistema.
2. Copie o código para um arquivo Python, por exemplo, `banco.py`.
3. Execute o arquivo Python usando o comando:
   ```bash
   python banco.py