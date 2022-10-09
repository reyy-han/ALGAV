from echauffement import *
from arbre_decision_2 import *
from Robdd import *

import sys
if len(sys.argv) < 2:
    raise Exception("Il manque un argument à 0 ou 1. Ajoutez l'argument 1 en ligne de commande si vous voulez afficher les graphes.\n")
else:
    if int(sys.argv[1]) == 1:
        affiche = True
    else:
        affiche = False

print("===============================================================================================================")
print("Q3.10")

print(">>> compression_bdd(luka(cons_arbre(table(8, 4))), True)\n",
      compression_bdd(luka(cons_arbre(table(8, 4)))))
assert luka(cons_arbre(table(38, 8))) == \
       ['x3(x2(x1(False)(True))(x1(True)(False)))(x2(x1(False)(True))(x1(False)(False)))',
        ['x2(x1(False)(True))(x1(True)(False))', ['x1(False)(True)', False, True],
         ['x1(True)(False)', True, False]], ['x2(x1(False)(True))(x1(False)(False))',
                                             ['x1(False)(True)', False, True],
                                             ['x1(False)(False)', False, False]]]

assert compression_bdd(luka(cons_arbre(table(38, 8)))) == \
       ['x3(x2(x1(False)(True))(x1(True)(False)))(x2(x1(False)(True))(x1(False)(False)))',
        ['x2(x1(False)(True))(x1(True)(False))', ['x1(False)(True)', False, True], ['x1(True)(False)', True, False]],
        ['x2(x1(False)(True))(x1(False)(False))', ['x1(False)(True)', False, True], False]]

print("\n>>> dot(compression_bdd(luka(cons_arbre(table(38, 8))), True)\n",
      dot(compression_bdd(luka(cons_arbre(table(38, 8)))), True))
if affiche:
    print(">>> dot(compression_bdd(luka(cons_arbre(table(38, 8)))), True).render('cons_arbre(table(38, 8))_ompresse_bdd.dot', view=True)\n",
      dot(compression_bdd(luka(cons_arbre(table(38, 8)))), True).render('cons_arbre(table(38, 8))_compresse_bdd.dot', view=True))

print("\n>>> compression_bdd(luka(cons_arbre(table(-5, 8))))\n", compression_bdd(luka(cons_arbre(table(-5, 8)))))
assert compression_bdd(luka(cons_arbre(table(0, 4)))) is False
assert compression_bdd(luka(cons_arbre(table(-5, 8)))) is None
print("\n>>> dot(compression_bdd(luka(cons_arbre(table(0, 4))), True)\n",
      dot(compression_bdd(luka(cons_arbre(table(0, 4)))), True))
# Affichage d'une feuille unique False attendue
if affiche:
    print(">>> dot(compression_bdd(luka(cons_arbre(table(0, 4)))), True).render('cons_arbre(table(0, 4))_compresse_bdd.dot', view=True)\n",
      dot(compression_bdd(luka(cons_arbre(table(0, 4)))), True).render('cons_arbre(table(0, 4))_compresse_bdd.dot', view=True))

print("\n>>> dot(compression_bdd(luka(cons_arbre(table(-5, 8))), True)\n",
      dot(compression_bdd(luka(cons_arbre(table(-5, 8)))), True))
# Affichage vide attendu
if affiche:
    print(">>> dot(compression_bdd(luka(cons_arbre(table(-5, 8)))), True).render('cons_arbre(table(-5, 8))_compresse_bdd.dot', view=True)\n",
      dot(compression_bdd(luka(cons_arbre(table(-5, 8)))), True).render('cons_arbre(table(-5, 8))_compresse_bdd.dot', view=True))


print("---------------------------------------------------------------------------------------------------------------")

print(">>> table(14, 5)\n", table(14, 5))
print("\n>>> luka(cons_arbre(table(14, 5))\n",
      luka(cons_arbre(table(14, 5))))
print("\n>>> compression_bdd_1(luka(cons_arbre(table(14, 4))\n",
      compression_bdd(luka(cons_arbre(table(14, 5)))))
print("\n>>> dot(compression_bdd(luka(cons_arbre(table(14, 4))), True)\n",
      dot(compression_bdd(luka(cons_arbre(table(14, 5)))), True))
if affiche:
    print(">>> dot(cons_arbre(table(14, 5)), True).render('cons_arbre(table(14, 5)).dot', view=True)\n",
      dot(cons_arbre(table(14, 5)), False).render('cons_arbre(table(14, 5)).dot', view=True))
    print(">>> dot(compression_bdd(luka(cons_arbre(table(14, 5)))), True).render('cons_arbre(table(14, 5))_compresse_bdd.dot', view=True)\n",
      dot(compression_bdd(luka(cons_arbre(table(14, 5)))), True).render('cons_arbre(table(14, 5))_compresse_bdd.dot', view=True))

# print(">>> dot(compression_bdd(luka(cons_arbre(table(14, 4))), True)\n",
#      dot(compression_bdd(luka(cons_arbre(table(14,4)))), True))

print(">>> table(64895235, 32)\n", table(64895235, 32))
print("\n>>> dot(compression_bdd(luka(cons_arbre(table(64895235, 32))), True)\n",
      dot(compression_bdd(luka(cons_arbre(table(64895235, 32)))), True))
if affiche:
    print(">>> dot(cons_arbre(table(64895235, 32)), True).render('cons_arbre(table(64895235, 32)).dot', view=True)\n",
      dot(cons_arbre(table(64895235, 32)), False).render('cons_arbre(table(64895235, 32)).dot', view=True))
    print(">>> dot(compression_bdd(luka(cons_arbre(table(64895235, 32)))), True).render('cons_arbre(table(64895235, 32))_compresse_bdd.dot', view=True)\n",
      dot(compression_bdd(luka(cons_arbre(table(64895235, 32)))), True).render('cons_arbre(table(64895235, 32))_compresse_bdd.dot', view=True))
    print(">>> dot(compression_bdd(luka(cons_arbre(table(89, 8)))), True).render('cons_arbre(table(89, 8))_compresse_bdd.dot', view=True)\n",
      dot(compression_bdd(luka(cons_arbre(table(89, 8)))), True).render('cons_arbre(table(89, 8))_compresse_bdd.dot', view=True))
