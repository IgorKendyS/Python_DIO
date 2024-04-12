usuario = {}
contas = []
numero_total_contas = 0
def cadastrar_usuario():
    global usuario
    nome = input("Nome: ")
    data = input("Data de nascimento: ")
    cpf = int(input("CPF: "))
    if cpf in usuario:
        "CPF já cadastrado!"
        return
    else:
        logradouro = input("Logradouro: ")
        numero_casa = input("Numero da casa: ")
        bairro = input("Bairro: ")
        cidade = input("Cidade: ")
        estado = input("Estado: ")
        usuario.update({cpf:{"nome":nome, "data_nascimento": data, "endereco":{"logradouro": logradouro,"numero": numero_casa, "bairro": bairro, "cidade": cidade, "estado": estado}}})
    print(usuario)

def conta_corrente():
    global usuario
    global contas
    global numero_total_contas
    print(usuario)
    numero_da_conta = numero_total_contas + 1
    agencia = ("0001",)
    cpf = input("Qual seu CPF?\n")
    if cpf in usuario.keys():
        contas.append([numero_da_conta, agencia, cpf])
        print(contas)
    else:
        print("CPF não cadastrado!")

def trocar_de_usuario():
    cpf = input("CPF: ")

#def saque(cpf):

cadastrar_usuario()
conta_corrente()

print("__________________MENU________________")
print("1-Cadastrar usuario\n2-criar conta\n")