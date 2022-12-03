from math import pi

class Circle():
    def __init__(self,color = 'red', radius = 1.0):
        self.__color = color
        self.__radius=float(radius)
    
    def getRadius(self):
        return self.__radius
    
    def setRadius(self,radius=1.0):
        self.radius=float(radius)
    
    def getColort(self):
        return self.__color

    def setColor(self,color):
        self.__color = color

    def toString(self):
        return {"Class":self.__class__.__name__, "Radius": self.__radius, "Color":self.__color}

    def getArea(self):
        self.__Area = self.__radius**2 * pi
        return self.__Area
