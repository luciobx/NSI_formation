#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Author: Christophe Viroulaud
@Time:   Jeudi 25 Novembre 2021 12:29
"""
from constantes import *


def choisir_colonne() -> int:
    """
    demande la colonne
    vérifie si on ne sort pas de la grille

    Returns:
        int: la colonne choisie
    """
    col = LARGEUR #valeur trop grande
    while col<0 or col>=LARGEUR:
        col = int(input("Dans quelle colonne placez-vous le jeton? "))
    return col


def changer_joueur(joueur: int) -> int:
    """
    passe la main à l'autre joueur

    Args:
        joueur (int): joueur en cours

    Returns:
        int: l'autre joueur
    """
    return joueur % 2+1


def initialiser_grille(col: int, lig: int) -> list:
    """
    construire la grille du jeu. 
    Une place vide est marquée par un zéro.

    Args:
        col (int): nombre de colonnes
        lig (int): nombre de lignes

    Returns:
        list: un tableau de lig tableaux contenant chacun col zéros.
    """
    return [[VIDE for i in range(col)] for j in range(lig)]


def est_remplie(grille: list, colonne: int) -> bool:
    """
    vérifie si la colonne est remplie jusqu'en haut

    Args:
        grille (list): le jeu
        colonne (int): la colonne

    Returns:
        bool: True si la colonne est remplie
    """
    # il suffit de vérifier si l'emplacement le plus haut est vide
    return not(grille[0][colonne] == VIDE)


def placer_jeton(grille: list, col: int, joueur: int) -> int:
    """
    place le jeton dans la colonne choisie 
    en le faisant descendre dans la ligne 
    la plus basse possible 
    Args:
        grille (list): le jeu
        col (int): la colonne
        joueur (int): la couleur du joueur
    Returns:
        int: la ligne où le jeton est placé 
    """
    lig = 0
    # on n'est pas en bas ni sur une case remplie
    while lig+1 < HAUTEUR and grille[lig+1][col] == VIDE:
        lig = lig + 1

    # place le jeton du joueur
    grille[lig][col] = joueur
    return lig
