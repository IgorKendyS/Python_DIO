def listar_contas_por_id(usuario, cpf):
    contas = []
    for usuario_id, dados_usuario in usuario.items():
        if usuario_id == cpf:
            for conta in dados_usuario['conta']:
                contas.append(conta)
    return contas

dados_usuarios = {
    '24485025771': {
        'nome': 'Igor Sakaguchi',
        'data_nascimento': '14042000',
        'endereco': {'logradouro': 'Francisco', 'numero': '1223', 'bairro': 'Morumbi', 'cidade': 'Birigui', 'estado': 'SP'},
        'conta': [
            {'numero_conta': 1, 'agencia': '0001', 'saldo': 0, 'extrato': ''},
            {'numero_conta': 2, 'agencia': '0001', 'saldo': 0, 'extrato': ''},
            {'numero_conta': 3, 'agencia': '0001', 'saldo': 0, 'extrato': ''}
        ]
    }
}

id_usuario = '24485025771'

contas_do_usuario = listar_contas_por_id(dados_usuarios, id_usuario)

for conta in contas_do_usuario:
    print(conta)