# By Luc VINCENT 
# 2022.05.25
# cell.py
# la classe cellule
# 1.0
# luc.vincent@ac-bordeaux.fr
# sys.version '3.7.9 (tags/v3.7.9:13c94747c7, Aug 17 2020, 18:01:55) [MSC v.1900 32 bit (Intel)]'

# Une case du labyrinthe
class Cellule:
    '''Definir une cellule
    
    Une cellule est une case du labyrinthe
    
    >>> a_cell = Cellule(True, True, True, True)
    >>> a_cell
    MURS: Nord:True Est:True Sud:True Ouest:True
    >>> print(a_cell)
     __ 
    |__|
    <BLANKLINE>
    '''
    def __init__(self, murNord, murEst, murSud, murOuest):
        '''Constructeur

        murs de type dict dont les clés sont ’N’, ’E’, ’S’ et ’O’
        dont les valeurs sont des booléens (True si le mur est présent et False sinon).
        '''
        self.murs={'N':murNord,'E':murEst, 'S':murSud,'O':murOuest}
        
    def __repr__(self):
        '''Afficher existence des murs d'une cellule'''
        nature_cellule = f"MURS: Nord:{self.murs['N']} Est:{self.murs['E']} Sud:{self.murs['S']} Ouest:{self.murs['O']}"
        return nature_cellule
    
    def __str__(self):
        '''Afficher dessin des murs d'une cellule
         __ 
        |__|
        '''
        forme_cellule = ""
        if self.murs['N']:
            forme_cellule += " __ \n"
        else:
            forme_cellule += "    \n"
        if self.murs['O']:
            forme_cellule += "|"
        else:
            forme_cellule += " "
        if self.murs['S']:
            forme_cellule += "__"
        else:
            forme_cellule += "  "    
        if self.murs['E']:
            forme_cellule += "|\n"
        else:
            forme_cellule += "  \n"      
        return forme_cellule
            

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)

    
    
    