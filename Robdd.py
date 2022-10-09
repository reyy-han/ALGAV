def compression_bdd(luka):
    """
    On considère que luka est soit True soit False soit une liste. Si il s'agit d'une liste alors
    elle est soit vide soit elle est de taille 3 (pour la tete et les fils).
    De plus il est préférable de donnée un table qui correspond bien au chiffre de depart (tel que la taille
    soit en 2^n), par exemple 14 est codé sur 4 bits (8 sur 3bits mais il faut une table de 2^n donc une table
    de 4 aussi, 38 -> 8 etc)
    :param luka: arbre de décision enrichi par les mots de lukasievicz
    :return: l'arbre compressé avec les noeuds sous forme de lukasiewicz
    """
    if type(luka) is not list or luka == []:
        return luka
    elif luka[1] == []:
        return compression_bdd(luka[2])
    elif luka[2] == []:
        return compression_bdd(luka[1])
    if type(luka[1]) is not list and type(luka[2]) is not list:
        if luka[1] == luka[2]:
            return luka[1]
        else:
            return luka
    elif type(luka[1]) is not list:
        if luka[2] == []:
            return luka[1]
        else:
            luka[2] = compression_bdd(luka[2])
            if luka[1] == luka[2]:
                return luka[1]
            else:
                return luka
    elif type(luka[2]) is not list:
        if luka[1] == []:
            return luka[2]
        else:
            luka[1] = compression_bdd(luka[1])
            if luka[1] == luka[2]:
                return luka[1]
            else:
                return luka
    elif luka[1][0] == luka[2][0]:
        return compression_bdd(luka[1])
    else:
        luka[1] = compression_bdd(luka[1])
        luka[2] = compression_bdd(luka[2])
        if luka[1] == luka[2]:
            return compression_bdd(luka[1])
        return luka


def flatten(l):
    """
    list[a] -> list[a]
    :param l: liste à aplatir
    :return: la liste aplati
    """
    f = []
    if type(l) is not list:
        return l
    for e in l:
        if type(e) is list:
            f = f + flatten(e)
        else:
            f.append(e)
    return f


def count_nodes_robdd(robdd):
    """
    Compte le nombre de noeuds contenus dans le ROBDD donné en paramètre.
    :param robdd: arbre de décision compressé
    :return: le nombre de noeuds contenus dans robdd
    """
    f = flatten(robdd)
    nbnodes = len(set(f))
    return nbnodes
