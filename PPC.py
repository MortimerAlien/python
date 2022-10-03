#!/usr/bin/python3
from random import choice


def choixUserPossi(listeChoix:list)->int:
    cpt = 0
    for valeur in listeChoix:
        print("{} - {}\n".format(cpt,valeur))
        cpt += 1
    lchoixUser = input("que choisissez vous ? (entrez le chiffre correspondant)\n")
    try:
        lchoixUser = int(lchoixUser)
        if lchoixUser > 3:
            print("merci de rentrez un chiffre entre 1 et 3\n")
            return choixUserPossi(listeChoix)
        return lchoixUser
    except:
        print("merci de rentrez un chiffre")
        return choixUserPossi(listeChoix)


def continuer()->str:
    continuerPartie = input("voulez vous rejouez ? (O/N)\n")
    if continuerPartie != 'N' and continuerPartie != 'O':
        return continuer()
    else:
        return continuerPartie
    

if __name__ == '__main__':
    nomUser = input("entrez votre nom : \n")
    print("Bienvue dans le jeu du pierre feuille ciseaux {}\n".format(nomUser))
    continuerPartie = 'O'
    while continuerPartie != 'N':
        listeDesChoix = ['pierre', 'feuille' , 'ciseau']
        choixUser = choixUserPossi(listeDesChoix)
        print("vous avez choisis {}\n".format(listeDesChoix[choixUser]))
        choixIa = choice(listeDesChoix)
        print("ia a choisis {}\n".format(choixIa))
        if (choixIa == "pierre" and choixUser == "ciseau") or (choixIa == "ciseau" and choixUser == "feuille"):
            print("vous avez perdu\n")
        elif choixIa == choixUser:
            print("égalité\n")
        else:
            print("vous gagnez\n")
        continuerPartie = continuer()
