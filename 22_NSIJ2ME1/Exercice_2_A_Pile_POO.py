# By Luc VINCENT 
# 2022.05.25
# 22-NSIJ2ME1 Exercice 2 les structures de données.
# La poussette est un jeu de cartes en solitaire
# implantation dans une pile en POO
# 1.0
# luc.vincent@ac-bordeaux.fr
# sys.version '3.7.9 (tags/v3.7.9:13c94747c7, Aug 17 2020, 18:01:55) [MSC v.1900 32 bit (Intel)]'
#


class Pile:
    ''' Une pile à partir d'une list python'''
    def __init__(self):
        """instancier une pile vide sous forme d'une liste"""
        self.valeurs = []

    def empiler(self, valeur):
        """Place l'élément valeur au sommet de la pile"""
        self.valeurs.append(valeur)

    def depiler(self):
        """
        Retire et renvoie l’élément placé au sommet de la pile,
        si la pile n’est pas vide.
        """
        if not self.estvide():
            return self.valeurs.pop()
        else:
            raise NameError('impossible de depiler une pile vide')

    def estvide(self):
        """Renvoie le booléen True si la pile est vide, False sinon."""
        return self.valeurs == []
    
    def sommet(self):
        """
        Renvoie l’élément placé au sommet de la pile,
        si la pile n’est pas vide.
        """
        if not self.estvide():
            return self.valeurs[-1]
        else:
            raise NameError('Pas de sommet pour une pile vide !')
    
    def taille(self):
        """Renvoie la taille de la pile"""
        return len(self.valeurs)


    def __str__(self):
        """Afficher la pile"""
        ch = ''
        for x in self.valeurs:
            ch = "|\t" + str(x) + "\t|" + "\n" + ch
        ch = "\nEtat de la pile:\n" + ch
        return ch

def creer_pile_vide():
    '''renvoie une pile vide'''
    return Pile()

def est_vide(p):
    '''renvoie True si p est vide, False sinon'''
    return p.estvide()

def empiler(p, element):
    '''ajoute element au sommet de p'''
    p.empiler(element)
    
def depiler(p):
    '''retire l'élément au sommet de p et le renvoie'''
    return p.depiler()

def sommet(p):
    '''renvoie l'élément au sommet de p sans le retirer de p'''
    return p.sommet()

def taille(p):
    ''' renvoie le nombre d'éléments de p'''
    return p.taille()


def reduire_triplet_au_sommet(p):
    ''' Modification de la pile en place'''
    a = depiler(p)
    b = depiler(p)
    c = sommet(p)
    if a % 2 != c % 2:
    # Non reduction on replace b
        empiler(p, b)
    # On replace toujours a
    empiler(p, a)

def parcourir_pile_en_reduisant(p):
    # Dans cette forme on conserve la modification en place
    q = creer_pile_vide()
    while taille(p) >= 3: 
        print(p)
        reduire_triplet_au_sommet(p)
        e = depiler(p)
        empiler(q, e)
    while not est_vide(q):
        e = depiler(q)
        empiler(p, e)
    print(p)
    return p # pas vraiment utile puisque la pile est modifiée en place !

def jouer(p):
    ''' forme sujet avec modification'''
    taille_p_ar = taille(p) # taille_p_ar avant reduction
    q = parcourir_pile_en_reduisant(p)
    parcours = 1
    if taille(q) == taille_p_ar:  
        #On ne peut plus réduire
        return p
    else:
        # on peut encore réduire
        parcours += 1
        print(f'parcours : {parcours}')
        jouer(q)


def jouer(p):
    ''' forme imperative'''
    parcours = 1
    while True:
        print(f'parcours : {parcours}')
        taille_p_ar = taille(p) # taille_p_ar avant reduction
        parcourir_pile_en_reduisant(p)
        parcours += 1
        if taille(p) == taille_p_ar:  
            # on ne peut plus réduire
            break

def jouer(p):
    ''' forme recursive'''
    taille_p_ar = taille(p) # taille_p_ar avant reduction
    parcourir_pile_en_reduisant(p)
    parcours = 1
    if taille(p) != taille_p_ar:  
        # on peut encore réduire
        parcours += 1
        print(f'parcours : {parcours}')
        jouer(p)
        

if __name__ == "__main__":
    une_pile = creer_pile_vide()
    # poussette = (6, 9, 8, 3, 4, 5, 7)
    # poussette = (2, 4, 7, 8, 9, 4)
    # poussette = (1, 2, 4, 5, 4, 5)
    poussette = (0, 2, 9, 4, 5, 4)
    # poussette = (1, 6, 7, 8, 4, 3)
    
    for value in poussette:
        empiler(une_pile, value)
    jouer(une_pile)
    
    
