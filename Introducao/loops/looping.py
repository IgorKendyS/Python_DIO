""" texto = input("Digite uma palavra:")
VOGAIS = "AEIOU"

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end=" ")
    else:
        print() #adiciona quebra de linha

for numero in range(0, 51, 4):
    print(numero, end=" ")

opcao = -1
while opcao !=0:
    opcao = int(input("1-sacar 2-depositar 0-sair"))
    if opcao == 1:
        print("Sacado")
    elif opcao == 2:
        print("Depositado")
else:
    print("Obrigado por usar o programa") """

#break e continue
while 1: #True or 1==1
    senha = int(input("Insira um numero: "))
    if senha == 10:
        break;
    if senha%2 != 0:
        continue
    print(senha)