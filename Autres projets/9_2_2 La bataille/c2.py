# By Luc VINCENT
# 2021.11.20
# concepteur c2
# c2.py 1.0
# luc.vincent@ac-bordeaux.fr


def distribuer(tab:list, tab1:list, tab2:list)->None:
    '''
    Distribuer alternativement les valeurs du tableau tab
    dans les tableaux tab1 et tab2
    Args :
    tab : list tableau d'entier
    tab1 : list tableau d'entier
    tab2 : list tableau d'entier
    Returns : None
    CU:
    len(tab) egale len(tab1) egale len(tab2) et est paire
    Exemples :
    >>> tab = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    >>> tab1 = [0 for i in range(10)]
    >>> tab2 = [0 for i in range(10)]
    >>> distribuer(tab, tab1, tab2)
    >>> tab1
    [1, 3, 5, 7, 9, 0, 0, 0, 0, 0]
    >>> tab2
    [2, 4, 6, 8, 10, 0, 0, 0, 0, 0]
    '''
    
    # respect des pré-conditions
    if not isinstance(tab, list) or \
       not isinstance(tab1, list) or \
       not isinstance(tab2, list):
        raise TypeError("Respecter tab:list, tab1:list tab2:list")
    assert len(tab) == len(tab1) and \
           len(tab) == len(tab2)and \
           len(tab) % 2 == 0, 'CU non respectées'
    # Eventuellement ajouter un test sur les élements de tab
    
    # Distribuer
    for i in range(0, len(tab), 2):
        tab1[i//2] = tab[i]
        tab2[i//2] = tab[i+1]

if __name__ == "__main__":
    import doctest
    print(doctest.testmod(verbose = False))
    
    # creer le paquet de carte
    paquet = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, \
              1, 2, 3, 4, 5, 6, 7, 8, 9, 10, \
              1, 2, 3, 4, 5, 6, 7, 8, 9, 10, \
              1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # creer les mains des joueurs
    joueur_1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0,\
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0,\
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0,\
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                
    joueur_2 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0,\
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0,\
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0,\
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    distribuer(paquet, joueur_1, joueur_2)
    print(joueur_1)
    print(joueur_2)
    
