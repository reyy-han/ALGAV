from echauffement import *
from arbre_decision_2 import *
from Robdd import *
import time
import random


def exp_var(var):
    """
    int -> dict[int:int]
    Effectue une expérimentation exhaustive sur les arbres ROBDD à var variables.
    :param var: le nombre de variables des ROBDD traités
    :return: un dictionnaire qui a pour clés les nombres de noeuds possibles et en valeur le nombre de ROBDD
    pour chaque nombre de noeuds.
    """
    taille_table = pow(2, var)
    n = pow(2, taille_table)
    d = dict()
    for i in range(n):  # de 0 à (n-1) (ainsi n fonctions Booléennes (2 variables -> 16 exps))
        f = flatten(compression_bdd(luka(cons_arbre(table(i, taille_table)))))
        if type(f) is list:
            nbnodes = len(set(f))
        else:
            nbnodes = 1
        if nbnodes in d:
            d[nbnodes] = d[nbnodes] + 1
        else:
            d[nbnodes] = 1
    return d


def whilen(var, max):
    """
    int * int -> dict[int:int]
    Effectue une expérimentation partielle sur les ROBDD à var variables. Il tire aléatoirement max nombres entre 0 et
    (2^(2^var))-1 et calcule son ROBDD ainsi que son nombre de noeuds.
    :param var: le nombre de variables des ROBDD traités
    :return: un dictionnaire qui a pour clés les nombres de noeuds possibles et en valeur le nombre de ROBDD
    pour chaque nombre de noeuds
    """
    taille_table = pow(2, var)
    n = pow(2, taille_table)
    d = dict()

    print("n:", n)
    i = 0
    while i < max:
        i = i + 1
        nb = random.randint(0, n)
        f = flatten(compression_bdd(luka(cons_arbre(table(nb, taille_table)))))
        if type(f) is list:
            nbnodes = len(set(f))
        else:
            nbnodes = 1
        if nbnodes in d:
            d[nbnodes] = d[nbnodes] + 1
        else:
            d[nbnodes] = 1
    return d


def temps(f, arg):
    """

    :param f: la fonction à chronometrer
    :param arg: argument à donner à f
    :return: le temps en secondes de l'execution
    """
    start = time.time()
    f(arg)
    end = time.time()
    return end - start


def moy(total, f, arg):
    """
    Calcule le temps moyen d'execution de f(arg) pour total itération
    :param total: le nombre de fois qu'on execute f(arg) en tout
    :param f: fonction à executer
    :param arg: arguments à donner à f
    :return: le temps moyen d'execution de f(arg)
    """
    somme = 0
    for i in range(total):
        somme = somme + temps(f, arg)
    return somme / total


print("===============================================================================================================")
print("Q4.15")
for i in range(1, 5):
    print("Repartitions des ROBDD à ", i, " variables:")
    # print(">>> exp_var(", i, ")\n", exp_var(i))
    #print("temps moyen de exp_var(", i, "): ", moy(100, exp_var, i))
    print("temps de exp_var(", i, "): ", temps(exp_var, i))
    print("\n")


# w = whilen(5, 500003)
# w = whilen(6, 400003)
# w = whilen(7, 486892)
# w = whilen(8, 56343)
# w = whilen(9, 94999)
# w = whilen(10, 17975)
t1 = time.time()
w = whilen(5, 500003)
t2 = time.time()
print(">>> whilen(5, 500003)\n", w, "len = ", len(w))
print("temps de whilen(5, 500003): ", (t2-t1))

# print(">>> exp_var(5)\n", exp_var(5))
# print("temps de exp_var(5): ", temps(exp_var, 5))

