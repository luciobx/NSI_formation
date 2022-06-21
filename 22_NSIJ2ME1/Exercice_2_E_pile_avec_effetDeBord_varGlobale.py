# By Luc VINCENT 
# 2022.05.25
# 22-NSIJ2ME1 Exercice 2 les structures de données.
# La poussette est un jeu de cartes en solitaire
# implantation dans une pile travail en place
# 1.0
# luc.vincent@ac-bordeaux.fr
# sys.version '3.7.9 (tags/v3.7.9:13c94747c7, Aug 17 2020, 18:01:55) [MSC v.1900 32 bit (Intel)]'
#


def creer_pile_vide() :
    """Renvoyer une liste vide"""
    return []

def est_vide(p):
    """Renvoie le booléen True si la pile est vide, False sinon."""
    return p==[]

def empiler(p, element):
    """Place l'élément v au sommet de la pile."""
    p.append(element)

def depiler(p):
    """Retirer un élément
    
    Retire et renvoie l’élément placé au sommet de la pile,
    si la pile n’est pas vide.
    """
    if not est_vide(p):
        return p.pop()
    else:
        return None

def sommet(p):
    """Renvoyer le sommet

    Renvoie l’élément placé au sommet de la pile,
    si la pile n’est pas vide.
    """
    if not est_vide(p):
        return p[-1]
    else:
        return None

def taille(p):
    """Renvoyer la taille de la pile."""
    return len(p)

def reduire_triplet_au_sommet():
    """Reduction de la pile p
    
    permet de supprimer l'élément central des trois premiers éléments
    en partant du haut de la pile,
    si l'élément du  bas et du haut sont de même parité.
    Les éléments dépilés et non supprimés sont replacés
    dans le bon ordre dans la pile.
    """
    # la pile p étant une liste c'est un objet muable
    # Cette fonction réduit le sommet de la pile globale une_pile
    a = depiler(une_pile)
    b = depiler(une_pile)
    c = sommet(une_pile)
    if a % 2 != c % 2:
        empiler(une_pile, b)
    empiler(une_pile, a)


def parcourir_pile_en_reduisant():
    """ parcourir la pile p en réduisant
    
    parcourt la pile du haut vers le bas en procédant aux réductions
    pour chaque triplet rencontré quand cela est possible
    """
    # la pile p étant une liste c'est un objet muable
    # Cette fonction réduit la pile globale une_pile
    q = creer_pile_vide()
    while taille(une_pile) >= 3 :
        reduire_triplet_au_sommet()
        e = depiler(une_pile)
        empiler(q, e)
    while not est_vide(q):
        e = depiler(q)
        empiler(une_pile, e)

def jouer():
    """Simplifier entièrement la pile"""
    # la pile p étant une liste c'est un objet muable
    # Cette fonction simplifie en place la pile une_pile
    # la variable est globale "une_pile"
    taille_p_ar = taille(une_pile) # taille_p_ar avant reduction
    parcourir_pile_en_reduisant()
    if taille(une_pile) != taille_p_ar:  
        jouer()


def affichage():
    """Affichage de la pile avec 3 chiffres au plus"""
    print()
    for i in range(len(une_pile)-1,-1,-1):
        print("|" + " "*(3-len(str(une_pile[i]) ))+str(une_pile[i])+"|")
    print("+---+")

if __name__ == "__main__":
    # une_pile est une variable globale connue de toutes les fonctions
    une_pile = creer_pile_vide()
    poussette = (6, 9, 8, 3, 4, 5, 7)
    for value in poussette:
        empiler(une_pile, value)
    jouer()
    affichage()
    
    # poussette = (2, 4, 7, 8, 9, 4)
    # poussette = (1, 2, 4, 5, 4, 5)
    # poussette = (0, 2, 9, 4, 5, 4)
    # poussette = (1, 6, 7, 8, 4, 3)
