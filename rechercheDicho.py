#!/usr/bin/python3


def demanderNombre()->int:
    """
    Returns
    -------
    int
        nombre choisis par l'user.

    """
    nbreUser = input("entrez nombre: \n")
    try:
        nbreUser = int(nbreUser)
        return nbreUser
    except:
        print("merci de rentrez un nombre!")
        return demanderNombre()


def creerTableau(longueur:int)->list:
    """
    Parameters
    ----------
    longueur : int
        longueur du tableau.

    Returns
    -------
    list
        le tableaua avec les nombres dedans.

    """
    print("creer un tableau: \n")
    tabUser = []
    for i in range(longueur):
        tabUser.append(demanderNombre())
    return tabUser


def reverse(listR:list)->list:
    """
    Parameters
    ----------
    listR : list
        listes à reverse.

    Returns
    -------
    list
        liste reverse.

    """
    return [i for i in listR[::-1]]
        


def tri(listeAtrier:list)->list:
    """
    Parameters
    ----------
    listeAtrier : list
        liste à trier.

    Returns
    -------
    list
        liste trier.

    """
    stock = 0
    for i in range(len(listeAtrier)):
        for j in range(len(listeAtrier)):
            if listeAtrier[i] > listeAtrier[j]:
                stock = listeAtrier[j]
                listeAtrier[j] = listeAtrier[i] 
                listeAtrier[i] = stock
    return reverse(listeAtrier)


def rechercheDichotomique(listeTrier:list, numberRecherche:int)->list:
    """
    Parameters
    ----------
    listeTrier : list
        la liste trier.
    numberRecherche : int
        le nombre à recherché dans la liste.

    Returns
    -------
    list
        nombre et position du nombre sinon ? pour dire qu'il n'est pas dans la liste.

    """
    a = 0
    b = len(listeTrier) - 1
    m = (a+b)//2
    while a <= b:
        if listeTrier[m] == numberRecherche:
            position = m
            return [numberRecherche,position]
        elif listeTrier[m] < numberRecherche:
            a = m + 1
        else:
            b = m - 1
        m = (a+b)//2
    return ['?','?']
                
                
        

if __name__ == '__main__':
    print("entrez longeur du tableau voulu: \n")
    longeur = demanderNombre()
    tabUser = creerTableau(longeur)
    print("entrez nombre a rechercher: \n")
    nbreUser = demanderNombre()
    print("tableau trier = {}".format(tri(tabUser)))
    rechercheDicho = rechercheDichotomique(tri(tabUser), nbreUser)
    print("[nombre = {}, position = {}]".format(rechercheDicho[0], rechercheDicho[1]))
    
