def salvar_carro(marca, modelo, ano, placa):
    print(f"Carro inserido marca {marca}, modelo: {modelo} ano: {ano}, placa: {placa}")
    
salvar_carro("FIAT", "Palio", 1999, "ABC-1234")
salvar_carro(ano=1999, placa="ABC-1234", marca="FIAT", modelo="Palio" )