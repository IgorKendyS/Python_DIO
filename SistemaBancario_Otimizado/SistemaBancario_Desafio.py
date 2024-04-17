

def valor_positivo(valor):
    if(valor <= 0):
        print("Valor inválido, insira um valor maior que 0!")
        return False
    else:
        return True
    
def valor_dentro_limite(valor, LIMITE):
    if valor > 500:
        print(f"Valor inserido está acima do limite, seu limite é de {LIMITE}")
        return False
    else:
        return True

def usuario_cadastrado(cpf, clientes):
    usuario = [cliente for cliente in clientes if cliente["CPF"] == cpf]
    if usuario != '[]':
        return True
    else:
        return False

def criar_usuario(clientes):
    print("Vamos começar seu cadastro!")
    cpf = input("Insira seu CPF: ")
    if usuario_cadastrado(cpf, clientes):
        nome = input("Nome completo: ")
        data_nasc = input("Data de nascimento: ")
        endereco = input("Endereço (formato: logradouro, numero - bairro - cidade/sigla estado): ")
        clientes.append({'nome': nome, 'CPF': cpf, 'data de nascimento': data_nasc, 'endereço': endereco})
    else:
        print("CPF já cadastrado!")
        
def criar_conta(contas, AGENCIA, clientes):
    cpf = input("Insira deu CPF: ")
    if usuario_cadastrado(cpf, clientes):
        tam = len(contas)
        if tam > 0:
            numero = contas[tam-1]['numero da conta']
            numero += 1
        else:
            numero = 1
        contas.append({'agencia': AGENCIA, 'CPF': cpf, 'numero da conta': numero})
        print(f"Conta {numero} cadastrada com sucesso!")
    else:
        print("Você não é um cliente cadastrado ainda, faça um cadastro primeiro")
        
def listar_contas(contas):
    for conta in contas:
        print(f"Agência: {conta['agencia']} Número da conta: {conta['numero da conta']}")
    
def deposito(valor, saldo, extrato_list, /):
    if valor_positivo:
        extrato_list.append(f"Depósito de R$ {valor:.2f}")
        print(f"Deposito de R$ {valor:.2f} realizado com sucesso!")
        print(f"Seu saldo atual é de R$ {(saldo+valor):.2f}")
        return saldo + valor
    else:
        print("Só é possível realizar depósitos com valores maiores que 0")

def sacar(*, valor, extrato_list, saldo, LIMITE, num_saques):
    if num_saques < 3:
        if valor_positivo(valor) and valor_dentro_limite(valor, LIMITE):
            print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
            print(f"Seu saldo atual é de R$ {(saldo-valor):.2f}")
            extrato_list.append(f"Saque de R$ {valor:.2f}")
            num_saques += 1
            return num_saques, saldo-valor
        else:
            print("Limite de saques diários atingido!")
    

def exibir_extrato(saldo, /, *, extrato):
    if extrato:
        print("\n".join(extrato))
        print(f"\nSaldo atual: R$ {saldo:.2f}")
    else:
        print("Não foram realizadas movimentações")


def menu():
    opcao = input("\n_____________MENU____________\n0 - sair\n1 - Criar usuario\n2 - Criar conta corrente\n3 - Deposito \n4 - Saque\n5 - Extrato\n6 - Listar Contas\n")
    return opcao

def main():
    LIMITE = 500
    AGENCIA = "0001"
    
    numero_de_saque = 0
    saldo = 0
    extrato_list = []
    
    clientes = []
    conta_corrente = []
    
    opcao = None
    while opcao!='0':
        opcao = menu()
        if opcao == '1':
            criar_usuario(clientes)
        
        elif opcao == '2':
            criar_conta(conta_corrente, AGENCIA, clientes)
        
        elif opcao == '3':
            valor = float(input("\nValor a depositar: "))
            saldo = deposito(valor, saldo, extrato_list)
                
        elif opcao == '4':
            valor = float(input("\nValor a sacar: "))
            numero_de_saque, saldo = sacar(valor=valor, extrato_list=extrato_list, saldo=saldo, LIMITE=LIMITE, num_saques=numero_de_saque)

        elif opcao == '5':
            exibir_extrato(saldo, extrato=extrato_list)
            
        elif opcao == '6':
            listar_contas(conta_corrente)
            
        elif opcao != '0':
            print("Opção inválida, selecione outra opção!")
    
    print("Programa encerrado!")
    
main()