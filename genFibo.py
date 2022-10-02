#!/usr/bin/python3
def genFibo(nbreUser:int) -> list:
    """
    Parameters
    ----------
    nbreUser : int
        nombre de la suite de fibo que l'utilisateur veut générer.

    Returns
    -------
    list
        la suite de nombre de fibo.

    """
    suiteFibo = [0,1]
    result = 1
    sto = 1
    cpt = 1
    while nbreUser != 0:
        sto = result
        result = sto + suiteFibo[cpt - 1]
        suiteFibo.append(result)
        nbreUser -= 1
        cpt+=1
    return suiteFibo


def demanderNombre()->int:
    """
    Returns
    -------
    int
        le nombre choisis par l'utilisateur.

    """
    nbreUser = input("merci de rentre un nombre: \n")
    try:
        nbreUser = int(nbreUser)
        return nbreUser
    except:
        return demanderNombre()

if __name__ == '__main__':
    nbreUser = demanderNombre()
    print("gen fibo: {}".format(genFibo(nbreUser)))
