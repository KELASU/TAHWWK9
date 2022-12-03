from Circle import Circle

class Cylinder(Circle):
    def __init__(self,height=1.0,radius=1.0,color="red"):
        self.__height = height
        self.__radius = radius
        self.__color = color

    def getHeight(self):
        return self.__height

    def setHeight(self,height):
        self.__height=height
    
    def toString(self):
        dictionary = super().toString()
        dictionary.update({"Height": self.__height})
        return dictionary
    
    def getVolume(self):
        Volume = self.__Area * self.__height
        return Volume
