from arbre_decision_2 import *
from echauffement import *

import sys

if len(sys.argv) < 2:
    raise Exception("Il manque un argument à 0 ou 1. Ajoutez l'argument 1 en ligne de commande si vous voulez afficher les graphes.\n")
else:
    if int(sys.argv[1]) == 1:
        affiche = True
    else:
        affiche = False

print("===============================================================================================================")
print("Q2.6")
afg = Arb("X")
afd = Arb(True)
a1 = Arb(6, afg, afd)
print(a1.print_arb())
assert afg.print_arb() == a1.fils_gauche.print_arb()
assert afg.print_arb() == "X"
assert afd.print_arb() == a1.fils_droit.print_arb()
assert afd.print_arb() == "True"
assert a1.print_arb() == "[6, 'X', True]"

assert cons_arbre([]) == []
assert cons_arbre(table(38, 8)) == ['x3', ['x2', ['x1', False, True], ['x1', True, False]], ['x2', ['x1', False, True], ['x1', False, False]]]
assert cons_arbre(table(1, 1)) == True
assert cons_arbre(table(3, 2)) == ['x1', True, True]
assert cons_arbre(table(8, 4)) == ['x2', ['x1', False, False], ['x1', False, True]]
assert decomposition(4589) == [True, False, True, True, False, True, True, True, True, False, False, False, True]
assert decomposition(4589) == table(4589, 13)
assert cons_arbre(table(4589, 16)) == ['x4',
                                       ['x3', ['x2', ['x1', True, False], ['x1', True, True]],
                                              ['x2', ['x1', False, True], ['x1', True, True]]],
                                       ['x3', ['x2', ['x1', True, False], ['x1', False, False]],
                                        ['x2', ['x1', True, False], ['x1', False, False]]]]
print("\tTest cons_arbre(T) :        OK\n")


print("===============================================================================================================")
print("Q2.7")
assert luka_table(table(38, 8)) == ['x3(x2(x1(False)(True))(x1(True)(False)))(x2(x1(False)(True))(x1(False)(False)))',
                                    ['x2(x1(False)(True))(x1(True)(False))', ['x1(False)(True)', False, True],
                                     ['x1(True)(False)', True, False]], ['x2(x1(False)(True))(x1(False)(False))',
                                                                         ['x1(False)(True)', False, True],
                                                                         ['x1(False)(False)', False, False]]]
assert racine_luka(cons_arbre(table(8, 4))) == "x2(x1(False)(False))(x1(False)(True))"
assert racine_luka(
    cons_arbre(table(38, 8))) == "x3(x2(x1(False)(True))(x1(True)(False)))(x2(x1(False)(True))(x1(False)(False)))"

assert racine_luka(cons_arbre([])) == "()"
assert racine_luka(
    cons_arbre(table(38, 8))) == "x3(x2(x1(False)(True))(x1(True)(False)))(x2(x1(False)(True))(x1(False)(False)))"
assert luka(cons_arbre(table(38, 8))) == luka_table(table(38, 8))
assert luka(cons_arbre(table(8, 4))) == ['x2(x1(False)(False))(x1(False)(True))',
                                         ['x1(False)(False)', False, False], ['x1(False)(True)', False, True]]
assert luka(cons_arbre(table(1, 1))) is True
assert luka(cons_arbre(table(0, 1))) is False
print("\tTest racine_luka(Abr) :     OK")
print("\tTest luka_table(T) :        OK")
print("\tTest luka(Abr) :            OK\n")

# print("lr cons arb : ", list_racine(cons_arbre(table(8, 4))))
assert list_racine(luka(cons_arbre(table(-5, 2)))) == []
assert racine_count(list_racine(luka(cons_arbre(table(-5, 2))))) == {}
assert list_racine(luka(cons_arbre(table(0, 2)))) == ['x1(False)(False)', False, False]
assert racine_count(luka(cons_arbre(table(0, 2)))) == {'x1(False)(False)': 1, False: 2}
assert list_racine(luka(cons_arbre(table(8, 4)))) == \
       ['x2(x1(False)(False))(x1(False)(True))', 'x1(False)(False)', False, False, 'x1(False)(True)', False, True]
assert racine_count(list_racine(luka(cons_arbre(table(8, 4))))) == \
       {'x2(x1(False)(False))(x1(False)(True))': 1, 'x1(False)(False)': 1, False: 3, 'x1(False)(True)': 1, True: 1}
print("\tTest list_racine(luka) :    OK")
print("\tTest racine_count(lr) :     OK\n")


print("===============================================================================================================")
print("Q2.8")
assert luka(cons_arbre(table(-4, 4))) is None
assert luka(cons_arbre(table(0, 4))) == \
       ['x2(x1(False)(False))(x1(False)(False))',
        ['x1(False)(False)', False, False], ['x1(False)(False)', False, False]]
assert compression(luka(cons_arbre(table(1, 1))), {}) is True
assert compression(luka(cons_arbre(table(-4, 4))), {}) is None
assert compression(luka(cons_arbre(table(0, 4))), {}) == ['x21', ['x11', False, False], ['x11', False, False]]
assert compression(luka(cons_arbre(table(8, 4))), {}) == \
       ['x21', ['x11', False, False], ['x12', False, True]]
assert compression(luka(cons_arbre(table(38, 8))), {}) == \
       ['x31', ['x21', ['x11', False, True], ['x12', True, False]], ['x22', ['x11', False, True], ['x13', False, False]]]
print("\tTest compression(luka) :    OK\n")


print("===============================================================================================================")
print("Q2.9")
# Attention il y aura des affichages de dots

print("\n>>> luka(cons_arbre(table(38, 8)))\n", luka(cons_arbre(table(38, 8))))

print("list_racine :", list_racine(luka(cons_arbre(table(38, 8)))))

f = list_racine(luka(cons_arbre(table(38, 8))))
print("dico racine avec count: ", racine_count(f))
print("\n>>> cons_arbre(table(3, 2))\n", cons_arbre(table(3, 2)))
print("\n>>> luka(cons_arbre(table(3, 2)))\n", luka(cons_arbre(table(3, 2))))
print("racine_count(luka(cons_arbre(table(3, 2)))): ", racine_count(list_racine(luka(cons_arbre(table(3, 2))))))

print("\n>>> dot(cons_arbre(table(3, 2)), False)\n", dot(cons_arbre(table(3, 2)), False))
if affiche:
    print("\n>>> dot(cons_arbre(table(3, 2)), False).render('cons_arbre(table(3, 2)).dot', view=True)\n",
      dot(cons_arbre(table(3, 2)), False).render('cons_arbre(table(3, 2)).dot', view=True))
if affiche:
    print("\n>>> dot(cons_arbre(table(3, 2)), True).render('cons_arbre(table(3, 2))_compresse.dot', view=True)\n",
      dot(cons_arbre(table(3, 2)), True).render('cons_arbre(table(3, 2))_compresse.dot', view=True))

print("\n>>> dot(cons_arbre(table(38, 8)), False)\n", dot(cons_arbre(table(38, 8)), False))
if affiche:
    print("\n>>> dot(cons_arbre(table(38, 8)), False).render('test_figure1.dot', view=True)\n",
      dot(cons_arbre(table(38, 8)), False).render('test_figure1.dot', view=True))

print("\n>>> dot(compression(luka(cons_arbre(table(38, 8))), {}), True)\n",
      dot(compression(luka(cons_arbre(table(38, 8))), {}), True))
if affiche:
    print("\n>>> dot(compression(luka(cons_arbre(table(38, 8))), {}), True).render('test_figure1_compresse.dot', view=True)\n",
      dot(compression(luka(cons_arbre(table(38, 8))), {}), True).render('test_figure1_compresse.dot', view=True))
    print("\n>>> dot(luka(cons_arbre(table(38, 8))), True).render('test_figure1_compresse_sans_fct_comp.dot', view=True)\n",
      dot(luka(cons_arbre(table(38, 8))), True).render('test_figure1_compresse_sans_fct_comp.dot', view=True))

print("\n>>> dot(cons_arbre(table(89, 8)), False)\n", dot(cons_arbre(table(89, 8)), False))
if affiche:
    print("\n>>> dot(cons_arbre(table(89, 8)), False).render('cons_arbre(table(89, 8)).dot', view=True)\n",
      dot(cons_arbre(table(89, 8)), False).render('cons_arbre(table(89, 8))', view=True))

print("\n>>> dot(compression(luka(cons_arbre(table(89, 8))), {}), True)\n", dot(compression(luka(cons_arbre(table(89, 8))), {}), True))
if affiche:
    print("\n>>> dot(compression(luka(cons_arbre(table(89, 8))), {}), True).render('cons_arbre(table(89, 8))_compresse.dot', view=True)\n",
      dot(compression(luka(cons_arbre(table(89, 8))), {}), True).render('cons_arbre(table(89, 8))_compresse.dot', view=True))
    print("\n>>> dot(luka(cons_arbre(table(89, 8))), True).render('cons_arbre(table(89, 8))_compresse_sans_comp.dot', view=True)\n",
        dot(luka(cons_arbre(table(89, 8))), True).render('cons_arbre(table(89, 8))_compresse_sans_comp.dot', view=True))



