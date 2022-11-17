"""
Nom : ...
Prénom : ...

Création : 17/11/2021
Modification : 17/11/2021
Licence : GPLv3

----------------------------------------------------
Projet : simuler une course de sauts de puces

Module  : course_puce
- Créer les puces
- Créer la grille
- Afficher la grille
- Simulation d'une course

----------------------------------------------------
Version 1 : pour la varte microbit
"""


# -------- Les bibliothèques --------
#from pprint import pprint
import random
from microbit import *
from time import sleep



# -------- Les fonctions --------
def creer_puces(np:int) -> list:
    """
    Générer un tableau de np puces
    Chaque puce est représentée par un dictionnaire
    
    Caractéristiques d'une puce
      - nom
      - pos : position de la puce
        - initialisée à 0
        - en suite, saut aléatoire de valeur comprise entre 1 et 3
      - couleur (choix aléatoire dans le tableau couleurs)
      - taille : pour éventuellement représenter une puce en fonction de sa taille
        - valeur aléatoire comprise entre 1 et 4 
      
    Param :
      np (int) :  nombre de puces
    Renvoi :
      puces (list) :  tableau de dictionnaires, un dictionnaire par puce
    """    
    assert type(np) == int # np doit être un entier naturel non nul
    assert 1 <= np <= 20   # np est en dehors des bornes
    
    # Création du tableau des puces (un tableau de dictopnnaires)
    couleurs = ['red', 'bleu', 'green', 'yellow', 'white']
    puces = [{'nom' : 'puce' + str(i), 'pos' : 0, 'couleur': random.choice(couleurs), 'taille' : random.randint(1, 4)} for i in range(1, np + 1)]
    return puces


def creer_grille(n:int, puces:list) -> list:
    """
    Créer la grille sur laquelle sont placées les puces
    Param :
        n (int) : longueur du parcours de la course
        puces (list) : tableau de dictionnaires, un dictionnaire par puce
    Renvoi :
      grille (list) : tableau 2 dimensions,
        - longueur correspond à la longueur du parcours ;
        - hauteur correspond au nombre de puces
    """
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


def afficher_grille_puces(grille:list):
    """
    Afficher dans la console, la grille avec les puces
    Param :
      grille (list) : tableau 2 dimensions
    Sortie :
      Affichage de la grille dans la console
    """
    assert type(grille) == list # la grille doit être un tableau à deux dimensions
    
    
    H = len(grille)      # hauteur de la grille = nombre de lignes
    L = len(grille[0])   # largeur de la grille = nombre de colonnes
    grille_txt = '-'*4*L+'\n'
    for i in range(H):
        ligne = '|'
        for j in range(L):
            if grille[i][j] == 0:
                ligne += " "*3 + '|'
            else:
                ligne +=f"{grille[i][j]:^3}|"
        grille_txt += ligne + '\n'
        grille_txt += '-'*4*L+'\n'
    print(grille_txt)
 
 
 
def deplacer_puces(grille:list, puces:list) -> tuple:
    """
    Déplacer les puces aléatoirement.
    Chaque déplacement est une valeur aléatoire comprise entre 1 et 3
    Param
      grille (list) : tableau 2 dimensions
      puces (list) : tableau de dictionnaires, un dictionnaire par puce
    Renvoi :
      grille, puces (tuples) : les tableaux grille et puces
    """
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
    """
    Vérifier qu'une ou plusieurs puces sont arrivées
    Param :
      puces (list) : tableau de dictionnaires, un dictionnaire par puce
    Renvoi :
      True/False (bool) : True si au moins une puce est arrivée, False sinon
    """
    assert type(puces) == list # puces doit être un tableau
    assert len(puces) > 0 # il faut au moins une puce dans le tableau
    
    for puce in puces:
        if puce['pos'] >= len(grille[0]) - 3: # Exemple 10 + 3 = 13 = largeur de la grille = len(grille[0])
            return True                       # cases de 0 à 12
                                              # arrivée si en cases 10, 11 ou 12 soit pos >= 10
    return False   # Aucune puce arrivée
        
    



def afficher_puces_arrivees(puces:list):
    """
    Lorsque au moins une puce est arrivée :
      - Afficher les puces arrivées
      - Afficher les puces non arrivées
    Param :
      puces (list) : tableau des puces
    Renvoi :
      Pas de renvoi
    """

    for puce in puces:
        if puce['pos'] >= 6:
            print(f"{puce['nom']} est en position {puce['pos']} : arrivée, donc c'est gagné")
        else:
            print(f"{puce['nom']} est en position {puce['pos']} : non arrivée")
    


def simuler_course(grille:list, puces:list) :
    """
    Simuler une course de puces
    Param :
      grille (list) : grille du jeu
      puces (list) : tableau de dictionnaires, un dictionnaire par puce
    Renvoi:
      Rien
    """
    
    # Répéter tant que les puces ne sont pas arrvées 
    while puces_arrivees(grille, puces) == False:
        afficher_grille_puces(grille)
        attendre_action_utilisateur()
        grille, puces = deplacer_puces(grille, puces)
    afficher_grille_puces(grille)
         
    # Pour chaque puce arrivée, afficher "arrivée"
    afficher_puces_arrivees(puces)            




# -------- Focntion pour la carte Micro:bit --------
#--------------------------------------------------------------
def afficher_grille_puces_microbit(grille:list):
    """
    Afficher dans la console, la grille avec les puces
    Param :
      grille (list) : tableau 2 dimensions
    Sortie :
      Affichage de la grille dans la console
    """
    assert type(grille) == list # la grille doit être un tableau à deux dimensions
    
    
    H = len(grille)      # hauteur de la grille = nombre de lignes
    L = len(grille[0])   # largeur de la grille = nombre de colonnes
    
    
    for i in range(H):
        for j in range(1, 5+1):      # On n'affiche pas les puces en position initiale
            if grille[i][j] != 0:
              display.set_pixel(j-1, i, 5)


def attendre_action_utilisateur_microbit():
    """
    Attendre une action de l'utilisateur sur le clavier
    Param :
      Si touche Q appuyée alors quitter le programme
      Si touche D (ou autre touche) appuyée alors le déplacement des puces se poursuit
    Renvoi :
      Pas de renvoi
    """
    while button_a.is_pressed() == False:
      pass

def afficher_puces_arrivees_microbit(grille:list, puces:list):
  """
  Lorsque au moins une puce est arrivée :
    - Afficher les puces arrivées
    - Afficher les puces non arrivées
  Param :
    puces (list) : tableau des puces
  Renvoi :
    Pas de renvoi
  """
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



def simuler_course(grille:list, puces:list) :
  """
  Simuler une course de puces
  Param :
    grille (list) : grille du jeu
    puces (list) : tableau de dictionnaires, un dictionnaire par puce
  Renvoi:
    Rien
  """
  
  # Répéter tant que les puces ne sont pas arrvées 
  while puces_arrivees(grille, puces) == False:
      afficher_grille_puces(grille)
      #print(puces)
      #print(grille)
      afficher_grille_puces_microbit(grille)
      attendre_action_utilisateur_microbit()
      grille, puces = deplacer_puces(grille, puces)
      sleep(0.5)
  afficher_grille_puces(grille)
  afficher_grille_puces_microbit(grille)
       
  # Pour chaque puce arrivée, afficher "arrivée"
  afficher_puces_arrivees(puces)            
  afficher_puces_arrivees_microbit(grille, puces) 
     





# -------- Programme principal / Test des fonctions --------


# Test : afficher grille
"""
grille =    [[0, 0, 0, 1, 0, 0],
             [0, 0, 0, 0, 2, 0],
             [0, 0, 3, 0, 0, 0],
             [0, 0, 0, 0, 0, 4],
             [0, 0, 0, 5, 0, 0]]

afficher_grille_puces(grille)
afficher_grille_puces_microbit(grille)
print("terminé")
"""



# Test 2 : créer et déplacer 1 fois les puces
"""
puces = creer_puces(3)                          # 1 à 5 puces possibles
grille  = creer_grille(5, puces)                # Grille fixée à 5 car 5 LED en largeur
grille, puces = deplacer_puces(grille, puces)
afficher_grille_puces(grille)
afficher_grille_puces_microbit(grille)
print("terminé")
"""




# Test 3 : simuler une couse
puces = creer_puces(3)                          # 1 à 5 puces possibles
grille  = creer_grille(6, puces)                # Grille fixée à 6
                                                # - case 0 non affichée
                                                # - cases 1 à 5 sur les 5 LED en largeur
                                                # - cases 6, 7 ou 8 d'arrivée, affichées sur un nouvel écran
simuler_course(grille, puces)



