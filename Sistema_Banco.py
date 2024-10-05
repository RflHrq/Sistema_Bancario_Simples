from datetime import datetime
import pytz
import textwrap

# Definindo limites
NUMERO_AGENCIA = "0001"
LIMITE_SAQUES = 3
LIMITE_VALOR_SAQUE = 500.00

# Função do menu
def menu():
    menu_texto = """\n
    =============== MENU =================
    [1]\tDepositar
    [2]\tSacar
    [3]\tExibir Extrato
    [4]\tCadastrar novo usuário
    [5]\tNova Conta
    [6]\tListar Contas
    [0]\tSair
    =>"""
    return input(textwrap.dedent(menu_texto))

# Função de depósito
def deposito(saldo, extratos):
    while True:
        try:
            valor_deposito = float(input("Defina o valor que deseja depositar: R$ "))
            if valor_deposito <= 0:
                print("Valor inválido. Por favor, digite um valor positivo.")
            else:
                saldo += valor_deposito
                hora_deposito = datetime.now(pytz.timezone("America/Sao_Paulo"))
                extrato = f"Depósito: R$ {valor_deposito:.2f} | Saldo: R$ {saldo:.2f} | Horário do Depósito: {hora_deposito.strftime('%d/%m/%Y %H:%M:%S')}\n"
                extratos.append(extrato)  # Armazena como uma lista
                print(f"Depósito realizado com sucesso!")
                return saldo, extratos
        except ValueError:
            print("Entrada inválida. Por favor, digite um valor numérico.")

# Função de saque
def saque(conta):
    data_atual = datetime.now(pytz.timezone("America/Sao_Paulo")).date()

    # Reseta a quantidade de saques se for um novo dia
    if data_atual != conta['data_sessao']:
        conta['data_sessao'] = data_atual
        conta['quant_saques'] = 0

    if conta['quant_saques'] >= LIMITE_SAQUES:
        print("Você atingiu o limite de 3 saques diários.")
        return conta['saldo'], conta['quant_saques'], conta['data_sessao'], None

    while True:
        try:
            valor_saque = float(input("Defina o valor que deseja sacar: R$ "))
            if valor_saque <= 0:
                print("Valor inválido. Por favor, digite um valor positivo.")
            elif valor_saque > LIMITE_VALOR_SAQUE:
                print(f"Limite de saques excedido. O valor máximo permitido por saque é R$ {LIMITE_VALOR_SAQUE:.2f}.")
            elif valor_saque > conta['saldo']:
                print("Saldo insuficiente. Não é possível sacar este valor.")
            else:
                # Atualiza saldo, contagem de saques e registra o saque no extrato
                conta['saldo'] -= valor_saque
                conta['quant_saques'] += 1
                hora_saque = datetime.now(pytz.timezone("America/Sao_Paulo"))
                extrato = f"Saque: R$ {valor_saque:.2f} | Saldo: R$ {conta['saldo']:.2f} | Horário do Saque: {hora_saque.strftime('%d/%m/%Y %H:%M:%S')}\n"
                print(f"Saque realizado com sucesso! Seu novo saldo é R$ {conta['saldo']:.2f}")
                return conta['saldo'], conta['quant_saques'], conta['data_sessao'], extrato
        except ValueError:
            print("Entrada inválida. Por favor, digite um valor numérico.")

def imprimir_extrato(conta_selecionada):
    if conta_selecionada:
        print("Modo de Extrato")
        if not conta_selecionada['historico']:
            print("Não foi realizada nenhuma transação.")
        else:
            print(f"\nExtrato impresso às {datetime.now(pytz.timezone('America/Sao_Paulo')).strftime('%d/%m/%Y %H:%M:%S')}")
            for transacao in conta_selecionada['historico']:
                print(transacao, end='')  # imprime cada transação
    else:
        print("Nenhuma conta selecionada. Por favor, selecione uma conta antes de prosseguir.")

# Função para criar um novo usuário
def criar_usuario(usuarios):
    while True:
        cpf = input("CPF: ")
        
        # Valida o CPF enquanto o usuário digita
        if len(cpf) != 11 or not cpf.isdigit():
            print("CPF inválido. Por favor, digite um CPF válido.")
            continue
        
        for usuario in usuarios:
            if usuario[1] == cpf:
                print("CPF já cadastrado. Por favor, tente novamente.")
                break
        else:
            nome = input("Nome: ")
            data_nascimento = input("Data de Nascimento (DD/MM/AAAA): ")
            logradouro = input("Logradouro: ")
            numero = input("Número: ")
            bairro = input("Bairro: ")
            cidade = input("Cidade: ")
            estado = input("Sigla do Estado (UF): ").upper()
            
            usuarios.append((nome, cpf, data_nascimento, logradouro, numero, bairro, cidade, estado))
            print("Usuário cadastrado com sucesso.")
            return

# Função para filtrar um usuário
def filtrar_usuario(usuarios, cpf):
    for usuario in usuarios:
        if usuario[1] == cpf:
            return usuario
    print("Usuário não encontrado.")
    return None

def criar_conta(usuarios, contas):
    numero_conta = len(contas) + 1
    
    while True:
        cpf = input("Informe o CPF do usuário para vincular a conta (ou digite 0 para sair): ")
        
        # Se o usuário digitar '0', saímos do loop
        if cpf == '0':
            print("Operação cancelada.")
            return
        
        # Verifica se o CPF é encontrado na lista de usuários
        usuario = filtrar_usuario(usuarios, cpf)
        
        if usuario is None:
            print("Usuário não encontrado. Tente novamente.")
        else:
            # CPF encontrado, então cria-se a conta
            conta = {
                'numero_conta': f"{numero_conta:04d}",
                'agencia': NUMERO_AGENCIA,
                'usuario': usuario,
                'saldo': 0.00,
                'historico': [],  # Armazenando como uma lista
                'quant_saques': 0,   # Quantidade de saques do usuário
                'data_sessao': datetime.now(pytz.timezone("America/Sao_Paulo")).date()  # Data de controle de saques
            }
            
            contas.append(conta)
            print(f"Conta criada com sucesso! Número da conta: {conta['numero_conta']}, Agência: {conta['agencia']}.")
            break  # Encerra o loop após criar a conta

# Função para listar contas
def listar_contas(contas):
    if not contas:
        print("Nenhuma conta cadastrada.")
        return None

    print("\nLista de Contas:")
    for i, conta in enumerate(contas):
        usuario = conta['usuario']
        print(f"[{i + 1}] Conta: {conta['numero_conta']}, Agência: {conta['agencia']}, Usuário: {usuario[0]} - CPF: {usuario[1]}")

    while True:
        try:
            escolha = int(input("Selecione o número da conta que deseja usar (ou 0 para cancelar): "))
            if escolha == 0:
                print("Operação cancelada.")
                return None
            elif 1 <= escolha <= len(contas):
                conta_selecionada = contas[escolha - 1]
                print(f"Conta {conta_selecionada['numero_conta']} selecionada com sucesso!")
                return conta_selecionada
            else:
                print("Opção inválida. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número.")

# Função principal
def main():
    usuarios = []
    contas = []
    conta_selecionada = None

    while True:
        escolha = menu()

        if escolha == '1':  # Depósito
            if conta_selecionada:
                conta_selecionada['saldo'], conta_selecionada['historico'] = deposito(conta_selecionada['saldo'], conta_selecionada['historico'])
            else:
                print("Nenhuma conta selecionada. Por favor, selecione uma conta antes de realizar um depósito.")
        
        elif escolha == '2':  # Saque
            if conta_selecionada:
                saldo, quant_saques, data_sessao, extrato = saque(conta_selecionada)
                if extrato:  # Se um saque foi realizado
                    conta_selecionada['historico'].append(extrato)  # Adiciona ao histórico da conta
            else:
                print("Nenhuma conta selecionada. Por favor, selecione uma conta antes de realizar um saque.")

        elif escolha == '3':  # Extrato
            imprimir_extrato(conta_selecionada)

        elif escolha == '4':  # Cadastrar novo usuário
            criar_usuario(usuarios)

        elif escolha == '5':  # Nova Conta
            criar_conta(usuarios, contas)

        elif escolha == '6':  # Listar Contas
            conta_selecionada = listar_contas(contas)

        elif escolha == '0':  # Sair
            print("Obrigado por usar o sistema. Até a próxima!")
            break
        
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
