#!/usr/bin/python3
import os


class Fichier:
    def __init__(self, Tfichier:str):
        self.fichier = Tfichier
    
    
    def fichierExiste(self):
        if os.path.exists(self.fichier):
            return True
        else:
            return "fichier inexistant"
        
    
    def lireFichier(self):
        if os.path.exists(self.fichier):
            sfichier = open(self.fichier, 'r').__enter__()
            try:
               return sfichier.read()
            except:
                return "impossible de lire le fichier"
            finally:
                sfichier.__exit__()
        else:
            return "fichier inexistant"
    
    
    def ecrireDansFichier(self, ecrisUser:str):
        if os.path.exists(self.fichier):
            sfichier = open(self.fichier,'a').__enter__()
            try:
                return sfichier.write(str(ecrisUser))
            except:
                return "impossible de lire le fichier"
            finally:
                sfichier.__exit__()
        else:
            return "fichier inexistant"
            

    def suppFichier(self):
        if os.path.exists(self.fichier):
            return os.remove(self.fichier)
        else:
            return "fichier inexistant"


fichierT = Fichier('jeedd.txt')
#print(fichierT.lireFichier())
#fichierT.ecrireDansFichier(1)
print(fichierT.lireFichier())

