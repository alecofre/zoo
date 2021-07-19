from animal import Animal

class Conejo(Animal):
    def __init__(self, nombre, edad, nivel_salud, nivel_felicidad, tipo):
        super().__init__(nombre, edad, nivel_salud, nivel_felicidad, tipo)