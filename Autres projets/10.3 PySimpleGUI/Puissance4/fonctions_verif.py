# By Luc VINCENT
# 2022.06.08
# Puissance4
# Source @Author: Christophe Viroulaud
# @Time:   Jeudi 25 Novembre 2021 19:26
# Focntions vérification
# 1.0
# luc.vincent@ac-bordeaux.fr
# sys.version '3.7.9 (tags/v3.7.9:13c94747c7, Aug 17 2020, 18:01:55) [MSC v.1900 32 bit (Intel)]'

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
            verif_horizontale(grille, joueur, ligne) or \
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
    u_l, u_c = ligne, colonne

    # vérification
    compteur = 0
    while u_l < N_HAUT and grille[u_l][u_c] == joueur and compteur < 4:
        compteur = compteur+1
        u_l = u_l + 1
    # si 4 jetons alignés renvoie True
    return compteur == 4


def verif_horizontale(grille: list, joueur: int, ligne: int) -> bool:
    """
    vérifie si l'alignement horizontal est gagnant
    on regarde se limite aux 3 cases gauches et 3 cases droites

    Args:
        grille (list): le jeu
        joueur (int): la couleur en cours
        ligne (int): la ligne du dernier jeton placé
        colonne (int): la colonne du dernier jeton placé (inutilisée)

    Returns:
        bool: True si gagnant
    """
    # se place en début de ligne ou au moins 3 cases en arrière
    u_l, u_c = ligne, 0
    recul = 0
    while recul < 3 and u_c > 0:
        u_c = u_c - 1
        recul = recul + 1

    # vérification
    compteur = 0
    while u_c < N_LARG and compteur < 4:
        if grille[u_l][u_c] == joueur:
            compteur = compteur + 1
        else:
            compteur = 0
        u_c = u_c + 1

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
    # on va se placer en début d alignement (bas gauche) ou au moins à trois cases en arrière (au droit)
    u_l, u_c = ligne, colonne
    recul = 0
    while recul < 3 and u_l < (N_HAUT-1) and u_c > 0:
        u_l = u_l + 1
        u_c = u_c - 1
        recul = recul + 1

    # vérification
    compteur = 0
    while u_c < N_LARG and u_l >= 0 and compteur < 4:
        if grille[u_l][u_c] == joueur:
            compteur = compteur + 1
        else:
            compteur = 0
        u_c = u_c + 1
        u_l = u_l - 1

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
    u_l, u_c = ligne, colonne
    recul = 0
    while recul < 3 and u_l > 0 and u_c > 0:
        u_l = u_l - 1
        u_c = u_c - 1
        recul = recul + 1

    # vérification
    compteur = 0
    while u_c < N_LARG and u_l < N_HAUT and compteur < 4:
        if grille[u_l][u_c] == joueur:
            compteur = compteur+1
        else:
            compteur = 0
        u_c = u_c + 1
        u_l = u_l + 1

    # si 4 jetons alignés renvoie True
    return compteur == 4

if __name__ == "__main__":
    # intialiser une grille
    import calculs  as c
    a_colors_board = c.initialiser_grille(N_LARG, N_HAUT)
    # intialiser une situation de jeu par défaut
    a_ligne, a_colonne = 0, 0
    a_joueur = ROUGE
    print(a_colors_board)
    assert verif_gagnant(a_colors_board, a_joueur, a_ligne, a_colonne) is False, "verif_gagnant KO"
    
    