# By Luc VINCENT 
# 2022.05.25
# 22-NSIJ2ME1 Exercice 5
# la programmation objet et la méthode diviser pour régner
# Générateur de labyrinthe
# 1.0
# luc.vincent@ac-bordeaux.fr
# sys.version '3.7.9 (tags/v3.7.9:13c94747c7, Aug 17 2020, 18:01:55) [MSC v.1900 32 bit (Intel)]'

from cell import Cellule
import random

class Labyrinthe:
    '''Definir un labyrinthe'''
    
    def __init__(self, hauteur, longueur):
        '''Constructeur
        
        grille: list un tableau à deux dimensions hauteur et longueur
        contenant des cellules possédant chacune ses quatre murs.
        >>> LIGNE = 2
        >>> COLONNE = 3
        >>> un_lab = Labyrinthe(LIGNE, COLONNE)
        '''
        self.grille = self.construire_grille(hauteur, longueur)
        
    def construire_grille(self, hauteur, longueur):
        '''Construire une grille
        
        Renvoyer un tableau à deux dimensions hauteur et longueur
        contenant des cellules possédant chacune ses quatre murs.
        '''
        grille = []
        # Pour chaque ligne
        for i in range(hauteur):
            ligne = []
            # Pour chaque colonne
            for j in range(longueur):
                # cellule à 4 murs
                cellule = Cellule(True, True, True, True)
                ligne.append(cellule)
            grille.append(ligne)
        return grille
    
    def __str__(self):
        '''Afficher une grille dans la console'''
        motif ='*'
        forme_grille = ""
               
        # Former la grille
        for ligne in self.grille:
            # Former le mur Nord
            for cellule in ligne: 
                if cellule.murs['N']:
                    forme_grille += motif * 3
                else:
                    forme_grille += motif + "  "
            # dernier cas
            forme_grille += "*\n"
            
            # Former mur intermediaire    
            for cellule in ligne: 
                if cellule.murs['O']:
                    forme_grille += motif + "  "
                else:
                    forme_grille += "   "
            # dernier cas
            if cellule.murs['E']:
                forme_grille += motif + "\n"
            else:
                forme_grille += "  "+ "\n"
                 
        
        # Former le mur Sud
        for cellule in self.grille[-1]: 
            if cellule.murs['S']:
                forme_grille += motif * 3
            else:
                forme_grille += motif + "  "     
        forme_grille += motif + "\n" 
        return forme_grille
    
    def __repr__(self):
        '''Afficher une grille
        
        >>> LIGNE = 2
        >>> COLONNE = 3
        >>> un_lab = Labyrinthe(LIGNE, COLONNE)    
        >>> un_lab # doctest: +NORMALIZE_WHITESPACE
        True True True True True True True True True True True True 
        True True True True True True True True True True True True 
        <BLANKLINE>    
        '''
        # aide https://docs.python.org/3/library/doctest.html
        nature_cellule = ''
        for ligne in self.grille:
            for cellule in ligne:
                nature_cellule += f"{cellule.murs['N']} {cellule.murs['E']} {cellule.murs['S']} {cellule.murs['O']}"
                nature_cellule += '\t'
            nature_cellule += '\n'
        return nature_cellule
        
    def creer_passage(self, c1_lig, c1_col, c2_lig, c2_col):
        '''Supprimer des murs entre deux cellules ayant un côté commun afin de créer un passage
        
        les coordonnées c1_lig, c1_col d'une cellule notée cellule1 et les coordonnées
        c2_lig, c2_col d'une cellule notée cellule2
        crée un passage entre cellule1 et cellule2.
        >>> LIGNE = 4
        >>> COLONNE = 5
        >>> un_lab = Labyrinthe(LIGNE, COLONNE)
        >>> un_lab.creer_passage(0, 1, 0, 0)
        >>> print(un_lab)
        ****************
        *     *  *  *  *
        ****************
        *  *  *  *  *  *
        ****************
        *  *  *  *  *  *
        ****************
        *  *  *  *  *  *
        ****************
        <BLANKLINE>
        >>> un_lab.creer_passage(2, 1, 1, 1)
        >>> print(un_lab)
        ****************
        *     *  *  *  *
        ****************
        *  *  *  *  *  *
        ****  **********
        *  *  *  *  *  *
        ****************
        *  *  *  *  *  *
        ****************
        <BLANKLINE>
        '''
        
        cellule1 = self.grille[c1_lig][c1_col]
        cellule2 = self.grille[c2_lig][c2_col]
        # cellule2 au Nord de cellule1
        if c1_lig - c2_lig == 1 and c1_col == c2_col:
            cellule1.murs['N'] = False
            cellule2.murs['S'] = False
        # cellule2 à l’Ouest de cellule1
        elif c1_lig == c2_lig and c1_col - c2_col == 1:
            cellule1.murs['O'] = False
            cellule2.murs['E'] = False
        

    def creer_labyrinthe(self, ligne, colonne, haut, long):
        '''Créer un labyrinthe à partir d'une grille
        
        Crée un labyrinthe de hauteur haut et de longueur long
        dont la cellule en haut à gauche est de coordonnées (ligne, colonne).
        >>> LIGNE = 3
        >>> COLONNE = 5
        >>> un_lab = Labyrinthe(LIGNE, COLONNE)
        >>> un_lab.creer_labyrinthe(0, 0, LIGNE, COLONNE)
        >>> print(un_lab)
        ****************
        *              *
        *  ****  *  ****
        *     *  *     *
        *  *******  ****
        *        *     *
        ****************
        <BLANKLINE>
        >>> LIGNE = 5
        >>> COLONNE = 3
        >>> un_lab = Labyrinthe(LIGNE, COLONNE)
        >>> un_lab.creer_labyrinthe(0, 0, LIGNE, COLONNE)
        >>> print(un_lab)
        **********
        *        *
        *  ****  *
        *     *  *
        *  *******
        *        *
        *  *******
        *        *
        *  ****  *
        *     *  *
        **********
        <BLANKLINE>
        '''
        # print(self) # voir les étapes
        # Cas de base
        if haut == 1 :
            # Créer tous les passages H de la ligne 
            for k in range(colonne, colonne+long-1):
                self.creer_passage(ligne, k+1, ligne, k)
        # Cas de base
        elif long == 1:
            # Créer tous les passages V de la  colonne 
            for k in range(ligne,ligne+haut-1):
                self.creer_passage(k+1, colonne, k, colonne)
        # Appels récursifs
        else:
            # Version 2
            # gérer la paritée de la dimension
            
            if haut >= long :
                # on coupe horizontalement la grille en deux sous labyrinthes
                # L'ouverture du passage V entre les deux sous-labyrinthes se fait le plus à l'Ouest
                if haut % 2 == 0:
                    self.creer_passage(ligne+haut//2, colonne, ligne+haut//2-1, colonne)
                    # labyrinthe haut
                    self.creer_labyrinthe(ligne, colonne, haut//2, long)
                    # labyrinthe bas
                    self.creer_labyrinthe(ligne+haut//2, colonne, haut//2, long)
                else:
                    self.creer_passage(ligne+haut//2+1, colonne, ligne+haut//2, colonne)
                    # labyrinthe haut
                    self.creer_labyrinthe(ligne, colonne, haut//2+1, long)
                    # labyrinthe bas
                    self.creer_labyrinthe(ligne+haut//2+1, colonne, haut//2, long)

            else:
                # on coupe verticalement la grille en deux sous-labyrinthes
                # L'ouverture du passage H entre les deux sous-labyrinthes se fait le plus au Nord
                if long % 2 == 0:         
                    self.creer_passage(ligne, colonne+long//2, ligne, colonne+long//2-1)
                    # labyrinthe gauche
                    self.creer_labyrinthe(ligne, colonne, haut, long//2)
                    # labyrinthe droit
                    self.creer_labyrinthe(ligne, colonne+long//2, haut, long//2)
                else:
                    self.creer_passage(ligne, colonne+long//2+1, ligne, colonne+long//2)
                    # labyrinthe gauche
                    self.creer_labyrinthe(ligne, colonne, haut, long//2+1)
                    # labyrinthe droit
                    self.creer_labyrinthe(ligne, colonne+long//2+1, haut, long//2)
    
    def ouvrir_mur(self, cel_lig, cel_col,haut, long):
        '''Ouvrir un mur exterieur
        
        Ouvre un mur sur la cellulle désignée
        première colonne ouvrir ouest
        dernière colonne ouvrir est
        1 ere ligne ouvrir au nord
        derniere ligne ouvrir au sud
        >>> LIGNE = 4
        >>> COLONNE = 4
        >>> un_lab = Labyrinthe(LIGNE, COLONNE)
        >>> un_lab.creer_labyrinthe(0, 0, LIGNE, COLONNE)
        >>> un_lab.ouvrir_mur(3, 2, LIGNE, COLONNE)
        >>> print(un_lab)
        *************
        *           *
        *  ****  ****
        *     *     *
        *  **********
        *           *
        *  ****  ****
        *     *     *
        *******  ****
        <BLANKLINE>
        '''
        cellule = self.grille[cel_lig][cel_col]
        if cel_col == 0:           
            cellule.murs['O'] = False
        elif cel_col == long - 1:
            cellule.murs['E'] = False
        elif cel_lig == 0:      
            cellule.murs['N'] = False
        elif cel_lig == haut - 1:
            cellule.murs['S'] = False
        else:
            raise ValueError("Cellule interne au labyrinthe")
                
                   

        

    def creer_portes(self, haut, long):
        '''Créer deux ouvertures au hasard dans un labyrinthe

        labyrinthe de hauteur haut et de longueur long
        dont la cellule en haut à gauche est de coordonnées (0, 0).
        '''
        # creer une liste des cases ouvrables
        cellules = []
        for y in range(haut):
            if y == 0 or y == haut - 1:
                # premier ou derniere ligne
                for x in range(long):
                    cellules.append((y, x))
            else:
                # lignes intermédaires
                cellules.append((y, 0))
                cellules.append((y, haut - 1))
        for i in range(2):
            # Choisir cellule
            ouvre = random.choice(cellules)
            # la retirer de la liste des possibles
            cellules.remove(ouvre)
            self.ouvrir_mur(ouvre[0], ouvre[1], haut, long)

        


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=False)
    LIGNE = 4
    COLONNE = 5
    un_lab = Labyrinthe(LIGNE, COLONNE)
    un_lab.creer_labyrinthe(0, 0, LIGNE, COLONNE)
    un_lab.creer_portes(LIGNE, COLONNE)
    print(un_lab)
