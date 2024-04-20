class Estudante:
    escola = "DIO"
    
    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula
        
    def __str__(self) -> str:
        return f"{self.nome} - {self.matricula} - {self.escola}"
    
def mostra_valores(*objs):
    for obj in objs:
        print(obj)

aluno_1 = Estudante("Igor", 1)
aluno_2 = Estudante("Benjamin", 2)
mostra_valores(aluno_1, aluno_2)


Estudante.escola = "Python"
aluno_3 = Estudante("Chappie", 3)
mostra_valores(aluno_1, aluno_2, aluno_3)
