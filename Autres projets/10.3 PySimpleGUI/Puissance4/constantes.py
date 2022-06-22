# By Luc VINCENT 
# 2022.06.08
# Puissance4
# Les constantes
# 1.0
# luc.vincent@ac-bordeaux.fr
# sys.version '3.7.9 (tags/v3.7.9:13c94747c7, Aug 17 2020, 18:01:55) [MSC v.1900 32 bit (Intel)]'

N_LARG = 7 # emplacement horizontaux
N_HAUT = 6 # emplacements verticaux
MARGE = 40 # Espace vertical et horizontal du premier CENTRE de dessin des jetons

# Codage des couleurs des jetons
VIDE = 0
ROUGE = 1
JAUNE = 2

# Mise en forme du GUI
# pas entre jetons
PAS = MARGE // 2
# diametre jetons
RAYON = PAS

# taille du plateau
LARGEUR = ((3 * N_LARG) + 1) * PAS
HAUTEUR = ((3 * N_HAUT) + 1) * PAS
