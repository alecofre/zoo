from vaca import Vaca
from conejo import Conejo
from tigre import Tigre
from leon import Leon
from animal import Animal

class Zoo:

    def __init__(self, nombre, lista_animales = []):
        self.nombre = nombre
        self.lista_animales = lista_animales

    def agregar_animal(self, nuevo_animal):
            for animal in self.lista_animales:
                if animal.nombre == nuevo_animal.nombre:
                    return False
            self.lista_animales.append(nuevo_animal)
            return True

    def eliminar_animal(self, nombre):
        for animal in self.lista_animales:
            if animal.nombre == nombre:
                self.lista_animales.remove(animal)
                return True
        return False

    def print_all_info(self):
        print("-"*30, self.nombre, "-"*30)
        for animal in self.lista_animales:
            print(animal.display_info())

    def listar_herbivoros(self):
        herbivoros = []
        for animal in self.lista_animales:
            if isinstance(animal,Conejo) or isinstance(animal,Vaca):
                herbivoros.append(animal)
        return herbivoros

    def listar_carnivoros(self):
        carnivoros = []
        for animal in self.lista_animales:
            if isinstance(animal,Leon) or isinstance(animal,Tigre):
                carnivoros.append(animal)
        return carnivoros

    def print_herbivoros(self):
        print("-"*30, self.nombre," HERBIVOROS ", "-"*30)
        for animal in self.listar_herbivoros():
            print(animal.display_info())

    def print_carnivoros(self):
        print("-"*30, self.nombre," CARNIVOROS ", "-"*30)
        for animal in self.listar_carnivoros():
            print(animal.display_info())


# zoo1 = Zoo("mio")
# zoo1.agregar_animal(Leon('lio',4,5,6,True))
# zoo1.agregar_animal(Tigre('Sherkan',6,7,8))

# zoo1.print_all_info()
# input('Presione una tecla para continuar...')

# lista = zoo1.listar_carnivoros()
# print(lista)
# input('Presione una tecla para continuar...')
