lista = []

lista.append(1)
print(lista)
lista.append('bola')
print(lista)
lista.append([40,20,30])
print(lista)
lista.append([[8,2],[9,5]])
print(lista)
lista.append(list("python"))
print(lista)

# copy
print("\nCOPY")

copia = lista.copy()
print(copia)
print(id(copia), id(lista))

# count
print("\nCOUNT")
cores = ["vermelho", "amarelo", "azul", "verde", "vermelho"]
print (cores.count("amarelo"))
print(cores.count("vermelho"))

# extend
print("\nEXTEND")
linguagens = ["Python", "JS", "CPP"]
linguagens.extend(["Java", "PHP", "CPP"])
print(linguagens)

# index - encontra o index do primeiro item procurado que aparece 
print("\nINDEX")
print(linguagens.index("CPP"))

# pop
print("\nPOP")
linguagens.pop()
print(linguagens)
linguagens.pop(0)
print(linguagens)

# remove - remove apenas um elemento
print("\nREMOVE")
linguagens.remove("Java")
print(linguagens)

# reverse
print("\nREVERSE")
linguagens.reverse()
print(linguagens)

# sort
print("\nSORT")
linguagens.sort()
print(linguagens)
linguagens.sort(reverse=True)
print(linguagens)
    #ordenar por tamanho da palavra
linguagens.sort(key=lambda x: len(x))
print(linguagens)
linguagens.sort(key=lambda x: len(x), reverse=True)
print(linguagens)

# len
print("\nLEN")
print(len(linguagens))

# sorted
print("\nSORTED")
print(sorted(linguagens, key=lambda x: len(x)))
print(sorted(linguagens, key=lambda x: len(x), reverse=True))
print(sorted(linguagens))

# clear
print("\nCLEAR")

lista.clear()
print(lista)

