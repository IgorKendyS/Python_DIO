contatos = {
    "igor@gmail.com" : {"nome":"Igor", "telefone": "9978-7245"},
    "kendy@gmail.com" : {"nome":"Kendy", "telefone": "9958-7225"},
    "benjamin@gmail.com" : {"nome":"Benjamin", "telefone": "9911-7277"},
    "elis@gmail.com" : {"nome":"Elis", "telefone": "9978-6241", "extra": {"a": 1}},
}

# .clear

# .copy

copia = contatos.copy()

for chave, valor in contatos.items():
    print(chave,valor)
    
# .fromkeys

dicio = dict.fromkeys(["nome", "telefone"])

dicio2 = dict.fromkeys(["nome", "telefone"], "vazio")

print("\ndicio: ")
for chave, valor in dicio.items():
    print(chave, valor)

print("\ndicio2: ")
for chave, valor in dicio2.items():
    print(chave, valor)
    
# get
print("\nGET")
print(contatos.get("chave"))
print(contatos.get("chave", "valor não encontrado!"))
print(contatos.get("nome"))
print(contatos.get("igor@gmail.com", {}))

# items
print("\nITEMS")
print(contatos.items())

# keys
print("\nKEYS")
print(contatos["igor@gmail.com"].keys())

# pop
print("\nPOP")
print(contatos.pop("igor@gmail.com"))
print(contatos["elis@gmail.com"].pop("elis@gmail.com", {}))
print(contatos.items())

# setdefault
print("\nSETDEFAULT")
cadastro = {"nome": "Leonardo", "email": "leo@gmail.com"}

cadastro.setdefault("nome", "Eduardo")

cadastro.setdefault("data_nascimento", "00/00/0000")

print(cadastro.items())

# update
print("\nUPDATE")
contatos.update({"benjamin@gmail.com": {"nome":"Benja"}})
contatos.update({"gabriel@gmail.com": {"nome":"Gabriel"}})
print(contatos.items())

# in
print("\nIN")
print("nome" in contatos)
print("benjamin@gmail.com" in contatos)
print("nome" in contatos["kendy@gmail.com"])
print("endereco" in contatos["kendy@gmail.com"])

# del
del contatos["elis@gmail.com"]["extra"]
del contatos["kendy@gmail.com"]
print(contatos.items())
# paga o dicionario
del contatos
#print((contatos.items()))
