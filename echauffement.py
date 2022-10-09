# 1.1 Echauffement

# question 1.1
# Le langage python permet de manipuler directement des entiers de taille arbitraire.

# question 1.2
def decomposition(x):
    """
    int -> list[bool]
    :param x: entier naturel de taille arbitraie
    :return: une liste de bits représentant la décomposition en base 2 de l'entier x. (Telle que les
    bits de poids faibles soient orésentés en tête de liste.
    """
    if x >= 0:
        c = 0
        total = 0
        reste = x
        l = []
        while total < x:
            i = 0
            while pow(2, i) <= reste:
                i = i + 1
            l.append(i-1)
            total = total + pow(2, i-1)
            reste = reste - pow(2, i-1)
        res = []
        if l:
            for i in range(max(l)+1):
                if i in l:
                    res.append(True)
                else:
                    res.append(False)
        return res
    else:
        #print("L'argument donné x doit être un entier naturel")
        raise Exception("Argument donné x doit être un entier naturel")


# question 1.3
def completion(l, n):
    """
    list[bool] * int -> list[bool]
    :param l: liste de bits
    :param n: entier naturel
    :return: soit la liste tronquée ne contenant que les n premiers éléments, soit la liste complétée
    à droite par des valeurs False, de taille n.
    """
    if len(l) > n:
        return l[:n]
    else:
        r = n - len(l)
        while r > 0:
            l.append(False)
            r = r - 1
        return l


# question 1.4
def table(x, n):
    """
    int * int -> list[bool]
    :param x: entier naturel de taille arbitraire
    :param n: entier naturel
    :return: la table de vérité, liste de bits de taille n correspondant à la décomposition de x en
     base 2.
    """
    try:
        l = decomposition(x)
        return completion(l, n)
    except Exception:
        print("Erreur: Argument donné x doit être un entier naturel")



