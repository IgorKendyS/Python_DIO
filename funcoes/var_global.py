# pratica a ser evitada
salario = 2000

def salario_bonus(bonus):
    global salario
    # lista.append(2)
    lista_aux = lista.copy()
    lista_aux.append(2)
    print(lista_aux)
    salario += bonus
    return salario

""" def salario_bonus(bonus, lista2):
    global salario
    # lista.append(2)
    lista_aux = lista2.copy()
    lista_aux.append(2)
    print(lista_aux)
    salario += bonus
    return salario
 """
lista = [1]
print(salario_bonus(500))
# print(salario_bonus(500),lista)
print(lista)
