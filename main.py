V_MINIMA = 0
V_MAXIMA = 80
V_INCREMENTO = 1

class Bicicleta:
    def __init__(self, ruedas, color, v):
        self.ruedas = ruedas
        self.color  = color
        self.v      = v 
    
    def subir_velocidad(self):
        self.v += V_INCREMENTO
    
    def bajar_velocidad(self):
        self.v -= V_INCREMENTO

bicicleta = Bicicleta(2, "roja", 15)
#print(bicicleta)

bicicleta.subir_velocidad()
bicicleta.subir_velocidad()
bicicleta.subir_velocidad()
bicicleta.subir_velocidad()
bicicleta.subir_velocidad()
bicicleta.subir_velocidad()
bicicleta.subir_velocidad()
print("Velocidad actual: " ,bicicleta.v)

bicicleta.bajar_velocidad()
bicicleta.bajar_velocidad()
bicicleta.bajar_velocidad()
bicicleta.bajar_velocidad()
print("Velocidad actual: " ,bicicleta.v)
