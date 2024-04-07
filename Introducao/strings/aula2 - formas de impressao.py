# old style (desuso)
""" nome = "Igor"
idade = 24
profissao = "Programador"
linguagem = "Python"

# dicionario

pessoa = {"nome": "Igor", "idade": 28}

print("Olá, me chamo %s. Tenho %d anos, atualmente sou %s, estou no processo de aprendizado sobre a linguagem %s."% (nome, idade, profissao, linguagem)) 

print("Olá, me chamo {}. Tenho {} anos, atualmente sou {}, estou no processo de aprendizado sobre a linguagem {}.".format(nome, idade, profissao, linguagem)) 

print("Olá, me chamo {1}. Tenho {2} anos, atualmente sou {3}, estou no processo de aprendizado sobre a linguagem {0}.".format(linguagem, nome, idade, profissao))

print("Olá, me chamo {nome1}. Tenho {idade1} anos, atualmente sou {profissao1}, estou no processo de aprendizado sobre a linguagem {linguagem1}.".format(nome1="nome", idade1=idade, profissao1=profissao, linguagem1 = linguagem))

print("Olá, me chamo {nome1}. Tenho {idade1} anos, atualmente sou {profissao1}, estou no processo de aprendizado sobre a linguagem {linguagem1}.".format(**pessoa))

#mais utilizado
print(f"Olá, me chamo {nome}. Tenho {idade} anos, atualmente sou {profissao}, estou no processo de aprendizado sobre a linguagem {linguagem}.") """

PI = 3.14159

# dois numeros depois da virgula
print(f"Valor de PI: {PI:.2f}")

#adiciona 10 casas antes da virvula
print(f"Valor de PI: {PI:10.2f}")