# By Luc VINCENT 
# 2021.11.20
# concepteur c3
# c3.py 1.0
# luc.vincent@ac-bordeaux.fr

def ramasser(gagnant:list, perdant:list, tour:int, n_bat:int)->None:
    '''
    Modifier les jeux du jouer perdant et du joueur gagnant
    Args:
    gagnant : list la main-tas du joueur gagnant
    perdant : list la main-tas du joueur perdant
    tour : int la ième tour joué en partant de 0
    n_bat : le nombre de bataille à ramasser sous le tour en cours
    CU:
    len(gagnant) egale len(perdant) et est paire
    Raises:
    TypeError : gagnant et perdant sont des listes, n_bat un entier
    Exemples :
    >>> g1 = [5, 2, 5, 4, 9, 0, 0, 0, 0, 0]
    >>> g2 = [7, 6, 6, 3, 3, 0, 0, 0, 0, 0]
    >>> ramasser(g1, g2, 0, 0)
    >>> g1
    [5, 2, 5, 4, 9, 7, 0, 0, 0, 0]
    >>> g2
    [0, 6, 6, 3, 3, 0, 0, 0, 0, 0]
    '''
     
    # respect des pré-conditions
    if not isinstance(gagnant, list) or \
       not isinstance(perdant, list) or \
       not isinstance(n_bat, int):
        raise TypeError("Respecter gagnant:list, perdant:list, tour:int, n_bat:int")
    assert len(gagnant) == len(perdant) and \
           len(gagnant) % 2 == 0, 'CU non respectées'
    # Eventuellement ajouter un test sur les élements de gagnant et perdant
    
    tas = len(gagnant) // 2
    for i in range(0, n_bat + 1):
        gagnant[tour + tas - i] = perdant[tour - i]
        # la carte est perdue
        perdant[tour - i] = 0


def fin_plis(j1:list, j2:list)->bool:
    '''
    Faire des plis
    Args :
    j1 : list tableau d'entier main et tas du joueur 1
    j2 : list tableau d'entier main et tas du joueur 2
    Returns : True
    lorsque l'un des joueurs a joué toutes ses cartes
    '''
    # Initialiser
    i_carte = 0
    nb_bataille = 0
    # Pour permettre de faire des tests sur de petits tas
    tas = len(j1) // 2
    
    # Tant que un joueur a des cartes à jouer
    while i_carte < tas:
        if j1[i_carte] > j2[i_carte]:
            # Jouer 1 gagnant
            ramasser(j1, j2, i_carte, nb_bataille)
            nb_bataille = 0
        elif j1[i_carte] < j2[i_carte]:
            # Jouer 2 gagnant
            ramasser(j2, j1, i_carte, nb_bataille)
            nb_bataille = 0
        else:
            # bataille
            nb_bataille += 1
        # Jouer carte suivante
        i_carte += 1
    # fin de partie
    return None

def generateur(taille:int):
    '''
    Renvoyer une main et un tas
    Args :
    taille: int le nombre total carte et tas
    Returns :
    main : list une main tirée au hasard et un tas vide
    CU:
    taille est paire
    '''
    main = [0 for i in range(taille)]
    for i in range(taille // 2):
        main[i] = randint(1, 9)
    return main
    
def test_multiples(n:int):
    '''
    Réaliser n tests
    '''
    for i in range(n):
        print("Donne")
        joueur_1 = generateur(10)
        joueur_2 = generateur(10)
        print("Joueur 1", joueur_1)
        print("Joueur 2", joueur_2)
        fin_plis(joueur_1, joueur_2)
        print("Fin")
        print("Joueur 1",joueur_1)
        print("Joueur 2",joueur_2) 
    


if __name__ == "__main__":
    from random import randint
    import doctest
    print(doctest.testmod(verbose = False))
    test_multiples(20)
#     joueur_1 = generateur(10)
#     joueur_2 = generateur(10)
#     print(joueur_1)
#     print(joueur_2)
#     print(fin_plis(joueur_1, joueur_2))
#     print(joueur_1)
#     print(joueur_2) 
    
    
    