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





def initialiser_grille(nb_col: int, nb_lig: int) -> list:
    """
    construire la grille du jeu

    Args:
        nb_col (int): nombre de colonnes
        nb_lig (int): nombre de lignes

    Returns:
        list: un tableau de HAUTEUR lignes et LARGEUR colonnes [[col0, col1 ...], ligne1, ligne2]
        dont le contenu code la couleur du jeton
    """
    return [[VIDE for i in range(nb_col)] for j in range(nb_lig)]

def changer_joueur(joueur: int) -> int:
    """
    passe la main à l'autre joueur

    Args:
        joueur (int): joueur en cours (1 ou 2)

    Returns:
        int: l'autre joueur
    """
    return joueur % 2 + 1


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


def placer_jeton(grille: list, colonne: int, joueur) -> int:
    """
    place le jeton 
    Args:
        grille (list): le jeu
        ligne (int): la ligne
        colonne (int): la colonne
        joueur ([type]): la couleur du joueur
    Modifie en place la grille
    Returns:
        int: la ligne où le jeton s'est arrêté 
    """
    ligne = tomber_ligne(grille, colonne)
    grille[ligne][colonne] = joueur
    return ligne


def tomber_ligne(grille: list, colonne: int) -> int:
    """
    fait descendre le jeton dans la colonne

    Args:
        grille(list): la grille de jeu
        colonne (int): la colonne choisie

    Returns:
        int: la ligne où le pion doit être placé
    """
    ligne = 0
    while ligne < N_HAUT and grille[ligne][colonne] == VIDE:
        # on descend tant qu'on n'est pas en bas ou sur une case remplie
        ligne = ligne + 1

    # renvoie la dernière place vide
    return ligne-1

def est_pleine(grille: list) -> bool:
    """
    vérifie si la grille est remplie complètement

    Args:
        grille (list): le jeu
        colonne (int): la colonne

    Returns:
        bool: True si la grille est remplie
    """
    for col in range(len(grille[0])):
        if not est_remplie(grille, col):
            # il reste une place libre
            return False
    return True
    

if __name__ == "__main__":
    assert initialiser_grille(3, 2) == [[0, 0, 0], [0, 0, 0]], 'initialiser_grille(3, 2) KO'
    assert changer_joueur(1) == 2 and changer_joueur(2) == 1 , 'changer_joueur KO'

    assert(est_pleine([[0, 1, 0], [0, 0, 0]])) == False, "est_pleine KO"
    assert(est_pleine([[2, 1, 2], [1, 2, 1]])) == True, "est_pleine KO"
