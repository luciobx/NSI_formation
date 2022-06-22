# By Luc VINCENT 
# 2022.06.08
# Puissance4
# Le programme
# 1.0
# luc.vincent@ac-bordeaux.fr
# sys.version '3.7.9 (tags/v3.7.9:13c94747c7, Aug 17 2020, 18:01:55) [MSC v.1900 32 bit (Intel)]'*

from constantes import *
import calculs  as c
import gui as g

# initialisation
colors_board = c.initialiser_grille(N_LARG, N_HAUT)

# dessiner plateau
a_game = g.dessiner_platine(colors_board)

# On joue le jeu
g.jouer(a_game, colors_board)