#!/usr/bin/python3
def genererNbrePremier(p:int)->list[int]:
    nbrePremier = []
    for i in range(2,p):
        premierF = True
        for j in range(2,i):
            if i % j == 0:
                premierF = False
        if premierF:
            nbrePremier.append(i)
    return nbrePremier
