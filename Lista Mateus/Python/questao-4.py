class Animal:
    def __init__(self, nome):
        self.nome = nome
    def som(self):
        raise NotImplementedError("Metodo som não implementado")

class Cachorro(Animal):
    def som(self):
        return f"{self.nome} Au au!"

class Gato(Animal):
    def som(self):
        return f"{self.nome} Miau!"


meu_cachorro = Cachorro("Bolinha")
meu_gato = Gato("Garfield")
print(meu_cachorro.som())  
print(meu_gato.som())      