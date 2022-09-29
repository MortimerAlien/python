def lireFichier(fichierAlire:str) -> str:
    """
    Parameters
    ----------
    fichierAlire : str
        le fichier dont on veut afficher le contenu

    Returns
    -------
    str
       le contenu du fichier ou bien un message indiquant je ne peux lire le fichier

    """
    fichier = open(fichierAlire)
    fichier.__enter__()
    try:
        return fichier.read()
    except:
        return "je ne peux lire le fichier"
    finally:
        fichier.__exit__()
print(lireFichier('j.txt'))
