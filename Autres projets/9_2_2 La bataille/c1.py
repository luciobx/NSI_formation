# By Luc VINCENT
# 2021.11.20
# concepteur c1
# c1.py 1.0
# luc.vincent@ac-bordeaux.fr

# importer le hasard
from random import randint

def echanger(tab:list, pos1:int, pos2:int)->None:
    '''
    echanger en place la valeur de deux elements d'un tableau d'entier
    Args :
    tab : list
    pos1 : int
    pos2 : int
    CU:
    0<=pos1<len(tab)
    0<=pos2<len(tab)
    Raises:
    TypeError : pos1 et pos2 entier tab est une liste
    AssertionError : CU
    Exemples :
    >>> tas = [3, 5, 7]
    >>> echanger(tas, 0, 2)
    >>> tas
    [7, 5, 3]
    '''
    # respect des pré-conditions
    if not isinstance(pos1, int) or \
       not isinstance(pos2, int) or \
       not isinstance(tab, list):
        raise TypeError("Respecter tab:list, pos1:int, pos2:int")
    assert 0 <= pos1 < len(tab) and \
           0 <= pos2 < len(tab), 'CU non respectées'
    # Eventuellement ajouter un test sur les élements de tab
   
    mem = tab[pos1]
    tab[pos1] = tab[pos2]
    tab[pos2] = mem
    

def  melanger(tab:list)->list:
    '''
    melanger les elements d'un tableau d'entiers
    Args : tab un tableau d'entiers
    Returns : tabmix un tableau mélangé
    Invariant : tab
    Raises:
    TypeError : tab est une liste
    '''
    # respect des préconditions
    if not isinstance(tab, list):
        raise TypeError("Respecter tab:list")
    
    # creer la structure de retour
    tabmix = [0 for i in range(len(tab))]
    
    # recopier le tableau donne en argurment
    for i in range(len(tab)):
        tabmix[i] = tab[i]
    
    # indice initial de la carte à echanger
    i_carte = len(tabmix)-1
    
    for x in range(i_carte, 0, -1):
        i = randint(0, i_carte)
        echanger(tabmix, i, i_carte)
        
    # renvoyer le nouveau tableau melange
    return tabmix
 

if __name__ == "__main__":
    import doctest
    print(doctest.testmod(verbose = False))
    
    # creer le paquet de carte
    paquet = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, \
              1, 2, 3, 4, 5, 6, 7, 8, 9, 10, \
              1, 2, 3, 4, 5, 6, 7, 8, 9, 10, \
              1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    paquet_m = melanger(paquet)
    print(paquet)
    print(paquet_m)
    


