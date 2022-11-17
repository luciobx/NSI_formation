
# -------- Les bibliothèques --------
#from pprint import pprint
import random
from microbit import *
from time import sleep


# -------- Les fonctions --------
def creer_puces(np:int) -> list:   
    assert type(np) == int # np doit être un entier naturel non nul
    assert 1 <= np <= 20   # np est en dehors des bornes
    
    # Création du tableau des puces (un tableau de dictopnnaires)
    couleurs = ['red', 'bleu', 'green', 'yellow', 'white']
    puces = [{'nom' : 'puce' + str(i), 'pos' : 0, 'couleur': random.choice(couleurs), 'taille' : random.randint(1, 4)} for i in range(1, np + 1)]
    return puces


def creer_grille(n:int, puces:list) -> list:
    assert type(n) == int # n doit être un entier 
    assert n >= 3          # n doit être un entier au moins égal à 3
    assert type(puces) == list # puces doit être un tableau
    assert len(puces) > 0 # il doit y avoir au moins une puce
    
    # ---- Créer la grille qui doit contenir la position de chaque puce ----
    # Hauteur de la grille : nombre de puces
    # Largeur de la grille :
    #   - Case 0 : position initiale des puces
    #   - Cases 1 à n : positions pendant la course
    #   - Plus 2 cases, car si en position n-1 :
    #     - +1 : gagné, arrivée sur le case n
    #     - +2 : gagné, arrivée sur le case n + 1
    #     - +3 : gagné, arrivée sur le case n + 2
    grille = [ [0 for j in range(n + 1 + 2) ] for i in range(len(puces))] # 3 cases en plus
    
    # ---- Placer puces en positions initiales
    for i in range(len(puces)):
        grille[i][0] = i + 1 # cases 0 avec le numéro de puce
                             # 1 : numéro de la première puce
    return grille



 
 
 
def deplacer_puces(grille:list, puces:list) -> tuple:
    assert type(grille) == list # la grille doit être un tableau à deux dimensions
    assert type(puces) == list # puces doit être un tableau
    
    
    # Mise à jour position puces dans les tableaux puces et grille
    taille = len(grille[0]) - 3 # largeur de la grille
    grille = [ [0 for i in range(taille + 1 + 2) ] for j in range(len(puces))] # 3 cases en plus pour le dernier saut

    for i in range(len(puces)):
        puce = puces[i]
        puce['pos'] += random.randint(1, 3) # ajouter un déplacement aléatoire entre 1 et 3 cases
        grille[i][puce['pos']] = i + 1  # Inscrire le numéro de puce (i+1) en position   pos
    return grille, puces


def puces_arrivees(grille:list, puces:list) -> bool:
    assert type(puces) == list # puces doit être un tableau
    assert len(puces) > 0 # il faut au moins une puce dans le tableau
    
    for puce in puces:
        if puce['pos'] >= len(grille[0]) - 3: # Exemple 10 + 3 = 13 = largeur de la grille = len(grille[0])
            return True                       # cases de 0 à 12
                                              # arrivée si en cases 10, 11 ou 12 soit pos >= 10
    return False   # Aucune puce arrivée
        
    
# -------- Focntion pour la carte Micro:bit --------
#--------------------------------------------------------------
def afficher_grille_puces_microbit(grille:list):
    assert type(grille) == list # la grille doit être un tableau à deux dimensions
    
    H = len(grille)      # hauteur de la grille = nombre de lignes
    L = len(grille[0])   # largeur de la grille = nombre de colonnes
    
    
    for i in range(H):
        for j in range(1, 5+1):      # On n'affiche pas les puces en position initiale
            if grille[i][j] != 0:
              display.set_pixel(j-1, i, 5)


def attendre_action_utilisateur_microbit():
    while button_a.is_pressed() == False:
      pass

def afficher_puces_arrivees_microbit(grille:list, puces:list):
  display.show(Image.HAPPY)
  sleep(0.5)
  display.clear()
  display.show(Image.HAPPY)
  sleep(0.5)
  display.clear()
  sleep(0.5)
  
  H = len(grille)      # hauteur de la grille = nombre de lignes
  L = len(grille[0])   # largeur de la grille = nombre de colonnes
  for i in range(H):
      for j in range(6, L):      # Les puces sont arrivées en 6, 7 ou 8
          if grille[i][j] != 0:
            display.set_pixel(j-6, i, 9)



def simuler_course_microbit(grille:list, puces:list) :  
  # Répéter tant que les puces ne sont pas arrvées 
  while puces_arrivees(grille, puces) == False:
      #print(puces)
      #print(grille)
      afficher_grille_puces_microbit(grille)
      attendre_action_utilisateur_microbit()
      grille, puces = deplacer_puces(grille, puces)
      sleep(0.5)
  afficher_grille_puces_microbit(grille)
       
  # Pour chaque puce arrivée, afficher "arrivée"
  afficher_puces_arrivees_microbit(grille, puces) 
     


# -------- Programme principal / Test des fonctions --------
puces = creer_puces(3)                          # 1 à 5 puces possibles
grille  = creer_grille(6, puces)                # Grille fixée à 6
                                                # - case 0 non affichée
                                                # - cases 1 à 5 sur les 5 LED en largeur
                                                # - cases 6, 7 ou 8 d'arrivée, affichées sur un nouvel écran
simuler_course_microbit(grille, puces)




