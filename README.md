# ALGAV
Projet M1 en ALGAV (ALGorithme Avancé) sur la compression des arbres, en particulier les diagrammes de décision binaire (ROBDD)

## Fonctionnalités :

Au sein de ce dépôt se trouve 3 fichiers de code « projet » avec à chaque fois leur propre fichier test:

-	**echauffement.py** pour la première partie avec le fichier **test1.py** dans lequel, on retrouve quelques tests.

-	**arbre_decision_2.py** pour la deuxième partie (jusqu'à la fonction *dot*) avec le fichier de test : **test2.py**.

-	**Robdd.py** qui contient les fonctions de la troisième partie et son fichier **test3.py** avec les tests correspondants.

-	**exp.py** qui contient les fonctions pour réaliser les expérimentations.

On y retrouve également le fichier **testsout.py** qui regroupe notamment deux autres tests.

De plus, pour les tests **test2.py**, **test3.py** et **testsout.py**, il faut ajouter un argument en ligne de commande: 0 si vous ne voulez pas d’affichages de graphe, 1 sinon.

Pour exécuter un test sur terminal, on se place dans le répertoire contenant les fichiers du projet et on écrit la commande : `python3 test1.py` ou `python3 test{2,3,out}.py 0/1`. 

