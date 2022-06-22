# By Luc VINCENT 
# 2022.06.08
# Puissance4
# Les constantes
# 1.0
# luc.vincent@ac-bordeaux.fr
# sys.version '3.7.9 (tags/v3.7.9:13c94747c7, Aug 17 2020, 18:01:55) [MSC v.1900 32 bit (Intel)]'
# PySimpleGUI 4.49.0

import PySimpleGUI as sg
from constantes import *
import calculs as c
import fonctions_verif as v


def dessiner_grille(a_graph, color: list):
    '''Dessiner dans le graphe a_graph le jeu de couleur color
    '''
    for ligne in range(N_HAUT):
        for colonne in range(N_LARG):
            dessiner_jeton(a_graph, color, ligne, colonne) 
   

def dessiner_jeton(graphe, color, ligne, couleur):
    ''' Dessiner un jeton dans le graphe le jeton ligne, colonne de couleur color
    '''
    centre = coord_jeton(ligne, couleur)
    coulor_jeton = couleur_jeton(color[ligne][couleur])
    graphe.draw_circle(centre, RAYON, fill_color=coulor_jeton, line_color='green')
    
def coord_jeton(ligne:int, colonne:int)->tuple:
    '''Calculer les coordonnées du centre du jeton
    Args:
    ligne, colonne l'indice de chaque jeton dans la grille de couleur
    Return:
    Un tuple des coordonnées du centre du jeton
    '''
    x = MARGE + (PAS + 2 * RAYON) * colonne
    y = MARGE + (PAS + 2 * RAYON) * ligne
    return (x, y)


def couleur_jeton(jeton: int) -> str:
    if jeton == JAUNE:
        return "#FFFF00"
    elif jeton == ROUGE:
        return "#FF0000"
    else:
        return "white"   
    
def dessiner_platine(color:list):
    col_layout = [sg.Button('Vider', key='-GO-', size=(6, 1))], [sg.Button('Quitter', key='-END-',size=(6, 1))]
    layout = [[sg.Graph(
        canvas_size=(LARGEUR, HAUTEUR),
        graph_bottom_left=(0, HAUTEUR),
        graph_top_right=(LARGEUR, 0),
        key="-GRAPH-",
        change_submits=True,  # mouse click events
        background_color='lightblue'),
               sg.Column(col_layout)],
              [sg.Text(size=20, font =('Arial', 10), justification ='center', key ='-OUTPUT-')]]
    
    
    window = sg.Window("Puissance 4", layout, finalize=True)
    a_graph = window['-GRAPH-']
    dessiner_grille(a_graph, color)
    return window

def effacer_grille(a_graph, color: list):
    '''Effacer la platine
    '''
    a_graph.erase()
    dessiner_grille(a_graph, color)


def choisir_colonne(x) -> int:
    """
    identifie la colonne du clic souris

    Returns:
        int: la colonne choisie ou -1 si hors colonne
    """
    larg_col = PAS + 2 * RAYON
    # in_col = 1 si on clic dans une colonne
    in_col = ((x - MARGE + RAYON) // larg_col) - ((x - MARGE - RAYON) // larg_col)
    if in_col == 1:
        n_col = ((x - MARGE + RAYON) // larg_col)
    else:
        n_col = -1
    return n_col 
        

def jouer(window, grille):
    # initialisation pour première entrée dans le jeu
    ligne, colonne = 0, 0
    joueur = ROUGE
    # il n'y a pas de gagnant et le match n'est pas nul
    score = [False, False]
    # boucle de jeu
    while True:

            
        event, values = window.read()
        # On veut terminer
        if event in (None,"-END-"):
            # On peut sortir par la croix ou le bouton
            break
        
        # On clic pour vider
        if event == "-GO-":
            grille = c.initialiser_grille(N_LARG, N_HAUT)
            effacer_grille(window["-GRAPH-"], grille)
            # on réinitalise le gagnant
            score = [False, False]
            window['-OUTPUT-'].update("")
            
        # On clic pour jouer  
        if not score[0] and event == "-GRAPH-":
            # identifier postion horizontale du clic (x, y)
            x = values["-GRAPH-"][0]
            # print(x)
            # identifier la colonne ou le joueur a joué
            col = choisir_colonne(x)
            # print(col)
            if col != -1 and not c.est_remplie(grille, col):
                # on est dans une colonne
                # le coup est valide
                # On place le jeton
                ligne = c.placer_jeton(grille, col, joueur)
                # print(grille)
                # dessiner le jeton
                dessiner_jeton(window["-GRAPH-"], grille, ligne, col)
                # On regarde si le coup est gagnant
                score[0] = v.verif_gagnant(grille, joueur, ligne, col)
                if not score[0]:
                    # ce n'est pas un coup gagnant
                    if not c.est_pleine(grille):
                        # ce n'est pas le dernier coup
                        # changer de joueur à chaque tour
                        joueur = c.changer_joueur(joueur)
                    else:
                        # match nul
                        score[1] =  True
                    
        # le dernier coup joué est gagnant ou final
        if score[0]:
            # on affiche le résultat
            if joueur == ROUGE:
                message = "ROUGE a gagné !"
            elif joueur == JAUNE:
                message = "JAUNE a gagné !"
            else:
                message = "erreur"
            window['-OUTPUT-'].update(message)
        if score[1]:
            message = " MATCH NUL"
            window['-OUTPUT-'].update(message)          
    
    # On ferme le programme
    window.close()

if __name__ == '__main__':
    a_colors_board = [[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]]
    a_game = dessiner_platine(a_colors_board)
    jouer(a_game, a_colors_board)
    