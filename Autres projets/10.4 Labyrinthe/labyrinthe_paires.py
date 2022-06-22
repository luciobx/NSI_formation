# By Luc VINCENT 
# 2022.05.25
# 22-NSIJ2ME1 Exercice 5
# la programmation objet et la méthode diviser pour régner
# Générateur de labyrinthe
# 1.0
# luc.vincent@ac-bordeaux.fr
# sys.version '3.7.9 (tags/v3.7.9:13c94747c7, Aug 17 2020, 18:01:55) [MSC v.1900 32 bit (Intel)]'

from cell import Cellule

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
            forme_grille += motif + "\n"     
        
        # Former le mur Sud
        for cellule in self.grille[-1]: 
            if cellule.murs['S']:
                forme_grille += motif * 3
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
        '''
        # print(self) voir les étapes
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
            # Version 1 ne traite que les labyrinthes de dimensions multiples de 2
            if haut >= long :
                # on coupe horizontalement la grille en deux sous labyrinthes de même dimension.
                # L'ouverture du passage V entre les deux sous-labyrinthes se fait le plus à l'Ouest
                self.creer_passage(ligne+haut//2, colonne, ligne+haut//2-1, colonne)
                # labyrinthe haut
                self.creer_labyrinthe(ligne, colonne, haut//2, long)
                # labyrinthe bas
                self.creer_labyrinthe(ligne+haut//2, colonne, haut//2, long)
            else:
                # on coupe verticalement la grille en deux sous-labyrinthes de même dimension.
                # L'ouverture du passage H entre les deux sous-labyrinthes se fait le plus au Nord
                self.creer_passage(ligne, colonne+long//2, ligne, colonne+long//2-1)
                # labyrinthe gauche
                self.creer_labyrinthe(ligne, colonne, haut, long//2)
                # labyrinthe droit
                self.creer_labyrinthe(ligne, colonne+long//2, haut, long//2)

        


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=False)
    LIGNE = 2
    COLONNE = 3
    un_lab = Labyrinthe(LIGNE, COLONNE)
    un_lab.creer_labyrinthe(0, 0, LIGNE, COLONNE)
    print(un_lab)
