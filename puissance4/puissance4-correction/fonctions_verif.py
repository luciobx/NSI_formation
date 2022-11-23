#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Author: Christophe Viroulaud
@Time:   Jeudi 25 Novembre 2021 19:26
"""
from constantes import *


def verif_gagnant(grille: list, joueur: int, ligne: int, colonne: int) -> bool:
    """
    Vérifie si la position est gagnante

    Args:
        grille (list): le jeu
        joueur (int): la couleur du joueur
        ligne (int): ligne du dernier jeton
        colonne (int): colonne du dernier jeton

    Returns:
        bool: True si la position est gagnante
    """
    if verif_verticale(grille, joueur, ligne, colonne) or \
            verif_horizontale(grille, joueur, ligne, colonne) or \
            verif_diagonale_montante(grille, joueur, ligne, colonne) or \
            verif_diagonale_descendante(grille, joueur, ligne, colonne):
        return True
    else:
        return False


def verif_verticale(grille: list, joueur: int, ligne: int, colonne: int) -> bool:
    """
    vérifie si l'alignement vertical est gagnant
    on ne regarde que la verticale descendante en partant du pion

    Args:
        grille (list): le jeu
        joueur (int): la couleur en cours
        ligne (int): la ligne du dernier jeton placé
        colonne (int): la colonne du dernier jeton placé

    Returns:
        bool: True si gagnant
    """
    # démarre à l'endroit du dernier pion descendu
    l, c = ligne, colonne

    # vérification
    compteur = 0
    while l < HAUTEUR and grille[l][c] == joueur and compteur < 4:
        compteur = compteur+1
        l = l+1
    # si 4 jetons alignés renvoie True
    return compteur == 4


def verif_horizontale(grille: list, joueur: int, ligne: int, colonne: int) -> bool:
    """
    vérifie si l'alignement horizontal est gagnant
    on regarde se limite aux 3 cases gauches et 3 cases droites

    Args:
        grille (list): le jeu
        joueur (int): la couleur en cours
        ligne (int): la ligne du dernier jeton placé
        colonne (int): la colonne du dernier jeton placé

    Returns:
        bool: True si gagnant
    """
    # se place en début de ligne ou au moins 3 cases en arrière
    l, c = ligne, 0
    recul = 0
    while recul < 3 and c > 0:
        c = c-1
        recul = recul+1

    # vérification
    compteur = 0
    while c < LARGEUR and compteur < 4:
        if grille[l][c] == joueur:
            compteur = compteur+1
        else:
            compteur = 0
        c = c+1

    # si 4 jetons alignés renvoie True
    return compteur == 4


def verif_diagonale_montante(grille: list, joueur: int, ligne: int, colonne: int) -> bool:
    """
    vérifie si l'alignement diagonal est gagnant
    on regarde se limite aux 3 cases gauches et 3 cases droites

    Args:
        grille (list): le jeu
        joueur (int): la couleur en cours
        ligne (int): la ligne du dernier jeton placé
        colonne (int): la colonne du dernier jeton placé

    Returns:
        bool: True si gagnant
    """
    # se place en début de diagonale ou au moins à trois cases en arrière
    l, c = ligne, colonne
    recul = 0
    while recul < 3 and l < (HAUTEUR-1) and c > 0:
        l = l+1
        c = c-1
        recul = recul+1

    # vérification
    compteur = 0
    while c < LARGEUR and l >= 0 and compteur < 4:
        if grille[l][c] == joueur:
            compteur = compteur+1
        else:
            compteur = 0
        c = c+1
        l = l-1

    # si 4 jetons alignés renvoie True
    return compteur == 4


def verif_diagonale_descendante(grille: list, joueur: int, ligne: int, colonne: int) -> bool:
    """
    vérifie si l'alignement diagonal est gagnant
    on regarde se limite aux 3 cases gauches et 3 cases droites

    Args:
        grille (list): le jeu
        joueur (int): la couleur en cours
        ligne (int): la ligne du dernier jeton placé
        colonne (int): la colonne du dernier jeton placé

    Returns:
        bool: True si gagnant
    """
    # se place en début de diagonale ou au moins à trois cases en arrière
    l, c = ligne, colonne
    recul = 0
    while recul < 3 and l > 0 and c > 0:
        l = l-1
        c = c-1
        recul = recul+1

    # vérification
    compteur = 0
    while c < LARGEUR and l < HAUTEUR and compteur < 4:
        if grille[l][c] == joueur:
            compteur = compteur+1
        else:
            compteur = 0
        c = c+1
        l = l+1

    # si 4 jetons alignés renvoie True
    return compteur == 4
