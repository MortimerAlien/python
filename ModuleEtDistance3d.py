#!/usr/bin/python3
import numpy as np

class Point:
    
    def __init__(self, x, y, z):
        """
        méthode d'initialisation d'un point dans l'espace
        """
        self.x = x
        self.y = y
        self.z = z
    
    
    def afficher(self):
        """
            affiche le point générer dans l'espace
        """
        print("Point ({}, {}, {})\n".format(self.x, self.y, self.z))
        
    
    def module(self):
        """

        calcul le module d'un point dans l'espace

        """
        mod = np.sqrt(pow(self.x,2) + pow(self.y,2) + pow(self.z,2)
        
        return mod
    
    
    def distance(self,autrePoint):
        """
            calcul la distance par rapport à un autre point dans l'espace
        """
        dst = np.sqrt((pow(self.x - autrePoint.x,2),pow(self.y - autrePoint.y,2),pow(self.z - autrePoint.z,2)))
        
        return dst
    
    def distance_et_module(self, other=None):
        """
        calcul la distance par rapport à un autre point ou par défaut à l'origine dans l'espace
        """
        if other is None:
            other = Point(0,0,0)
        dst = np.sqrt((pow(self.x - other.x,2),pow(self.y - other.y,2),pow(self.z - other.z,2)))
        
        return dst
    
    
p = Point(1,2,3)
p2 = Point(2,3,4)
p.afficher()
p.module()
p.distance(p2)
p.distance_et_module()
p.distance_et_module(p2)
