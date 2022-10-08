#!/usr/bin/python3
from random import choice


def DemanderMotsDeviner()->str:
    demander = input("donner un mot a deviner: \n")
    return demander

def lettreUser()->str:
    demander = input("entrez une lettre: ")
    if len(demander) > 1:
        return lettreUser()
    return demander


def demanderChiffre()->int:
    chiffreUser = input("entrez un chiffre : \n")
    try:
        chiffreUser = int(chiffreUser)
        if chiffreUser != 1 and chiffreUser != 2:
            return demanderChiffre()
        return chiffreUser
    except:
        return demanderChiffre()
        

def rejouer()->str:
    demander = input("rejouer ? (y/n)")
    if demander.lower() == 'y' or 'n':
        return demander.lower()
    return rejouer()


def IaGenererMots()->str:
    """
    j'ai commencer l'implémentation de la generations de mots (Alpha)

    """
    prefixe = ["psycho", "anti","archéo", "calc"]
    suffixe = ["logie","oide", "pode"]
    return "".join([choice(prefixe), choice(suffixe)])


def jeux(motsDeviner:str)->str:
    affichage = ""
    motsUser = ""
    for i in range(len(motsDeviner)):
        affichage += "_"
    print(affichage)
    chance = 10
    while chance != 0 and motsUser != motsDeviner:
        choisirLettre = lettreUser()
        affichage = list(affichage)
        if choisirLettre in motsDeviner:
            affichage[motsDeviner.index(choisirLettre)] = choisirLettre
            motsUser += choisirLettre
        else:
            print("pas dans le mot\n")
            chance -= 1
        print("".join(affichage))
    if chance == 0:
        print("perdu")
    else:
        print("gagnez")
        
        
    
    
if __name__ == '__main__':
    rejouerUser = 'y'
    while rejouerUser == 'y':
        print("choix mode de jeux: \n1 - vous jouez à deux ou plus\n2 - vous jouer contre l'ia (alpha)\n")
        demanderUser = demanderChiffre()
        if demanderUser == 1:
            motsAdeviner = DemanderMotsDeviner()
        else:
            motsAdeviner = IaGenererMots()

        print(motsAdeviner)
        jeux(motsAdeviner)
        rejouerUser = rejouer()
    print("arret du jeux")
