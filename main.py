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
            
    def __str__(self):
        print("Tengo", self.ruedas, "ruedas y mi velocidad actual es: ", self.v )
    
    #Esta funcion compara si 2 bicis son iguales. La primera (self) es la bici que llama a la funcion.
    #La segunda (abc) es con la que comparo a la primer bici. 
    
    def __eq__(self, abc):
        print (self.ruedas == abc.ruedas and self.color == abc.color and self.v == abc.v)
        
    def multiplicar(self, abc):
        b3 = Bicicleta(self.ruedas * abc.ruedas, "negra", 5)
        print(b3.ruedas)
            
bicicleta = Bicicleta(2, "roja", 78)

b1 = Bicicleta(2, "azul", 5)
b2 = Bicicleta(540, "azul", 5)

#Si bien __eq__ recibe 2 parametros, en el parentesis solo va 1, que es el parametro (abc).
#Esto es asi porque el parametro self esta fuera del parentesis, ya que (en este caso) 
#self es b1.
b1.__eq__(b2)
b2.multiplicar(b1)
#print(bicicleta)

bicicleta.subir_velocidad()
bicicleta.subir_velocidad()
bicicleta.subir_velocidad()

#print("Velocidad actual: " ,bicicleta.v)
bicicleta.__str__()




bicicleta2 = Bicicleta(2, "roja", 3)

bicicleta2.bajar_velocidad()
bicicleta2.bajar_velocidad()
bicicleta2.bajar_velocidad()
bicicleta2.bajar_velocidad()
print("Velocidad actual: " ,bicicleta2.v)

##########Ejercicio de polimorfismo############################################

USO_DE_TINTA = 1
SIN_TINTA    = 0
CAPACIDAD_MAXIMA = 5

#Instancia de creacion de la clase Util
class Util():
    def __init__(self,grosor,color,tinta):
        self.grosor = grosor
        self.color  = color
        self.tinta  = tinta
        
    #Creacion del metodo escribir()
    def escribir(self):
        if(tinta > SIN_TINTA):
            self.tinta -= USO_DE_TINTA
        else:
            print("Se acabo la tinta/mina. Cambia de cartucho")

class Lapicera(Util):
    pass

class Lapiz(Util):
    pass

class Marcador(Util):
    pass

lapicera = Lapicera(4,"azul oscuro",100)
lapiz    = Lapiz(2,"grafito",1000000)
marcador = Marcador(10,"verde",50)

class Cartuchera:
    def __init__(self):
        self.capacidad = []
    
    def agregarUtil(self, util):
        self.capacidad.append(util)
"""
        if(self.capacidad < CAPACIDAD_MAXIMA)
           self.capacidad.append(util)
        else:
            print("Cartuchera llena")
"""
cartuchera = Cartuchera()
cartuchera.agregarUtil(marcador)
cartuchera.agregarUtil(lapiz)
cartuchera.agregarUtil(lapicera)
cartuchera.agregarUtil(marcador)

print(cartuchera) #Esto me imprime el objeto cartuchera pero quiero que me imprima la lista "capacidad" que contiene a los objetos !!
