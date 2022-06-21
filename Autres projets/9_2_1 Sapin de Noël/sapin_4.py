# Author(s) name (Individual or corporation)
# Luc VINCENT for Lycee des GRAVES
# Date : 07/10/2021
# Title of program/source code
# sapin_4
# Code version
# V4.2
# Type (e.g. computer program, source code)
# source code
# Web address or publisher (e.g. program publisher, URL)
# luc.vincent@ac-bordeaux.fr

# import d'une fonction de hasard
from random import random

# afficher le sommet du sapin
print('       *')
print('       ^')

# affichage du feuillage
for i in range(7, 0, -1): # affichage des lignes
    for j in range(i-1): #  affichage de l'espace gauche
        print(' ', end='')
    print('/', end='') # affichage de la limite gauche /
    #affichage des feuilles selon le type ou du boule
    for j in range(15-2*i):
        # boule ou feuille ?
        boule = random()
        if boule < 0.2:
            print('o', end='') # boule pour 20% de chaque feuille
        elif j%2 == 0:
            print('"', end='') # feuille "
        else:
            print("'", end='') # feuille '
    # affichage de la limite droite
    print('\\')

# affichage du tronc
for i in range(0,3,1):
    for i in range(6):
        print(' ', end='')
    print("|||", end='')
    print()
    
