contatos = {
    "igor@gmail.com" : {"nome":"Igor", "telefone": "9978-7245"},
    "kendy@gmail.com" : {"nome":"Kendy", "telefone": "9958-7225"},
    "benjamin@gmail.com" : {"nome":"Benjamin", "telefone": "9911-7277"},
    "elis@gmail.com" : {"nome":"Elis", "telefone": "9978-6241", "extra": {"a": 1}},
}

print(contatos["igor@gmail.com"]["telefone"])
print(contatos["elis@gmail.com"]["extra"]["a"])

for chave in contatos:
    print(chave, contatos[chave])
    
for chave, valor in contatos.items():
    print(chave, valor)