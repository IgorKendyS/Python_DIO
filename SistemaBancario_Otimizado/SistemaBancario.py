# variaveis globais
AGENCIA = "0001"
LIMITE = 500

def cadastrar_usuario(usuario):
    nome = input("Nome: ")
    data = input("Data de nascimento: ")
    cpf = input("CPF: ")
    if cpf in usuario:
        print("CPF já cadastrado!")
        return
    else:
        logradouro = input("Logradouro: ")
        numero_casa = input("Numero da casa: ")
        bairro = input("Bairro: ")
        cidade = input("Cidade: ")
        estado = input("Estado: ")
        novo_usuario = {
        "nome": nome,
        "data_nascimento": data,
        "endereco": {
            "logradouro": logradouro,
            "numero": numero_casa,
            "bairro": bairro,
            "cidade": cidade,
            "estado": estado
        }
    }
    usuario[cpf] = novo_usuario
    return cpf

def trocar_de_usuario():
    return input("Insira seu CPF: ")

def conta_corrente(cpf, usuario):
    global AGENCIA
    if usuario[cpf].get("conta"):
        numero_total_contas = len(usuario[cpf]["conta"]) + 1
    else:
        numero_total_contas = 1
    if cpf in usuario:
        nova_conta =  {
            "numero_conta": numero_total_contas,
            "agencia": AGENCIA,
            "saldo": 0,
            "extrato": ""
        }
        if numero_total_contas == 1:
            usuario[cpf].setdefault("conta", [nova_conta])
        else:
            usuario[cpf]["conta"].append(nova_conta)
        print(f"Conta {numero_total_contas} criada!")
    else:
        print("CPF não cadastrado!")
    
    print(usuario[cpf]["conta"])
    return numero_total_contas

def imprime_contas_usuario(cpf, usuario):
    print(usuario[cpf]["conta"])

def trocar_de_conta(cpf, usuario):
    print("Escolha o numero da conta para qual deseja trocar")
    imprime_contas_usuario(cpf, usuario)
    escolha = input("0 - Cancelar a operação\n")
    
    if escolha != '0':
         for conta in usuario[cpf].get("conta", []):
            print(conta)
            return escolha
    elif escolha == '0':
        print("Operação cancelada!")
    else:
        print("Não foi possível realizar a operação.")

def deposito(valor):
    global contas
    global pos_conta_vetor
    global pos_cpf_vetor
    pos_cpf_vetor = int(pos_cpf_vetor)
    pos_conta_vetor = int(pos_conta_vetor)
    print(type(pos_conta_vetor))
    print(type(pos_cpf_vetor))
    if valor > 0:
        print(f"posicao cpf {pos_cpf_vetor} posicao conta {pos_conta_vetor}")
        contas[pos_cpf_vetor][pos_conta_vetor]["saldo"] += valor
        contas[pos_cpf_vetor][pos_conta_vetor]["extrato"].append(f"Depósito de R${valor}")
    else:
        print("Deposite valor maior que 0")


def saque(valor):
    global contas
    global pos_conta_vetor
    global pos_cpf_vetor
    pos_cpf_vetor = int(pos_cpf_vetor)
    pos_conta_vetor = int(pos_conta_vetor)
    if valor > 0:
        contas[pos_cpf_vetor][pos_conta_vetor]["saldo"] -= valor
        contas[pos_cpf_vetor][pos_conta_vetor]["extrato"].append(f"Saque de R${valor}")
    else:
        print("Saque um valor maior que 0")

def imprime_extrato():
    print(contas[pos_cpf_vetor][pos_conta_vetor]["extrato"])

def menu(usuario, cpf, conta):
    while True:
        print("\n__________________MENU________________")
        print("0-Sair\n1-Cadastrar novo usuario")
        if usuario:
            print("2-Criar conta corrente")
        if len(usuario) >= 2:
            print("3-Trocar de usuario")
        if usuario.get(cpf) and usuario[cpf].get("conta"):
            print("4-Trocar de conta\n5-Depositar\n6-Sacar\n7-Extrato")
        menu = input("Escolha uma opção\n")
        if menu == '0':
            break
        elif menu == '1':
            cpf = cadastrar_usuario(usuario)
        elif menu == '2':
            conta = conta_corrente(cpf, usuario)
        elif menu == '3' and len(usuario) >= 2:
            cpf = trocar_de_usuario(cpf, usuario)
        elif menu == '4' and cpf:
            print(usuario)
            conta = trocar_de_conta(usuario, cpf)
            print(conta)
            print(type(conta))
        elif menu == '5':
            valor = float(input("Valor para depositar: "))
            deposito(cpf, valor, conta)
        elif menu == '6':
            valor = float(input("Valor para sacar"))
            saque(cpf, valor, conta)
            
def main():
    cpf = None
    conta = None
    usuario = {}
    menu(usuario, cpf, conta)

main()