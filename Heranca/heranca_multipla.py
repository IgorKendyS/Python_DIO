class Animal:
    def __init__(self, nro_patas):
        self.nro_patas = nro_patas
        
    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}:{valor}' for chave, valor in self.__dict__.items()])}"

class Mamifero(Animal):
    def __init__(self, cor_pelo, **kw):
        super().__init__(**kw)
        self.cor_pelo = cor_pelo
        
    def __str__(self):
        return __class__.__name__

class Ave(Animal):
    def __init__(self, cor_bico, **kw):
        super().__init__(**kw)
        self.cor_bico = cor_bico
        
    def __str__(self):
        return "ave 42"

class Cachorro(Mamifero):
    pass

class Gato(Mamifero):
    pass

class Leao(Mamifero):
    pass

class Ornitorrinco(Mamifero, Ave):
    def __init__(self, cor_bico, cor_pelo, nro_patas):
        
        #print(Ornitorrinco.__mro__)
        print(Ornitorrinco.mro())
        
        super().__init__(cor_bico=cor_bico, cor_pelo=cor_pelo, nro_patas=nro_patas)
        
    def __str__(self):
        return self.__class__.__name__


gato = Gato(nro_patas=4, cor_pelo='preto')
print(gato)

ornitorrinco = Ornitorrinco(nro_patas=4, cor_pelo="marrom", cor_bico="laranja")
print(ornitorrinco)