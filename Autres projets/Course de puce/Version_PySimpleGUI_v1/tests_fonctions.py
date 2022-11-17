"""
Nom : ...
Prénom : ...

Création : 17/11/2021
Modification : 17/11/2021
Licence : GPLv3

#----------------------------------------------------
Projet : simuler une course de sauts de puces

Fichier  : tests_fonction.py
- tests de toutes les fonctions avant intégration

#----------------------------------------------------
Version 1 : en console
"""

# -------- Les modules nécessaires --------
import time
import pprint

# -------- Les modules du projet --------
from course_puces import *




# -------- Tests des fonctions du module course_puces.py-------
#--------------------------------------------------------------

# Test 1 : création des puces
"""
puces = creer_puces(5)   # 5 puces participent à la course
pprint.pprint(puces, width = 80)
"""


# Test 2 : création de la grille
"""
puces = creer_puces(5)   # 5 puces participent à la course
grille = creer_grille(10, puces)  # grille de 10 cases pour les déplacements
pprint.pprint(grille, width = 80)
"""


# Test 4 : afficher la grille - version 1
# Une course sur 10 cases donne une grille de largeur 13
# 10 + cases initiale + 2 cases de débordement
"""
grille =    [[0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0]]
afficher_grille_puces(grille)
print(f"Hauteur : {len(grille)}")
print(f"Largeur : {len(grille[0])}")
"""


# Test 5 : afficher la grille - version 2
"""
puces = creer_puces(5)   # 5 puces participent à la course
grille = creer_grille(10, puces)  # Course sur 10 cases, grille de largeur 13
pprint.pprint(grille)
afficher_grille_puces(grille)
print(f"Hauteur : {len(grille)}")
print(f"Largeur : {len(grille[0])}")
"""


# Test 6 : déplacer les puces
"""
puces = creer_puces(5)   # 5 puces participent à la course
grille = creer_grille(10, puces)  # Course sur 10 cases, grille de largeur 13

print("Positions initiales")
afficher_grille_puces(grille)


for s in range(1, 4 + 1):
    time.sleep(2)
    print(f"Saut N° {s}")
    grille, puces = deplacer_puces(grille, puces)
    afficher_grille_puces(grille)
"""


# Test 7 : vérifier qu'une puce est arrivée - version 1
"""
# Tableau des puces, on modifie les valeurs de pos pour les tests
puces = [{'couleur': 'white', 'nom': 'puce1', 'pos': 12, 'taille': 2},
         {'couleur': 'yellow', 'nom': 'puce2', 'pos': 9, 'taille': 1},
         {'couleur': 'bleu', 'nom': 'puce3', 'pos': 9, 'taille': 3},
         {'couleur': 'green', 'nom': 'puce4', 'pos': 5, 'taille': 4},
         {'couleur': 'white', 'nom': 'puce5', 'pos': 2, 'taille': 1}]

# Créer une grille de hauteur p et de largeur n + 3
p = len(puces)
n = 10
grille = [ [0 for j in range(n + 1 + 2) ] for i in range(p)] # 3 cases en plus
    
# ---- Placer puces dans la grille ----
for i in range(len(puces)):
    puce = puces[i]
    grille[i][puce['pos']] = i + 1  # Inscrire le numéro de puce (i+1) en position   pos
    

pprint.pprint(puces)
pprint.pprint(grille)
print(puces_arrivees(grille, puces))
"""


# Test 8 : vérifier qu'une puce est arrivée - version 2
"""
puces = creer_puces(5)   # 5 puces participent à la course
grille = creer_grille(10, puces)  # Course sur 10 cases, grille de largeur 13

print("Positions initiales")
afficher_grille_puces(grille)

s = 0 # compteur du nombre de sauts
while puces_arrivees(grille, puces) == False:
    time.sleep(1)
    s += 1
    print(f"Saut N° {s}")
    grille, puces = deplacer_puces(grille, puces)
    afficher_grille_puces(grille)
print("Au moins une puce est arrivée")
"""



# Test 9 : attendre choix de l'utilisateur
"""
print("Début")
while True:
    print("Attente action sur le clavier")
    attendre_action_utilisateur()
"""
    



# Test 10 : simuler une course

puces = creer_puces(5)   # 5 puces participent à la course
grille = creer_grille(10, puces)  # grille de 10 cases pour les déplacements
#afficher_grille_puces(grille)
simuler_course(grille, puces)



