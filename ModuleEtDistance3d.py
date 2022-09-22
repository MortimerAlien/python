#!/usr/bin/python3
import numpy as np

class Point:
    def __init__(self, x, y, z):
        """
        initialisation d'un point dans l'espace
        """
        self.x = x
        self.y = y
        self.z = z
    
        
    def __str__(self, other = None):
        """
        représentations d'un point dans l'espace
        """
        if other is None:
            other = Point(self.x, self.y, self.z)
        return "Point ({}, {}, {})\n".format(other.x, other.y, other.z)

    
    def __add__(self, other):
        """
        opérateurs d'additions'
        """
        return Point(self.x + other.x,
                     self.y + other.y,
                     self.z + other.z)
    
    
    def __sub__(self, other):
        """
        opérateurs de soustraction
        """
        return Point(self.x - other.x,
                     self.y - other.y,
                     self.z - other.z)
    
    
    def __mul__(self, scalaire):
        """
        opérateurs de multiplication via un scalaire(nombre)
        """
        return Point(self.x * scalaire,
                     self.y * scalaire,
                     self.z * scalaire)
    
    
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
    
    
p = Point(1,2,3)
p2 = Point(2,3,4)
