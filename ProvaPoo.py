'''Crie uma classe base chamada Animal que tenha um método chamado falar, o qual imprime uma mensagem genérica, como "Este animal faz um som." Em seguida, crie duas subclasses chamadas Cachorro e Gato que herdem de Animal. Dentro de cada uma dessas subclasses, sobrescreva o método falar para que ele imprima uma mensagem específica para cada animal. Por exemplo, na classe Cachorro, o método falar pode imprimir "O cachorro late." e, na classe Gato, pode imprimir "O gato mia."'''

class Animal:
    def __init__(self, nome):
        self.nome = nome
        
    def falar(self):
        return 'este animal faz um som'
    
class Gato(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def falar(self):
        return f'o {self.nome} Mia!'    

class Cachorro(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def falar(self):
        return f'o {self.nome} Late!'           



pet_1 = Cachorro('Bill')

pet_2 = Gato('Gates')

print(f'tenho o {pet_1.nome} e o {pet_2.nome}')
print(pet_1.falar())
print(pet_2.falar())