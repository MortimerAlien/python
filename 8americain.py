#!/usr/bin/python3
"""




oui je sais x) mais flm de l'opti et je sais plus si j'ai gerer le 1 joueur,
désolé pour les fautes fais à 3h30 du mat




"""
from random import sample, choice
#Max 3 joueurs
"""
1 - gerer les derniers problème exemple pas de partie à 1 joueur
2 - optimiser le code
"""

"""
mettre a jour le dictionnaire avec une liste pour le deck des joueurs
example:
    l = [[],[],[]]
dico[keys] = l[j]
"""

def demander_saisie()->int:
    """
    Returns
    -------
    nbreJoueurs : int
        nomnres de joueurs dans la partie
    """
    nbreJoueurs = input("choisissez un chiffre : \n")
    try:
        nbreJoueurs = int(nbreJoueurs)
        return nbreJoueurs
    except ValueError:
        print("ce n'est pas une bonne saisie, merci de rentrez un nombre\n")
        return demander_saisie()

        
def genererCartes(nomDesJoueurs:list, cartes:list)->dict:
    """
    Parameters
    ----------
    nomDesJoueurs : list
        liste des joueurs
    cartes : list
        cartes du jeux
    Returns
    -------
    CartesJoueurs : dict
        retourne chaque joueurs avec son jeu de cartes

    """
    CartesJoueurs = {}
    for i in nomDesJoueurs:
        CartesJoueurs[i] = sample(cartes,8) + [chr(0x1f0ab),chr(0x1f0bb),chr(0x1f0cb),chr(0x1f0db)]
    return CartesJoueurs


def nomJoueurs(nbreJoueurs:int)->list:
    """
    Parameters
    ----------
    nbreJoueurs : int
        nombres de joueurs dans la partie

    Returns
    -------
    listeJoueurs : list
        liste des joueurs avce leurs noms

    """
    listeJoueurs = []
    for i in range(nbreJoueurs):
        nom = input("entrez un nom de joueurs: \n")
        listeJoueurs.append(nom)
    return listeJoueurs
        

def tourJoueurs(nomDesJ:list)->str:
    """
    Parameters
    ----------
    nomDesJ : list
        listes des joueurs de la parties

    Returns
    -------
    nomJ : str
        nom du joueurs qui doit jouer

    """
    print("qui va jouer : \n")
    nomJ = choice(nomDesJ)
    return nomJ


def addCartes(deckJoueurs:dict,nomJ:str,nbreDeCartes:int)->dict:
    """
    Parameters
    ----------
    deckJoueurs : dict
        le deck du joueurs
    nomJ : str
        le nom du joueurs a qui on ajoute les cartes
    nbreDeCartes : int
        le nombre de cartes a ajouter

    Returns
    -------
    dict
        deck du joueurs après ajouts

    """
    cartes = [chr(x) for x in range(0x1f0a1, 0x1f0DE) if x != 0x1f0af and x != 0x1f0b0 and x != 0x1f0c0 and x != 0x1f0d0]
    l = []
    for indice, cle in deckJoueurs.items():
        if indice == nomJ:
            for i in cle:
                l.append(i)
    for i in sample(cartes,nbreDeCartes):
        l.append(i)
    deckJoueurs[nomJ] = l
    return deckJoueurs


def SpeValet(nomDesJoueurs:list,cpt:int)->str:
    """
    Parameters
    ----------
    nomDesJoueurs : list
        listes des joueurs
    cpt : int
        compteur pour passage a un autre joueurs

    Returns
    -------
    str
        joueurs qui va jouer après passage de tours

    """
    if len(nomDesJoueurs) == 2:
        return nomDesJoueurs[cpt - 1]
    elif cpt >= len(nomDesJoueurs) - 1 or cpt + 1 == len(nomDesJoueurs) - 1: #probleme ici
            print("ok")
            for i in nomDesJoueurs:
                if cpt == nomDesJoueurs.index(i):
                    return nomDesJoueurs[cpt - 1]
    else:
        return nomDesJoueurs[cpt+2]
    

def extractionListes(MapCartes:dict, indice:int)->list:
    """
    Parameters
    ----------
    MapCartes : dict
        map des cartes avec chaque couleurs
    indice : int
        position de la liste a extraire

    Returns
    -------
    list
        liste extraite

    """
    cpt = 0
    for i in MapCartes.values():
        if indice == cpt:
            return i
        cpt+=1  
        

def rechercheDictio(deckJoueurs:dict, nomJ:str ,index:int)->list:
    """
    Parameters
    ----------
    deckJoueurs : dict
        deck du joueurs
    nomJ : str
        nom du joueurs dans le dico ou on dois faire la recherche
    index : int
        position ou on dois chercher

    Returns
    -------
    list
        liste des cartes

    """
    for indice, cartes in enumerate(deckJoueurs[nomJ]):
        if indice == index:
            return cartes


def selectJoueurs(nomDesJoueurs:list)->int:
    """
    Parameters
    ----------
    nomDesJoueurs : list
        listes des joueurs

    Returns
    -------
    int
        positions du joueurs dans la liste

    """
    cpt = 0
    for i in nomDesJoueurs:
        print(cpt,"-",i)
        cpt += 1
    joueursSelect = demander_saisie()
    return joueursSelect


def addAs(deckJoueurs:dict, nomDesJoueurs:list)->dict:
    """
    Parameters
    ----------
    deckJoueurs : dict
        deck du joueurs a qui on ajoute l'as
    nomDesJoueurs : list
        listes des joueurs

    Returns
    -------
    dict
        deck du joueurs après ajouts

    """
    print("a qui voulez vous mettre l'as\n")
    joueursSelect = selectJoueurs(nomDesJoueurs)
    return addCartes(deckJoueurs,nomDesJoueurs[joueursSelect],2)


def addJoker(deckJoueurs:dict, nomDesJoueurs:list)->dict:
    """
    Parameters
    ----------
    deckJoueurs : dict
        deck du joueurs a qui on ajoute le joker
    nomDesJoueurs : list
        listes du nom des joueurs

    Returns
    -------
    dict
        deck du joueurs après ajouts

    """
    print("a qui voulez vous placer le joker\n")
    joueursSelect = selectJoueurs(nomDesJoueurs)
    return addCartes(deckJoueurs,nomDesJoueurs[joueursSelect],4)


def add2(deckJoueurs:dict, nomDesJoueurs:list)->dict:
    """
    Parameters
    ----------
    deckJoueurs : dict
        deck du joueurs a qui on ajoute le 2
    nomDesJoueurs : list
        listes des joueurs 

    Returns
    -------
    dict
        deck du joueurs après ajouts
    """
    print("a qui voulez vous mettre le 2\n")
    joueursSelect = selectJoueurs(nomDesJoueurs)
    return addCartes(deckJoueurs,nomDesJoueurs[joueursSelect],2)


def retirerCartes(deckJoueurs:dict, cartesSelect:str, nomJ:str)->dict:
    """
    Parameters
    ----------
    deckJoueurs : dict
        listes des cartes des joueurs
    cartesSelect : str
        la carte poser a retirer du deck du joueurs
    nomJ : str
        nom du joueurs a qui nous devons retirer la cartes

    Returns
    -------
    dict
        deck du joueurs après avoir retirer la cartes

    """
    l = []
    finJeux = False
    for indice, cle in deckJoueurs.items():
        if indice == nomJ:
            for i in cle:
                l.append(i)
    del l[l.index(cartesSelect)]
    if len(l) == 0:
        finJeux = True
    deckJoueurs[nomJ] = l
    return deckJoueurs, finJeux


def poser_cartes(deckJoueurs:dict, cartes:list, nomJ:str, deckDuJeux:list, MapCartes:dict, nomDesJoueurs:list)->list or str:
    """
    Parameters
    ----------
    deckJoueurs : dict
        deck du joueurs
    cartes : list
        listes des cartes
    nomJ : str
        nom du joueurs qui pose la cartes
    deckDuJeux : list
        deck du jeux sur la table
    MapCartes : dict
        toutes les cartes en fonction de la couleurs
    nomDesJoueurs : list
        listes des joueurs

    Returns
    -------
    list or str
        sois le deck du jeux sois une chaine car le joueurs n'a pas pu poser la cartes

    """
    for indice, cartes in enumerate(deckJoueurs[nomJ]):
        print("{} {}".format(indice, cartes))
    print("qu'elle cartes voulez vous poser ?\n")
    choixJ = demander_saisie()
    cartesSelect = rechercheDictio(deckJoueurs, nomJ, choixJ)
    valetPresence = False
    if ord(cartesSelect) == 0x1f0ab or ord(cartesSelect) == 0x1f0bb or ord(cartesSelect) == 0x1f0cb or ord(cartesSelect) == 0x1f0db:
        valetPresence = True
    if ord(cartesSelect) == 0x1f0a8 or ord(cartesSelect) == 0x1f0b8 or ord(cartesSelect) == 0x1f0c8 or ord(cartesSelect) == 0x1f0d8:
        deckDuJeux.append(cartesSelect)
        stock = retirerCartes(deckJoueurs, cartesSelect, nomJ)
        deckJoueurs = stock[0]
        finJeux = stock[1]
    etat = False
    for indice, cartes in enumerate(MapCartes.items()): 
        if ord(cartesSelect) in extractionListes(MapCartes,indice) and ord(deckDuJeux[-1]) in extractionListes(MapCartes,indice):
            if ord(cartesSelect) == 0x1f0a8 or ord(cartesSelect) == 0x1f0b8 or ord(cartesSelect) == 0x1f0c8 or ord(cartesSelect) == 0x1f0d8:
                pass
            else:
                deckDuJeux.append(cartesSelect)
                stock = retirerCartes(deckJoueurs, cartesSelect, nomJ)
                deckJoueurs = stock[0]
                finJeux = stock[1]
                print(deckJoueurs, " - ", finJeux)
                etat = True
                if ord(cartesSelect) == 0x1f0a1 or ord(cartesSelect) == 0x1f0b1 or ord(cartesSelect) == 0x1f0c1 or ord(cartesSelect) == 0x1f0d1:
                    deckJoueurs = addAs(deckJoueurs, nomDesJoueurs)
                elif ord(cartesSelect) == 0x1f0a2 or ord(cartesSelect) == 0x1f0b2 or ord(cartesSelect) == 0x1f0c2 or ord(cartesSelect) == 0x1f0d2 or ord(cartesSelect) == 0x1f0cf:
                    deckJoueurs = add2(deckJoueurs, nomDesJoueurs)
                elif ord(cartesSelect) == 0x1f0cf or ord(cartesSelect) == 0x1f0a2 or ord(cartesSelect) == 0x1f0b2 or ord(cartesSelect) == 0x1f0c2 or ord(cartesSelect) == 0x1f0d2:
                    deckJoueurs = addJoker(deckJoueurs,nomDesJoueurs)
                #return poser_cartes(deckJoueurs, cartes, nomJ, deckDuJeux, MapCartes)
    if etat:
        return deckDuJeux, finJeux, valetPresence
    else:
        return "tu ne peux poser cette cartes car ce n'est pas la meme couleur"
    


def jeu(nbreJoueurs:int, cartes:list, MapCartes:dict)->list:
    """
    Parameters
    ----------
    nbreJoueurs : int
        nombre de joueurs qui joue
    cartes : list
        listes des cartes
    MapCartes : dict
        toute les cartes en fonction de leurs couleurs
    nomJT : str, optional
        nom du joueurs qui rejoue si il pause le valet. The default is None.

    Returns
    -------
    list
        listes des cartes sur la table

    """
    nomDesJoueurs = nomJoueurs(nbreJoueurs)
    TableauDuJeux = []
    print("listes des joueurs : ", nomDesJoueurs, "\n")
    print("la partie peut commencer\n")
    deckJoueurs = genererCartes(nomDesJoueurs, cartes)
    print("deck des joueurs : ", deckJoueurs, "\n")
    TableauDuJeux.append(choice(cartes))
    print("cartes sur la table : ", TableauDuJeux, "\n")
    nomJ = tourJoueurs(nomDesJoueurs)
    print("{} joue\n".format(nomJ))
    finJeux = False
    cpt = nomDesJoueurs.index(nomJ)
    while finJeux != True:
        print("que voulez vous faire ? \n 1 - poser cartes \n 2 - tirer cartes\n")
        choixJ = demander_saisie()
        if choixJ == 1:
            stock = poser_cartes(deckJoueurs, cartes, nomJ, TableauDuJeux, MapCartes, nomDesJoueurs)
            deckduJeux = stock[0]
            finJeux = stock[1]
            valetPresence = stock[2]
            print("Valet Presence - ", valetPresence)
        else:
            deckduJeux = addCartes(deckJoueurs,nomJ,1)
        print(deckduJeux)
        """
        ici probleme avec valet
        """
        if valetPresence:
            cpt = nomDesJoueurs.index(nomJ)
            nomJ = SpeValet(nomDesJoueurs,cpt) #-
            valetPresence = False
        elif cpt >= len(nomDesJoueurs):
            nomJ = nomDesJoueurs[0]
            print(nomDesJoueurs)
        else:
            nomJ = nomDesJoueurs[cpt - 1]
        if cpt >= len(nomDesJoueurs):
            cpt = 0
        else:
            cpt += 1
        print("{} joue\n".format(nomJ))


if __name__ == '__main__':
    print("Bienvenue sur le jeux du 8 americains\n")
    cartes = [chr(x) for x in range(0x1f0a1, 0x1f0DE) if x != 0x1f0af and x != 0x1f0b0 and x != 0x1f0c0 and x != 0x1f0d0]
    MapCartes = {
        "hearth" : [i for i in range(127153,127166)],
        "carreau" : [i for i in range(127169,127182)],
        "trefle" : [i for i in range(127185,127198)],
        "pique" : [i for i in range(127137,127150)]
        }
    print("nombre de joueurs dans la parties\n")
    nbreJoueurs = 4
    while nbreJoueurs > 3 and nbreJoueurs != 1:
        print("3 joueurs max")
        nbreJoueurs = demander_saisie()
    
    jeu(nbreJoueurs, cartes, MapCartes)
    
    
