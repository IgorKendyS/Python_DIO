# metodos count, index, len
#boa pratica terminar com ,
frutas = ("laranja", "pera", "uva",)
print(frutas)

letras = tuple("python")
print(letras)

numeros = tuple([1, 2, 3, 4])
print(numeros)

pais = ("Brasil",)
print(pais)

matriz = (
    (1, 2, "p",),
    ("gold", 8, "9",),
)
print(matriz)

for item in matriz:
    print(item)
    
for indice, item in enumerate(frutas):
    print(f"{indice}: {item}")