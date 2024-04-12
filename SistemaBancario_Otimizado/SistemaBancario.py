# variaveis globais
usuario = {}
contas = []
pos_cpf_vetor = 0
pos_conta_vetor = 0
numero_total_contas = 0
AGENCIA = "0001"

def cadastrar_usuario():
    global usuario
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

def conta_corrente(cpf):
    global usuario
    global contas
    global numero_total_contas
    global AGENCIA
    global pos_cpf_vetor
    print(usuario)
    if cpf in usuario:
        nova_conta =  {
            "numero_conta": numero_total_contas + 1,
            "agencia": AGENCIA,
            "saldo": 0,
            "extrato": ""
        }
        x = 0
        for item in contas:
            if item[0] == cpf:
                item[1].append(nova_conta)
                pos_cpf_vetor = item
                break
        else:
            contas.append([cpf, nova_conta])
        numero_total_contas += 1
        print(f"Conta {nova_conta['numero_conta']} criada!")
    else:
        print("CPF não cadastrado!")

def imprime_contas_usuario(cpf):
    global contas
    for item in contas:
        if item[0] == cpf:
            print(f"Contas do usuário com CPF {cpf}:")
            for conta in item[1]:
                print(f"Numero da conta: {conta['numero_conta']}, Agencia: {conta['agencia']}, Saldo: {conta['saldo']}, Extrato: {conta['extrato']}")
            return item[1]
    else:
        print("CPF não encontrado ou usuário não possui contas.")
        return None

def trocar_de_conta(cpf, imprime_contas):
    global pos_conta_vetor
    contas_usuario = imprime_contas(cpf)
    if contas_usuario:
        numero_da_conta = int(input("Escolha para qual conta você deseja trocar: "))
        if 1 <= numero_da_conta <= len(contas_usuario):
            pos_conta_vetor = numero_da_conta - 1 
            print(f"Você escolheu a conta {numero_da_conta}")
        else:
            print("Número de conta inválido.")
    else:
        print("Não foi possível trocar de conta.")

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
    
cpf = None

while True:
    if not cpf:
        print("Ja possui uma conta?\n1-sim\n2-nao")
        menu = input("Escolha uma opção\n")
        if menu == '1':
            cpf = input("Muito bem, poderia informar seu cpf?\n")
        elif menu == '2':
            print("Então vamos cadastrar sua conta")
            cpf = cadastrar_usuario()
            
    print("\n__________________MENU________________")
    print("0-Sair\n1-Cadastrar novo usuario\n2-Criar conta")
    if len(usuario) >= 2:
        print("3-Trocar de usuario")
    if cpf:
        print("4-trocar de conta\n5-Depositar\n6-Sacar\n7-Extrato")
    menu = input("Escolha uma opção\n")
    if menu == '0':
        break
    elif menu == '1':
        cpf = cadastrar_usuario()
    elif menu == '2':
       conta_corrente(cpf)
    elif menu == '3' and len(usuario) >= 2:
        cpf = trocar_de_usuario(cpf)
    elif menu == '4' and cpf:
        trocar_de_conta(cpf,imprime_contas_usuario(cpf))
    elif menu == '5':
        valor = float(input("Valor para depositar: "))
        deposito(valor)
    elif menu == '6':
        valor = float(input("Valor para sacar"))
        saque(valor)