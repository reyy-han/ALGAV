from graphviz import Graph

# 2 Arbre de décision et compression
# question 2.5
class Arb:
    def __init__(self, racine, fils_gauche=None, fils_droit=None):
        # si le fils droit et le fils gauche sont à None, cela veut dire que l'Arb créé est une feuille
        self.racine = racine
        self.fils_gauche = fils_gauche
        self.fils_droit = fils_droit

    def get_racine(self):
        return self.racine

    def noeud(self):
        if self.fils_droit != None and self.fils_gauche != None:
            return [self.racine, self.fils_gauche.noeud(), self.fils_droit.noeud()]
        if self.fils_droit != None:
            return [self.racine, [], self.fils_droit.noeud()]
        if self.fils_gauche != None:
            return [self.racine, self.fils_gauche.noeud(), []]
        else:  # feuille
            return self.racine

    def print_arb(self):
            return str(self.noeud())


# Question 2.6
def cons_arbre(T):
    """
    :param T: table de vérité
    :return: construit l'arbre de décision associé à la table de vérité T.
    """
    L = []
    table = T
    cpt = 1
    if not T:
        return T
    while len(table) > 1:
        L = []
        for i in range(0, len(table), 2):
            racine = "x" + str(cpt)
            # j = j + 1
            if i + 1 < len(table):
                ad = Arb(racine, Arb(table[i]), Arb(table[i + 1]))
            else:
                ad = Arb(racine, Arb(table[i]))
            L.append(ad.noeud())
        cpt = cpt + 1
        table = L
    return table[0]


# Question 2.7
def luka_table(T):
    """
    :param T: table de vérité
    :return: associe le mot de lukasievicz enrichi associé au sous-arbre enraciné à ce noeud.
    """
    L = []
    rac = T
    R = []
    table = T
    cpt = 1
    while len(table) > 1:
        L = []
        R = []
        for i in range(0, len(table), 2):
            racine = "x" + str(cpt) + "(" + str(rac[i]) + ")(" + str(rac[i + 1]) + ")"
            R.append(racine)
            ad = Arb(racine, Arb(table[i]), Arb(table[i + 1]))
            L.append(ad.noeud())
        cpt = cpt + 1
        rac = R
        table = L
    return table[0]


def racine_luka(A):
    """
    fonction récurrente permettant d'associé un mot de lukasievicz à chaque noeud du sous arbre de
    décision fournie A
    :param A: arbre de décision
    :return: le mot de lukasievicz de la tête de l'arbre A
    """
    nv = A
    if len(nv) == 3:
        if type(nv[1]) is not list and type(nv[2]) is not list:
            nv[0] = A[0] + "(" + str(A[1]) + ")(" + str(A[2]) + ")"
        elif type(nv[1]) is not list:
            if nv[2] == []:
                nv[0] = A[0] + "(" + str(A[1]) + ")()"
            else:
                nv[2][0] = racine_luka(nv[2])
                nv[0] = A[0] + "(" + str(A[1]) + ")(" + nv[2][0] + ")"
        elif type(nv[2]) is not list:
            if nv[1] == []:
                nv[0] = A[0] + "()(" + str(A[2]) + ")"
            else:
                nv[1][0] = racine_luka(nv[1])
                nv[0] = A[0] + "(" + nv[1][0] + ")(" + str(A[2]) + ")"
        else:
            if nv[1] == [] and nv[2] == []:
                nv[0] = nv[0] + "()()"
            elif nv[1] == []:
                nv[2][0] = racine_luka(nv[2])
                nv[0] = nv[0] + "()(" + nv[2][0] + ")"
            elif nv[2] == []:
                nv[1][0] = racine_luka(nv[1])
                nv[0] = nv[0] + "(" + nv[1][0] + ")()"
            else:
                nv[1][0] = racine_luka(nv[1])
                nv[2][0] = racine_luka(nv[2])
                nv[0] = nv[0] + "(" + nv[1][0] + ")(" + nv[2][0] + ")"
        return nv[0]
    elif len(nv) == 2:
        if type(nv[1]) is not list:
            nv[0] = A[0] + "(" + str(A[1]) + ")"
        else:
            nv[1][0] = racine_luka(nv[1])
            nv[0] = A[0] + "(" + nv[1][0] + ")()"
        return nv[0]
    else:  # nv de taille 1 ou 0
        if nv == []:
            return "()"
        return nv[0]


def luka(arb):
    """
    La fonction a pour paramètre l'arbre de décision entier à modifier. Il appelle la fonction
    récurrente racine_luka sur la tête de l'arbre.
    :param arb: Arbre de décision
    :return: Arbre de décision enrichi par les mots de lukasievicz
    """
    if type(arb) is not list or len(arb) == 1:
        return arb
    else:
        nv = arb
        # On donne la tête de l'arbre arb
        nv[0] = racine_luka(arb)
        return nv


def list_racine(arb):
    """
    :param luka: arbre de décision enrichi par les mots de lukasievicz
    :return: la liste des mots lukasievicz contenu dans l'arbre luka
    """
    racine = []
    if arb == [] or arb is None:
        return racine
    elif type(arb) is not list:
        racine.append(arb)
        return racine
    else:
        if type(arb[0]) is not list:
            racine.append(arb[0])
            if len(arb) == 1:
                return racine
            else:
                return racine + list_racine(arb[1:])
        else:
            return racine + list_racine(arb[0]) + list_racine(arb[1:])


def racine_count(lr):
    """
    :param lr: liste des racines lukasievicz ou non (par exemple le résultat de la fonction list_racine)
    :return: le dictionnaire de la liste lr, ainsi il n'y a plus de doublons. Les clés sont les racines
    (ou mots de lukasievicz) et les valeurs leur nombre d'occurrence dans l'arbre correspondant.
    """
    return {a: lr.count(a) for a in lr}


# Question 2.8
def compression(luka, dico):
    """
    Fonction recurrente qui depuis un sous-arbre de décision enrichi par les mots de lukasievicz
    construit un arbre compressé (cad: en fusionnant les sous-arbres communs).
    :param luka: arbre de décision enrichi par les mots de lukasievicz
    :param dico: dictionnaire vide
    :return: arbre de décision (sans mots de lukasievicz) compressé
    """
    if luka == [] or type(luka) is not list:
        return luka
    else:
        if luka[0] in dico:
            luka[0] = dico[luka[0]]
        else:
            nx = luka[0].split("(")[0]  # recupere seulement le nom du noeud d'origine (ex: 'x1')
            if nx in dico:
                dico[nx] = dico[nx] + 1
                nx = nx + str(dico[nx])
            else:
                dico[nx] = 1
                nx = nx + '1'
            dico[luka[0]] = nx
            luka[0] = nx
        luka[1] = compression(luka[1], dico)
        luka[2] = compression(luka[2], dico)
        return luka


# Question 2.9
def node_lien_dot(dot, arb, dico, mere, compresse):
    """
    Hyp: On considère que arb est verifié comme liste de 3 elements.
    Cette fonction ne rend rien, elle rajoute seulement les sous noeuds au dot et les liens qui les
    relient.
    :param dot: parametre dot
    :param arb: arbre de décision (enrichi ou pas par les mots de lukasievicz)
    :param dico: parametre dico
    :param mere: le nom du noeud parent à la tête de l'arbre arb
    :param compresse: booleen qui si à True indique que l'arbre doit être représenté sous forme
    compressée, normal sinon
    :return: rien
    """
    if type(arb[1]) is list:  # arb[1] représente l'arbre gauche
        if arb[1] == []:
            return
        if arb[1][0] in dico:
            dico[arb[1][0]] = dico[arb[1][0]] + 1
        else:
            dico[arb[1][0]] = 1
        if not compresse:
            fils1 = str(arb[1][0]) + str(dico[arb[1][0]])
        else:
            fils1 = str(arb[1][0]) + "1"
        dot.node(fils1, str(arb[1][0]).split('(')[0])
        dot.edge(mere, fils1, style="dotted")
        if dico[arb[1][0]] <= 1 or not compresse:
            node_lien_dot(dot, arb[1], dico, fils1, compresse)
    else:
        if arb[1] in dico and not compresse:
            dico[arb[1]] = dico[arb[1]] + 1
        else:
            dico[arb[1]] = 1
        if not compresse:
            fils1 = str(arb[1]) + str(dico[arb[1]])
        else:
            fils1 = str(arb[1]) + "1"
        dot.node(fils1, str(arb[1]).split('(')[0])
        dot.edge(mere, fils1, style="dotted")
    if type(arb[2]) is list:  # arb[2] représente l'arbre droit
        if arb[2] == []:
            return
        if arb[2][0] in dico:
            dico[arb[2][0]] = dico[arb[2][0]] + 1
        else:
            dico[arb[2][0]] = 1
        if not compresse:
            fils2 = str(arb[2][0]) + str(dico[arb[2][0]])
        else:
            fils2 = str(arb[2][0]) + "1"
        dot.node(fils2, str(arb[2][0]).split('(')[0])
        dot.edge(mere, fils2)
        if dico[arb[2][0]] <= 1 or not compresse:
            node_lien_dot(dot, arb[2], dico, fils2, compresse)
    else:
        if arb[2] in dico and not compresse:
            dico[arb[2]] = dico[arb[2]] + 1
        else:
            dico[arb[2]] = 1
        if not compresse:
            fils2 = str(arb[2]) + str(dico[arb[2]])
        else:
            fils2 = str(arb[2]) + "1"
        dot.node(fils2, str(arb[2]).split('(')[0])
        dot.edge(mere, fils2)


def dot(arb, compresse):
    """
    :param arb: arbre de décision (enrichi ou non par les mots de lukasievicz)
    :param compresse: booleen qui indique si l'arbre est sous forme compressée ou non
    :return: un dot que l'on pourra afficher par la suite avec la fonction render
    """
    dot = Graph(filename='Test.dat')
    if arb == [] or arb is None:
        return dot
    elif type(arb) is not list:
        dot.node(str(arb), str(arb))
        return dot
    else:
        dico = {arb[0]: 1}
        mere = str(arb[0]) + str(dico[arb[0]])
        dot.node(mere, str(arb[0]).split('(')[0])
        node_lien_dot(dot, arb, dico, mere, compresse)
        # print("dico (fct dot): ", dico, "\n nbr noeuds :", len(dico))
        return dot

