def deposito(valor, conta, extrato_list):
    extrato_list.append(f"Depósito de R$ {valor:.2f}")
    return conta + valor


def saque(valor, conta, extrato_list):
    extrato_list.append(f"Saque de R$ {valor:.2f}")
    return conta - valor


def verifica_valor(valor):
    if(valor <= 0):
        print("Valor inválido, insira um valor maior que 0!")
        return False
    else:
        return True
    

numero_de_saque = 0
saldo = 0
extrato_list = []

while True:
    opcao = input("\n_____________MENU____________\n0 - sair\n1 - deposito \n2 - saque\n3 - extrato\n")
    if opcao == '0':
        break
    elif opcao == '1':
        valor = float(input("\nValor a depositar: "))
        if verifica_valor(valor):
           saldo = deposito(valor, saldo, extrato_list)
           
    elif opcao == '2':
        valor = float(input("\nValor a sacar: "))
        if numero_de_saque < 3:
            if verifica_valor(valor):
                if valor > 500:
                    print("O limite máximo de saque é R$500,00")
                elif valor > saldo:
                    print("Saldo insuficiente")
                else:
                    saldo = saque(valor, saldo, extrato_list)
                    numero_de_saque += 1
        else:
            print("Limite de saques diários atingido!--")

    elif opcao == '3':
        if extrato_list:
            print("\n".join(extrato_list))
            print(f"\nSaldo atual: R$ {saldo:.2f}")
        else:
            print("Não foram realizadas movimentações")
    
    else:
        print("Opção inválida, selecione outra opção!")