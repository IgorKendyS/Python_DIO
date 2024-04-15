# Dados estáticos para teste
usuario = {
    "12345678900": {
        "nome": "Fulano",
        "endereco": {
            "logradouro": "Rua A",
            "numero": "123",
            "bairro": "Centro",
            "cidade": "Cidade A",
            "estado": "Estado A"
        }
    },
    "98765432100": {
        "nome": "Ciclano",
        "endereco": {
            "logradouro": "Rua B",
            "numero": "456",
            "bairro": "Periferia",
            "cidade": "Cidade B",
            "estado": "Estado B"
        }
    }
}

contas = [
    ["12345678900", [
        {"numero_conta": 1, "agencia": "0001", "saldo": 100.00, "extrato": "Depósito inicial"},
        {"numero_conta": 2, "agencia": "0001", "saldo": 50.00, "extrato": "Depósito inicial"}
    ]],
    ["98765432100", [
        {"numero_conta": 1, "agencia": "0001", "saldo": 200.00, "extrato": "Depósito inicial"},
        {"numero_conta": 2, "agencia": "0001", "saldo": 150.00, "extrato": "Depósito inicial"},
        {"numero_conta": 3, "agencia": "0001", "saldo": 300.00, "extrato": "Depósito inicial"}
    ]]
]

# Definições de funções
def imprime_contas_usuario(cpf):
    global contas
    for item in contas:
        if item[0] == cpf:
            print(f"Contas do usuário com CPF {cpf}:")
            for conta in item[1]:
                print(f"Numero da conta: {conta['numero_conta']}, Agencia: {conta['agencia']}, Saldo: {conta['saldo']}, Extrato: {conta['extrato']}")
            return item[1]  # Retorna a lista de contas do usuário
    else:
        print("CPF não encontrado ou usuário não possui contas.")
        return None

def trocar_de_conta(cpf, imprime_contas):
    contas_usuario = imprime_contas(cpf)
    if contas_usuario:
        numero_da_conta = int(input("Escolha para qual conta você deseja trocar: "))
        if 1 <= numero_da_conta <= len(contas_usuario):
            posicao_vetor_conta = numero_da_conta - 1  # Ajusta para o índice baseado em zero
            print(f"Você escolheu a conta {numero_da_conta}")
            # Use a posicao_vetor_conta conforme necessário
        else:
            print("Número de conta inválido.")
    else:
        print("Não foi possível trocar de conta.")

# Testando a função trocar_de_conta com os dados estáticos
cpf_teste = "12345678900"
print(len(contas))
trocar_de_conta(cpf_teste, imprime_contas_usuario)

