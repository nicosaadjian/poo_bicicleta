V_MINIMA = 0
V_MAXIMA = 80
V_INCREMENTO = 1

class Bicicleta:
    def __init__(self, ruedas, color, v):
        self.ruedas = ruedas
        self.color  = color
        self.v      = v 
    
    def subir_velocidad(self):
        if(self.v < V_MAXIMA):
            self.v += V_INCREMENTO
        else: 
            print("Velocidad máxima alcanzada!! Disminuya la velocidad!")
            
    def bajar_velocidad(self):
        if(self.v > V_MINIMA):
            self.v -= V_INCREMENTO
        else:
            print("La velocidad es 0. Empiece a pedalear")
            
bicicleta = Bicicleta(2, "roja", 78)
#print(bicicleta)

bicicleta.subir_velocidad()
bicicleta.subir_velocidad()
bicicleta.subir_velocidad()

print("Velocidad actual: " ,bicicleta.v)

bicicleta2 = Bicicleta(2, "roja", 3)

bicicleta2.bajar_velocidad()
bicicleta2.bajar_velocidad()
bicicleta2.bajar_velocidad()
bicicleta2.bajar_velocidad()
print("Velocidad actual: " ,bicicleta2.v)
