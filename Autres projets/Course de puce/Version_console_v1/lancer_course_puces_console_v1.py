"""
Nom : ...
Prénom : ...

Création : 17/11/2021
Modification : 17/11/2021
Licence : GPLv3

----------------------------------------------------
Projet : simuler une course de sauts de puces
Script principal

----------------------------------------------------
Version 1 : en console
"""



# ---------------------Le module avec les fonctions -------------------------------------------------
from course_puces import *



# ---------------------Initialisation -------------------------------------------------

# Créer le tableau des puces
puces = creer_puces(5)   # 5 puces participent à la course

# Créer la grille de déplacement
grille = creer_grille(10, puces)  # grille de 10 cases pour les déplacements



# ----------------------Programme principale-------------------------------------------
# Répéter tant que les puces ne sont pas arrvées
while puces_arrivees(grille, puces) == False:
    afficher_grille_puces(grille)
    attendre_action_utilisateur()
    grille, puces = deplacer_puces(grille, puces)
afficher_grille_puces(grille)  
  
# Pour chaque puce arrivée, afficher "arrivée"
afficher_puces_arrivees(puces) 
    

