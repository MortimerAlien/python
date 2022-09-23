#!/usr/bin/python3
import numpy as np


class AffichableMixin:
    str_format = "Venus"
    
    def __str__(self):
        return self.str_format.format(self=self)


class NomAutomatiqueMixin:
    ordinal = 65
    
    def __init__(self):
        self.lettre = chr(NomAutomatiqueMixin.ordinal)
        NomAutomatiqueMixin.ordinal += 1


class Point(AffichableMixin, NomAutomatiqueMixin):
    
    str_format = "Point {self.lettre} ({self.x}, {self.y}, {self.z})"
    
    def __init__(self, x, y, z):
        """
        initialisation d'un point dans l'espace
        """
        super().__init__()
        self.x = x
        self.y = y
        self.z = z
        
    
    def __add__(self, other):
        """
        opérateurs d'additions'
        """
        self.x += other.x
        self.y += other.y
        self.z += other.z
        
        return self
    
    
    def __sub__(self, other):
        """
        opérateurs de soustraction
        """
        self.x -= other.x
        self.y -= other.y
        self.z -= other.z
        
        return self
   
    
    
    def __mul__(self, scalaire):
        """
        opérateurs de multiplication via un scalaire(nombre)
        """
        self.x *= scalaire
        self.y *= scalaire
        self.z *= scalaire
        
        return self
    
    
    def module(self):
        """

        calcul le module d'un point'

        """
        mod = np.sqrt(pow(self.x,2) + pow(self.y,2))
        
        return mod
    
    
    def distance(self,autrePoint):
        """
            calcul la distance par rapport à un autre point.
        """
        dst = np.sqrt((pow(self.x - autrePoint.x,2),pow(self.y - autrePoint.y,2),pow(self.z - autrePoint.z,2)))
        
        return dst
    
    
    def distance_et_module(self, other=None):
        """
        calcul la distance par rapport à un autre point ou par défaut à l'origine'
        """
        if other is None:
            other = Point(0,0,0)
        dst = np.sqrt((pow(self.x - other.x,2),pow(self.y - other.y,2),pow(self.z - other.z,2)))
        
        return dst


class Point2D(Point):
    
    str_format = "Point2D {self.lettre} ({self.x}, {self.y})"
    
    def __init__(self,x,y):
        super().__init__(x,y,0)




p = Point(1,2,3)
p += Point(2,3,4)
print(p)
p2d = Point2D(1,2)
p2d += Point2D(3,0)
print(p2d)
