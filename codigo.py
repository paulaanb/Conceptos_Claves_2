import math
#Definimos la clase punto

class Punto:
    def __init__(self, coordenada_X=0, coordenada_Y=0):
 
        self.coordenada_X = coordenada_X
        self.coordenada_Y = coordenada_Y
    def __str__(self):
        return  "({}, {})".format(self.coordenada_X, self.coordenada_Y)
#Definimos el cuadrante para poder trabajar con todos los ejes.
    def cuadrante(self):
        if self.coordenada_X > 0 and self.coordenada_Y > 0:
            print("{} pertenece al primer cuadrante".format(self))
        elif self.coordenada_X < 0 and self.coordenada_Y > 0:
            print("{} pertenece al segundo cuadrante".format(self))
        elif self.coordenada_X < 0 and self.coordenada_Y < 0:
            print("{} pertenece al tercer cuadrante".format(self))
        elif self.coordenada_X > 0 and self.coordenada_Y < 0:
            print("{} pertenece al cuarto cuadrante".format(self))
        elif self.coordenada_X != 0 and self.coordenada_Y == 0:
            print("{} se sitúa sobre el eje X".format(self))
        elif self.coordenada_X == 0 and self.coordenada_Y != 0:
            print("{} se sitúa sobre el eje Y".format(self))
        else:
            print("{} se encuentra sobre el origen".format(self))

