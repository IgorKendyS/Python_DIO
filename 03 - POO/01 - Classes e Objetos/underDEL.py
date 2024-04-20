class Cachorro:
    def __init__(self, nome, cor, acordado=True):
        print("Inicializando a classe... ")
        self.nome = nome
        self.cor = cor
        self.acordado = acordado
        
    def __del__(self):
        print("Removendo a instância da classe.")
        
    def latir(self):
        print("au au")
        
def criar_cachorro():
    c= Cachorro("Zeus", "Branco e preto", False)
    print(c.nome)
        
c = Cachorro('Chappie', 'amarelo')
c.latir()

#criar_cachorro()

print("Ola Mundo")

del c

print("Ola Mundo")
print("Ola Mundo")
print("Ola Mundo")
print("Ola Mundo")
