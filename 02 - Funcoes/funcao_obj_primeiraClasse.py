def somar (a,b):
    return a+b

def subtrair(a,b):
    return a-b

def exibir_resultado(a,b,funcao):
    resultado = funcao(a,b)
    print(f"O resultado da operacao {a} + {b} = {resultado}")
    
exibir_resultado(10, 9, somar)
exibir_resultado(10, 9, subtrair)

op = somar
exibir_resultado(10, 9, op)
print(op(1, 23))