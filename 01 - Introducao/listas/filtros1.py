numeros = list(range(0,30,3))


""" 
pares = []
for numero in numeros:
    if numero%2 == 0:
        pares.append(numero) """
        
pares = [numero for numero in numeros if numero%2 == 0]

print(pares)