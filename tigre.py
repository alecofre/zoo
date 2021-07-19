from animal import Animal

class Tigre(Animal):
    def __init__(self, nombre, edad, nivel_salud, nivel_felicidad):
        super().__init__(nombre, edad, nivel_salud, nivel_felicidad)
        
    def alimentacion(self, comida):
        if comida <= 7:
            self.nivel_salud += 7
            self.nivel_felicidad += 4
        elif comida <= 14:
            self.nivel_salud += 14
            self.nivel_felicidad += 7
        elif comida < 22:
            self.nivel_salud += 22
            self.nivel_felicidad += 11
        else:
            self.nivel_salud += 25
            self.nivel_felicidad += 13
        return self
