from animal import Animal

class Leon(Animal):
    def __init__(self, nombre, edad, nivel_salud, nivel_felicidad,  melena):
        super().__init__(nombre, edad, nivel_salud, nivel_felicidad)
        self.melena = melena
        
    def alimentacion(self, comida):
        if comida <= 5:
            self.nivel_salud += 5
            self.nivel_felicidad += 2
        elif comida <= 10:
            self.nivel_salud += 10
            self.nivel_felicidad += 5
        elif comida < 20:
            self.nivel_salud += 15
            self.nivel_felicidad += 8
        else:
            self.nivel_salud += 20
            self.nivel_felicidad += 10

        return self

    def display_info(self):
        info = super().display_info()
        if self.melena:
            info = info + " y tiene melena"
        else:
            info = info + " y no tiene melena"
        return info



