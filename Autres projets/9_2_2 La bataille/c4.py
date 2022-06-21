# By Luc VINCENT 
# 2021.11.20
# concepteur c3
# c4.py 1.0
# luc.vincent@ac-bordeaux.fr

def compter(joueur:list)->int:
    '''
    Renvoyer le nombre de carte d'un joueur
    Args:
    joueur : list tableau d'entier main et tas du joueur
    Returns :
    nb_carte : int nombre de carte main plus tas
    Exemples
    >>> compter([4, 9, 4, 7, 8, 1, 4, 4, 1, 3])
    10
    '''
    # respect des pré-conditions
    if not isinstance(joueur, list):
        raise TypeError("Respecter joueur:list")
    # Eventuellement ajouter un test sur les élements de joueur
    nb_carte = 0
    for i in range(len(joueur)):
        if joueur[i] != 0:
            nb_carte += 1
    return nb_carte
        
    

def quel_vainqueur (j1:list, j2:list)->int:
    '''
    Identifier le tableau j1 ou j2 qui contient le plus grand nombre de valeur non nulle
    Args:
    j1 : list tableau d'entier main et tas du joueur 1
    j2 : list tableau d'entier main et tas du joueur 2
    Returns :
    n: int
    0 si égalité
    1 si j1
    2 si j2
    CU:
    len(j1) egale len(j2) et est paire
    Raises:
    TypeError : j1 et j2 sont des listes d'entiers
    Exemples
    >>> quel_vainqueur([0, 0, 3, 9, 0, 0, 0, 1, 7, 0], [8, 8, 0, 0, 4, 4, 7, 0, 0, 2])
    2
    >>> quel_vainqueur([4, 9, 4, 7, 8, 1, 4, 4, 1, 3], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    1
    >>> quel_vainqueur([4, 0, 5, 0, 8, 3, 0, 2, 0, 0], [0, 9, 0, 8, 8, 0, 6, 0, 7, 0] )
    0
    '''
    # respect des pré-conditions
    if not isinstance(j1, list) or \
       not isinstance(j2, list):      
        raise TypeError("Respecter j1:list, j2:list")
    assert len(j1) == len(j2) and \
           len(j1) % 2 == 0, 'CU non respectées'
    # Eventuellement ajouter un test sur les élements de j1 et j2
    nb_carte_1 = compter(j1)
    nb_carte_2 = compter(j2)
    if nb_carte_1 > nb_carte_2:
        return 1
    elif nb_carte_1 < nb_carte_2:
        return 2
    else:
        return 0




if __name__ == "__main__":
    from random import randint
    import doctest
    print(doctest.testmod(verbose = False))