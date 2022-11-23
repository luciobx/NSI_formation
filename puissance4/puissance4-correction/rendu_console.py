#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Author: Christophe Viroulaud
@Time:   Samedi 26 Mars 2022 13:41
"""
from constantes import *


def dessiner_grille(grille: list) -> None:
    for l in range(HAUTEUR):
        # print("-"*10)
        for c in range(LARGEUR):
            print(dessiner_jeton(grille, l, c), end="")
        print("|")


def dessiner_jeton(grille: list, l: int, c: int) -> str:
    return "|"+couleur_jeton(grille[l][c])


def couleur_jeton(jeton: int) -> str:
    if jeton == JAUNE:
        return "J"
    elif jeton == ROUGE:
        return "R"
    else:
        return " "


def afficher_gagnant(joueur: int) -> None:
    """
    crée la phrase pour le gagnant

    Args:
        joueur (int): le joueur gagnant
    """
    if joueur == ROUGE:
        couleur = "rouge"
    else:
        couleur = "jaune"
    print(f"Le joueur {couleur} a gagné.")



