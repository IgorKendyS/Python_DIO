lista = [4,5,10,4,87,3,25,3]
# sets - o vetor retornado pode nao estar ordenado
print("SET")
print(lista)
print(set(lista))

print(set("abacaxi"))

print(set(("palio", "gol", "celta", "palio")))

linguagens = {"python", "java", "python"}
print(linguagens)

numeros = {1, 2, 3, 2}
# print(numeros[0]) error

numeros = list(numeros)
print(numeros[0]) 

for indice, num in enumerate(numeros):
    print(f"{indice}: {num}")
    
# union
print("\nUNION")
conj_a = {1,2,1}
conj_b = {2,3,4}
print(conj_a.union(conj_b))

# intersection
print("\nINTERSECTION")
print(conj_a.intersection(conj_b))

# difference
print("\nDIFFRENCE")
print(conj_a.difference(conj_b))

# symmetric_difference
print("\nSYMMETRIC DIFFRENCE")
print(conj_a.symmetric_difference(conj_b))

# subset
print("\nSUBSET")
conjunto = {0,1,2,3,4,5,6,7,8,9}
print(conjunto)
subset = {4, 8, 6}
print(subset)
print(conjunto.issubset(subset))
print(subset.issubset(conjunto))

#superset
print("\nSUPERSET")
print(conjunto.issuperset(subset))
print(subset.issuperset(conjunto))

# isdisjoint
print("\nISDISJOINT")
conjunto_b = {100,200,58}
print(conjunto.isdisjoint(subset))
print(conjunto.isdisjoint(conjunto_b))

# add
print("\nSORTEIO")
sorteio = {1, 5, 6}
print(sorteio)
sorteio.add(25)
print(sorteio)
sorteio.add(18)
print(sorteio)
sorteio.add(5)
sorteio.add(7)
sorteio.add(8)
sorteio.add(55)
print(sorteio)

# copy
print("\nCOPY")
copia = sorteio.copy()
print(copia)

# discard
print("\nDISCARD")
sorteio.discard(18)
print(sorteio)

# pop
print("\nPOP")
print(sorteio.pop())
print(sorteio)

# remove - da erro se n tiver o objeto
print("\nREMOVE")
sorteio.remove(8)
print(sorteio)

# len
print("\nLEN")
print(sorteio)
print(len(sorteio))

# in
print("\nIN")
print(55 in sorteio)
print(27 in sorteio)

# clear
print("\nCLEAR")
sorteio.clear()
print(sorteio)