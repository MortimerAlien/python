#!/usr/bin/python3
def genFibo(nbreUser:int) -> int:
    #complexité temporelle de theta(n), pire des cas 0(n) (linéaire)
    
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
    
    f0 = 0
    f1 = 1
    stock = 0
    for i in range(nbreUser):
        f0 = f1
        f1 = stock
        stock = f0 + f1
        print(stock)


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
    genFibo(nbreUser)
