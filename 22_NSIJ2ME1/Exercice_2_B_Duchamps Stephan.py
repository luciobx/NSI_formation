# Duchamps Stephan <Stephan-Fa.Duchamps@ac-bordeaux.fr>

# Forme impérative

# NSI Exercice 2 J2
print(" Exercice 2 du sujet 23")

def creer_pile_vide() :
    return []

def est_vide(p):
    """Renvoie le booléen True si la pile est vide, False sinon."""
    return p==[]

def empiler(p, element):
    """Place l'élément v au sommet de la pile"""
    p.append(element)

def depiler(p):
    """
    Retire et renvoie l’élément placé au sommet de la pile,
    si la pile n’est pas vide.
    """
    if not est_vide(p):
        return p.pop()
    else:
        return None

def sommet(p):
    """
    Renvoie l’élément placé au sommet de la pile,
    si la pile n’est pas vide.
    """
    if not est_vide(p):
        return p[-1]
    else:
        return None

def taille(p):
    """
    Renvoie la taille de la pile,
    """
    return len(p)

def reduire_triplet_au_sommet(p):
    a = depiler(p)
    b = depiler(p)
    c = sommet(p)
    if a % 2 != c%2 :
        empiler(p, b)
    empiler(p, a)


def parcourir_pile_en_reduisant(p):
    q = creer_pile_vide()
    p=list(p) # pour dissocier de l'adresse memoire de p
    while taille(p) >= 3 :
        reduire_triplet_au_sommet(p)
        e = depiler(p)
        empiler(q, e)
    while not est_vide(q):
        e = depiler(q)
        empiler(p, e)
    return p

def jouer(p):
    q = parcourir_pile_en_reduisant(p)
    if q==p :
        return q
    else:
        return jouer(q)

def affichage(p):
    """ affichage de la pile avec 3 chiffres au plus"""
    print()
    for i in range(len(p)-1,-1,-1):
        print("|" + " "*(3-len(str(p[i]) ))+str(p[i])+"|")
    print("+---+")



print("Pile de l'exemple")
p_exemple=creer_pile_vide()
print(p_exemple)
empiler(p_exemple,6)
empiler(p_exemple,9)
empiler(p_exemple,8)
empiler(p_exemple,3)
empiler(p_exemple,4)
empiler(p_exemple,5)
empiler(p_exemple,7)
affichage(p_exemple)
p_exemple=jouer(p_exemple)
affichage(p_exemple)


print("Pile de l'exemple 1a")
p_1A=creer_pile_vide()
empiler(p_1A,2)
empiler(p_1A,4)
empiler(p_1A,7)
empiler(p_1A,8)
empiler(p_1A,9)
empiler(p_1A,4)
affichage(p_1A)
p_1A=jouer(p_1A)
affichage(p_1A)

print("Pile A de l'exemple 1b")
p_A=creer_pile_vide()
empiler(p_A,1)
empiler(p_A,2)
empiler(p_A,4)
empiler(p_A,5)
empiler(p_A,4)
empiler(p_A,5)
affichage(p_A)
p_A=jouer(p_A)
affichage(p_A)

print("Pile B de l'exemple 1b")
p_B=creer_pile_vide()
empiler(p_B,0)
empiler(p_B,2)
empiler(p_B,9)
empiler(p_B,4)
empiler(p_B,5)
empiler(p_B,4)
affichage(p_B)
p_B=jouer(p_B)
affichage(p_B)

print("Pile C de l'exemple 1b")
p_C=creer_pile_vide()
empiler(p_C,1)
empiler(p_C,6)
empiler(p_C,7)
empiler(p_C,8)
empiler(p_C,4)
empiler(p_C,3)
affichage(p_C)
p_C=jouer(p_C)
affichage(p_C)