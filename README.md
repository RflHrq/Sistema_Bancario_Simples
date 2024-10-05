# Projeto de Gerenciamento Bancário em Python

## Descrição

Este projeto é uma aplicação simples de gerenciamento bancário desenvolvida em Python. O código simula um sistema bancário básico, permitindo operações de depósito, saque e visualização de extrato. O objetivo principal deste projeto é aprimorar o conhecimento da linguagem Python através da implementação de funcionalidades típicas de sistemas bancários.

## Funcionalidades

O sistema oferece as seguintes funcionalidades:

1. **Depositar**: Permite ao usuário depositar um valor em sua conta.
2. **Sacar**: Permite ao usuário sacar um valor de sua conta, respeitando os limites diários e máximos por saque.
3. **Exibir Extrato**: Mostra o histórico de transações realizadas na conta selecionada.
4. **Cadastrar Novo Usuário**: Permite cadastrar um novo usuário no sistema.
5. **Nova Conta**: Cria uma nova conta bancária associada a um usuário existente.
6. **Listar Contas**: Mostra todas as contas cadastradas e permite selecionar uma conta para realizar operações.

## Código

O código é dividido nas seguintes funções:

1. **`menu()`**: Exibe as opções disponíveis para o usuário interagir com o sistema. Coleta a escolha do usuário e retorna essa opção, permitindo que o programa saiba qual ação deve ser executada em seguida.

2. **`deposito()`**: Solicita ao usuário o valor a ser depositado e valida a entrada. O valor depositado é registrado em um histórico de transações. Retorna o saldo atualizado e o histórico após a operação.

3. **`saque(conta)`**: Solicita ao usuário o valor a ser sacado e valida a entrada. Se o saldo for insuficiente, uma mensagem de erro é exibida. Caso contrário, o valor é subtraído do saldo e registrado no histórico de transações. Retorna a conta com o saldo atualizado.

4. **`imprimir_extrato(conta_selecionada)`**: Imprime o histórico de transações do usuário. Se não houver transações registradas, exibe uma mensagem apropriada.

5. **`criar_usuario(usuarios)`**: Permite que um novo usuário seja cadastrado no sistema. O usuário fornece seu nome, CPF e endereço, que são armazenados em uma lista de usuários. Uma mensagem de confirmação é exibida após o cadastro.

6. **`filtrar_usuario(usuarios, cpf)`**: Filtra a lista de usuários com base no CPF fornecido. Retorna o usuário correspondente se encontrado; caso contrário, retorna `None`.

7. **`criar_conta(usuarios, contas)`**: Vincula uma nova conta a um usuário existente. O CPF do usuário é solicitado, e se um usuário correspondente for encontrado, uma nova conta é criada com um número exclusivo e um saldo inicial de zero. Exibe uma mensagem de erro se o CPF não for encontrado.

8. **`listar_contas(contas)`**: Exibe todas as contas registradas, mostrando o número da conta e o nome do usuário associado. O usuário pode selecionar uma conta a partir da lista, e a função retorna a conta escolhida.

9. **`main()`**: Controla o fluxo do programa, executando um loop contínuo que permite ao usuário escolher diferentes opções do menu. Chama as funções apropriadas com base na escolha do usuário e continua até que o usuário decida sair do sistema.

## Limitações
O sistema possui limites para saques diários e valores máximos por saque, que devem ser definidos em constantes. Além disso, o CPF deve ser único para cada usuário, e o sistema irá solicitar um novo CPF se o fornecido já estiver cadastrado.

## Requisitos

- Python 3.x
- Biblioteca `pytz`
  
Para instalar a biblioteca `pytz`, utilize o seguinte comando:

```bash
pip install pytz


## Como Executar

Para executar o código, siga os seguintes passos:

1. Certifique-se de que o Python está instalado em seu sistema.
2. Copie o código para um arquivo Python, por exemplo, `banco.py`.
3. Execute o arquivo Python usando o comando:
   ```bash
   python banco.py