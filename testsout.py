from echauffement import *
from arbre_decision_2 import *
from Robdd import *

import sys

if len(sys.argv) < 2:
    raise Exception(
        "Il manque un argument à 0 ou 1. Ajoutez l'argument 1 en ligne de commande si vous voulez afficher les graphes.\n")
else:
    if int(sys.argv[1]) == 1:
        affiche = True
    else:
        affiche = False

print(">>>decomposition(1422119206754208377)\n", len(decomposition(1422119206754208377)))
print("\n>>> table(1422119206754208377, 64)\n", table(1422119206754208377, 64))
print("\n>>> cons_arbre(table(1422119206754208377, 64))\n",
      cons_arbre(table(1422119206754208377, 64)))
print("\n>>> dot(cons_arbre(table(1422119206754208377, 64)), False)\n",
      dot(cons_arbre(table(1422119206754208377, 64)), False))

print("\n>>> compression(luka(cons_arbre(table(1422119206754208377, 64))), {})\n",
      compression(luka(cons_arbre(table(1422119206754208377, 64))), {}))
print("\n>>> dot(cons_arbre(table(1422119206754208377, 64)), False)\n",
      dot(luka(cons_arbre(table(1422119206754208377, 64))), True))

print("\n>>> compression_bdd(luka(cons_arbre(table(1422119206754208377, 64)))\n",
      compression_bdd(luka(cons_arbre(table(1422119206754208377, 64)))))
print("\n>>> dot(compression_bdd(luka(cons_arbre(table(1422119206754208377, 64))), True)\n",
      dot(compression_bdd(luka(cons_arbre(table(1422119206754208377, 64)))), True))

if affiche:
    print(
        "\n>>> dot(cons_arbre(table(1422119206754208377, 64)), False).render('cons_arbre(table(1422119206754208377, 64)).dot', view=True)\n",
        dot(cons_arbre(table(1422119206754208377, 64)), False).render('cons_arbre(table(1422119206754208377, 64)).dot',
                                                                      view=True))
    print(
        ">>> dot(luka(cons_arbre(table(1422119206754208377, 64))), True).render('cons_arbre(table(1422119206754208377, 64))_compresse_sans_comp.dot', view=True)\n",
        dot(luka(cons_arbre(table(1422119206754208377, 64))), True).render(
            'cons_arbre(table(1422119206754208377, 64))_compresse_sans_comp.dot', view=True))
    print(
        ">>> dot(compression_bdd(luka(cons_arbre(table(1422119206754208377 64)))), True).render('cons_arbre(table(1422119206754208377, 64))_compresse_bdd.dot', view=True)\n",
        dot(compression_bdd(luka(cons_arbre(table(1422119206754208377, 64)))), True).render(
            'cons_arbre(table(1422119206754208377, 64))_compresse_bdd.dot', view=True))

print(
    "----------------------------------------------------------------------------------------------------------------------------------")

print("\ndecomposition(101247173429701308769807673754056716620117458044746632656397076520187575777199)\n",
      len(decomposition(101247173429701308769807673754056716620117458044746632656397076520187575777199)))
print("\n>>> table(101247173429701308769807673754056716620117458044746632656397076520187575777199, 256)\n",
      table(101247173429701308769807673754056716620117458044746632656397076520187575777199, 256))

print("\n>>> cons_arbre(table(101247173429701308769807673754056716620117458044746632656397076520187575777199, 256))\n",
      cons_arbre(table(101247173429701308769807673754056716620117458044746632656397076520187575777199, 256)))
print(
    "\n>>> dot(luka(cons_arbre(table(101247173429701308769807673754056716620117458044746632656397076520187575777199, 256))), False)\n",
    dot(luka(cons_arbre(table(101247173429701308769807673754056716620117458044746632656397076520187575777199, 256))),
        False))

print(
    "\n>>> compression(luka(cons_arbre(table(101247173429701308769807673754056716620117458044746632656397076520187575777199, 256))), {})\n",
    compression(
        luka(cons_arbre(table(101247173429701308769807673754056716620117458044746632656397076520187575777199, 256))),
        {}))
print(
    "\n>>> dot(luka(cons_arbre(table(101247173429701308769807673754056716620117458044746632656397076520187575777199, 256))), True)\n",
    dot(luka(cons_arbre(table(101247173429701308769807673754056716620117458044746632656397076520187575777199, 256))),
        True))

print(
    "\n>>> compression_bdd(luka(cons_arbre(table(101247173429701308769807673754056716620117458044746632656397076520187575777199, 256)))\n",
    compression_bdd(
        luka(cons_arbre(table(101247173429701308769807673754056716620117458044746632656397076520187575777199, 256)))))
print(
    "\n>>> dot(compression_bdd(luka(cons_arbre(table(101247173429701308769807673754056716620117458044746632656397076520187575777199, 256))), True)\n",
    dot(compression_bdd(luka(cons_arbre(table(1422119206754208377, 256)))), True))

if affiche:
    print(
        ">>> dot(cons_arbre(table(101247173429701308769807673754056716620117458044746632656397076520187575777199, 256)), True).render('test2.dot', view=True)\n",
        dot(cons_arbre(table(101247173429701308769807673754056716620117458044746632656397076520187575777199, 256)),
            False).render('test2.dot', view=True))
    print(
        ">>> dot(compression_bdd(luka(cons_arbre(table(101247173429701308769807673754056716620117458044746632656397076520187575777199, 256)))), True).render('test2_compresse_bdd.dot', view=True)\n",
        dot(compression_bdd(luka(
            cons_arbre(table(101247173429701308769807673754056716620117458044746632656397076520187575777199, 256)))),
            True).render('test2_compresse_bdd.dot', view=True))
    print(
        ">>> dot(luka(cons_arbre(table(101247173429701308769807673754056716620117458044746632656397076520187575777199, 256))), True).render('test2_compresse_sans_comp.dot', view=True)\n",
        dot(luka(
            cons_arbre(table(101247173429701308769807673754056716620117458044746632656397076520187575777199, 256))),
            True).render('test2_compresse_sans_comp.dot', view=True))

n = pow(2, 100) + 1
if affiche:
    print("\n>>> dot(compression_bdd(luka(cons_arbre(table(", n, ", 1024))), True)\n",
          dot(compression_bdd(luka(cons_arbre(table(n, 1024)))), True))

print(
    "----------------------------------------------------------------------------------------------------------------------------------")
f1 = flatten(compression_bdd(luka(cons_arbre(table(1422119206754208377, 64)))))
nbnodes1 = len(set(f1))
print("\nnombre de noeuds ROBDD de table( 1422119206754208377 , 64): ", nbnodes1)

f2 = flatten(compression_bdd(
    luka(cons_arbre(table(101247173429701308769807673754056716620117458044746632656397076520187575777199, 256)))))
nbnodes2 = len(set(f2))
print(
    "\nnombre de noeuds ROBDD de table( 101247173429701308769807673754056716620117458044746632656397076520187575777199 , 256): ",
    nbnodes2)

print(
    "\nnombre de noeuds ROBDD de table(", n, ", 1024): ",
    count_nodes_robdd(compression_bdd(luka(cons_arbre(table(n, 1024))))))
print(
    "\n----------------------------------------------------------------------------------------------------------------------------------")
