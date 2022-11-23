#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Author: Christophe Viroulaud
@Time:   Jeudi 25 Novembre 2021 12:27
"""
from constantes import *
from fonctions_placement import *
from fonctions_verif import *
from rendu_console import *

# initialisation
grille = initialiser_grille(LARGEUR, HAUTEUR)
# affichage
dessiner_grille(grille)

# initialisation pour première entrée dans la boucle
ligne, colonne = 0, 0
joueur = ROUGE

# boucle de jeu
while not verif_gagnant(grille, joueur, ligne, colonne):
    # au tour de l'autre joueur
    joueur = changer_joueur(joueur)

    # demande la colonne choisie (tant qu'elle est pleine)
    colonne = choisir_colonne()
    while est_remplie(grille, colonne):
        colonne = choisir_colonne()

    # place le jeton
    ligne = placer_jeton(grille, colonne, joueur)

    # affichage
    dessiner_grille(grille)

# fin du jeu
afficher_gagnant(joueur)
