"""
Nom : ...
Prénom : ...

Création : 17/11/2021
Modification : 17/11/2021
Licence : GPLv3

----------------------------------------------------
Projet : simuler une course de sauts de puces

Fichier principal
- créer les puces
- créer la grille des déplacements
- gérer les événements
- déplacer les puces
- afficher la grille
- afficher le message de fin lors de l'arrivée des puces

----------------------------------------------------
Version 2 : avec le module graphique PySimpleGUI
"""
 
 
 
# -------- Les modules Python --------
 
#import PySimpleGUIWeb as sg # Pour lancer l'application dans un serveur Web
import PySimpleGUI as sg
#sg.theme_previewer()
from pprint import pprint

# -------- Les modules personnels --------
from course_puces import *



# -------- Programme principal --------

# Créer le tableau des puces
puces = creer_puces(5)   # 5 puces participent à la course
pprint(puces) # Pour déboguer

# Créer la grille de course
grille = creer_grille(10, puces) # (longueur grilles, tableau des puces)
pprint(grille) # Pour déboguer


# Taille du tableau puces
H = len(grille)       # hauteur = nombre de lignes
L = len(grille[0])    # largeur = nombre de colonnes

# Créer la grille de course
grille_GUI = []
for i in range(H):
    ligne = []
    for j in range(L):
        if j == 0:
            ligne.append(sg.Button(str(i+1), size=(4, 2), key=(i,j), pad=(0,0)))
        else:
            ligne.append(sg.Button(' ', size=(4, 2), key=(i,j), pad=(0,0)))
    grille_GUI.append(ligne)
        

structure =  [grille_GUI,
              [sg.Text('Course non terminée',size=(80, H), key='sortie')],
              [sg.Submit("Envoyer"), sg.Cancel("Quitter")]]


sg.theme('BlueMono')
window = sg.Window('Course de sauts de puces', structure)




while True:
    # ---- Événements et valeurs envoyées par l'interface graphique ----
    event, values = window.read()
    #print(event, values) # pour déboguer
        
    # ---- Vérifier s'il faut fermer l'interface graphique ----
    if event in (sg.WIN_CLOSED, 'Quitter'):
        break
    
    
    # ---- Répéter tant que les puces ne sont pas arrvées ----
    if event == "Envoyer" and puces_arrivees(grille, puces) == False :
        
        # ---- Déplacer les puces ----
        grille, puces = deplacer_puces(grille, puces)
        
        # ---- Afficher la grille ----
        # Afficher dans la console
        afficher_grille_puces(grille) # Facultatif
        
        # Afficher dans l'interface graphique
        for i in range(H):
            for j in range(L):
                if grille[i][j] == 0:
                    structure[0][i][j].update(' ')
                else:
                    structure[0][i][j].update(str(grille[i][j]))
        
        # ---- Vérifier qu'au moins une puce est arrivée ----
        # Pour chaque puce arrivée, afficher "arrivée"
        if puces_arrivees(grille, puces) == True :
            
            # -- Afficher dans la console
            afficher_puces_arrivees(puces) # Facultatif
            
            # -- Afficher dans l'interface graphique
            texte = afficher_puces_arrivees_GUI(puces)
            # print(texte) # pour déboguer
            window['sortie'].update(texte)

        
window.close()
