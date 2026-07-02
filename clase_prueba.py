
class Perro:
    def __init__(self, nombre):
        self.nombre = nombre

    def ladrar(self):
        print(f"{self.nombre} dice: ¡Guau!")

perro1 = Perro("Luna")
perro2 = Perro("Thor")

perro1.ladrar()
perro2.ladrar()

