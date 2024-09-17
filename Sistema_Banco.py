from datetime import datetime

def deposito():
    while True:
        print("Defina o valor que deseja depositar")
        valor_deposito = float(input("Valor: "))
        if valor_deposito < 0:
            print("Valor inválido. Por favor, digite um valor positivo.")
        else:
            return valor_deposito

def saque(saldo):
    while True:
        print("Defina o valor que deseja sacar")
        valor_saque = float(input("Valor: "))
        if valor_saque < 0:
            print("Valor inválido. Por favor, digite um valor positivo.")
        elif valor_saque > 500:
            print("Limite de saques excedido. Não é possível sacar este valor.")
        elif valor_saque > saldo:
            print("Saldo insuficiente. Não é possível sacar este valor.")
        else:
            return valor_saque

def menu():
    saldo = 2000.00
    historico = []
    LIMITE_SAQUES = 3
    quant_saques = 0
    data_sessao = datetime.now().date()
    
    while True:
        print("Bem vindo ao nosso Banco! \nEscolha uma opção")
        print("1. Depósito")
        print("2. Saque")
        print("3. Extrato")
        print("4. Sair")

        # Captura a escolha do usuário
        escolha = input("Selecione uma opção (1-4): ")
        
        # Verifica a opção selecionada
        if escolha == '1':
            print("Modo de Depósito")
            valor_deposito = deposito()
            saldo += valor_deposito
            historico.append(f"Depósito: R$ {valor_deposito:.2f} | Saldo: R$ {saldo:.2f}")

        elif escolha == '2':
            print("Modo de Saque")
            data_atual = datetime.now().date()
            if data_atual != data_sessao:
                data_sessao = data_atual
                quant_saques = 0
            
            if quant_saques >= LIMITE_SAQUES:
                print("Você atingiu o limite de 3 saques diários.")
            else:
                valor_saque = saque(saldo)
                saldo -= valor_saque
                quant_saques += 1
                historico.append(f"Saque: R$ {valor_saque:.2f} | Saldo: R$ {saldo:.2f}")

        elif escolha == '3':
            print("Modo de Extrato")
            if not historico:
                print("Não foi realizada nenhuma transação.")
            else:
                for transacao in historico:
                    print(transacao)
            print(f"\n\nO seu saldo atualizado: R$ {saldo:.2f}")

        elif escolha == '4':
            print("Saindo...")
            break

        else:
            print("Opção inválida! Por favor, selecione uma opção válida.")

menu()
