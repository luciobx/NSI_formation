# By Luc VINCENT 
# 2021.11.29
# concepteur c5
# c5.py 1.0
# luc.vincent@ac-bordeaux.fr

def afficher(vainqueur:int)->None:
    '''
    Afficher le vainqueur du jeu 1 ou 2 ou le match nul
    Args:
    vainqueur: int
    CU :
    0 si match nul
    1 si le joueur 1 a gagné
    2 si le joueur 2 a gagné
    Raises:
    TypeError : vainqueur est de type entier
    AssertionError : Non respect des CU
    Exemples:
    >>> afficher(0)
    C'est un match nul
    >>> afficher(1)
    Le joueur 1 a gagné la partie
    >>> afficher(2)
    Le joueur 2 a gagné la partie
    '''
    # respect des pré-conditions
    if not isinstance(vainqueur, int):
        raise TypeError("vainqueur est de type entier")
    assert vainqueur in (0, 1, 2), "CU non repsectées"
        
    if vainqueur == 0:
        print("C'est un match nul")
    else:
        print(f"Le joueur {vainqueur} a gagné la partie")
    
if __name__ == "__main__":
    import doctest
    print(doctest.testmod(verbose = False))