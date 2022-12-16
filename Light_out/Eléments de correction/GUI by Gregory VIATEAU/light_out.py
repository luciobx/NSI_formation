import sys, tkinter as tk
#from tkinter.messagebox import showinfo
from collections import deque
sys.setrecursionlimit(10000)

class Grille:
    """
    Grille du jeu Light Out utilisée par les classes Jeu_txt, Jeu_gfx et Solveur.
    """
    def __init__(self, longueur, hauteur):
        assert 4 <= longueur * hauteur <= 64, "La grille doit avoir entre 4 et 64 cases."
        self.l = longueur
        self.h = hauteur
        self.grille = [[0]*(longueur+1) for i in range(hauteur+1)]  # ligne 0 et colonne 0 laissées vierges pour éviter les décalages
    
    def __repr__(self):
        return "\n".join(
                        " ".join(str(self.grille[i][j]) for j in range(1, self.l+1))
                        for i in range(1, self.h+1)
                        )
    
    def bascule(self, lgn, col):
        self.grille[lgn][col] = 1 - self.grille[lgn][col]
        if lgn > 1: self.grille[lgn-1][col] = 1 - self.grille[lgn-1][col]
        if lgn < self.h: self.grille[lgn+1][col] = 1 - self.grille[lgn+1][col]
        if col > 1: self.grille[lgn][col-1] = 1 - self.grille[lgn][col-1]
        if col < self.l: self.grille[lgn][col+1] = 1 - self.grille[lgn][col+1]
    
    def a_gagne(self):
        for i in range(1, self.h+1):
            for j in range(1, self.l+1):
                if self.grille[i][j] == 0:
                    return False
        return True
        
    def exporter(self):
        "sauvegarde de la grille, utilisée uniquement par le solveur"
        return [[self.grille[i][j] for j in range(1, self.l+1)] for i in range(1, self.h+1)]
    
    def importer(self, grille):
        "recharge la grille, utilisée uniquement par le solveur"
        for i in range(self.h):
            for j in range(self.l):
                self.grille[i+1][j+1] = grille[i][j]
        

class Jeu_txt:
    """
    Jeu en version console
    Se lance avec Jeu_txt(nb_lgn, nb_col)
    Exemple : Jeu_txt(8, 6)
    La taille de la grille doit être entre 4 et 64 cases.
    """
    def __init__(self, longueur, hauteur):
        self.grille = Grille(longueur, hauteur)
        self.l = longueur
        self.h = hauteur
        self.jeu()
                
    def jeu(self):
        for tour in range(1, 101):
            print(f"Tour n°{tour}")
            self.grille.bascule(*self.saisie())
            print()
            if self.grille.a_gagne():
                print(self.grille)
                print(f"Vous avez gagné en {tour} tours.")
                return
        print(self.grille)
        print("Vous avez perdu.")
    
    def saisie(self):
        print()
        print(self.grille)
        lgn = col = 0
        try:
            choix = input("Entrer votre choix au format ligne colonne : ").split(" ")
            if len(choix) != 2:
                raise Exception
            lgn = int(choix[0])
            col = int(choix[1])
            if lgn < 1 or lgn > self.h:
                print(f"Le numéro de ligne doit être entre 1 et {self.h}.")
                return self.saisie()
            if col < 1 or col > self.l:
                print(f"Le numéro de colonne doit être entre 1 et {self.l}.")
                return self.saisie()
            return lgn, col
        except:
            print("Entrer deux nombres séparées par un espace.")
            print("Exemple : 3 4 pour choisir la ligne 3 et la colonne 4")
            return self.saisie()

class Grille_tk(tk.Canvas):
    def __init__(self, root, longueur, hauteur, taille_carre, message):
        largeur_canvas = longueur*taille_carre
        hauteur_canvas = hauteur*taille_carre
        super().__init__(root, width=largeur_canvas, height=hauteur_canvas, background='#202020')
        self.root = root
        self.l = longueur
        self.h = hauteur
        self.tour = 1
        self.taille_carre = taille_carre
        self.message = message
        self.grille = Grille(longueur, hauteur)
        self.trace()
        self.pack()
        self.bind("<Button-1>", self.clic)
         
    def trace(self):
        taille = self.taille_carre
        for i in range(self.h):
            for j in range(self.l):
                if self.grille.grille[i+1][j+1] == 1:
                    couleur = '#FFFF50'
                else:
                    couleur = '#505050'
                self.create_rectangle(j*taille, i*taille, (j+1)*taille, (i+1)*taille, fill=couleur)
            
    def clic(self, event):
        col, lgn = event.x//self.taille_carre+1, event.y//self.taille_carre+1
        if col > self.l:
            col = self.l - 1
        if lgn > self.h:
            lgn = self.h - 1
        self.bascule(lgn, col)
        if self.grille.a_gagne():
            self.message.set(f"Gagné en {self.tour} tours !")
            self.unbind("<Button-1>")
            return
        self.tour += 1
        self.message.set(f"Tour n°{self.tour} : cliquer sur une case.\n")
                            
    def bascule(self, lgn, col):
        self.grille.bascule(lgn, col)
        self.trace() 

class Jeu_gfx(tk.Tk):
    """
    Jeu en version graphique
    Se lance avec Jeu_gfx(nb_lgn, nb_col)
    Exemple : Jeu_gfx(8, 6)
    La taille de la grille doit être entre 4 et 64 cases.
    """
    def __init__(self, longueur, hauteur):
        super().__init__()
        self.l = longueur
        self.h = hauteur
        tk.Label(self, text="Light Out", font=("Lucida Console", 20)).pack()   
        taille_carre = self.calcule_taille_carre()
        message = tk.StringVar(value=f"Tour n°1 : cliquer sur une case.\n")
        self.Grille_tk = Grille_tk(self, longueur, hauteur, taille_carre, message)
        tk.Label(self, textvariable=message, font=("Lucida Console", 16)).pack()
        self.mainloop()

    def calcule_taille_carre(self):
        largeur_ecran = self.winfo_screenwidth()
        hauteur_ecran = self.winfo_screenheight()
        taille_carre = min(int(hauteur_ecran*0.5/self.h), 
                          int(largeur_ecran*0.5/self.l)) 
        return taille_carre     
    
class Solveur:
    """
    Solveur bourrin, effectue un parcours en largeur du graphe des coups.
    Une file du type deque est utilisée pour le parcours en profondeur.
    Toutes les positions sont enregistrées dans un dictionnaire afin de ne
    pas réexplorer deux fois la même position. Le dictionnaire permet aussi
    de remonter la solution.
    La fonction Solveur.grille_vdico transforme le plateau muable en tuple
    pour qu'il puisse servir de clé dans le dictionnaire.
    Fonctionne sur mon PC jusqu'à (4,4) ou (5,3), MemoryError si plus gros.
    Se lance avec Solveur(nb_lgn, nb_col)
    Exemple : Solveur(4, 3)
    À améliorer : Le stockage des plateaux sous forme de listes 2D ou de tuples
    2D consomment trop de mémoire. Il faudrait réfléchir à une autre structure
    de données moins gourmande pour avoir un solveur plus efficace.
    """
    def __init__(self, longueur, hauteur):
        self.grille = Grille(longueur, hauteur)
        self.l = longueur
        self.h = hauteur
        self.dico = {Solveur.grille_vdico(self.grille.grille): None}
        self.file = deque([])  
        self.parcours()
    
    def grille_vdico(grille):
        return tuple(tuple(grille[i][j] for j in range(1,len(grille[0]))) for i in range(1,len(grille)))
    
    def parcours(self):
        "parcours en largeur de l'arbre des coups possibles"
        for i in range(1, self.h+1):
            for j in range(1, self.l+1):
                grille_prec = Solveur.grille_vdico(self.grille.grille)
                self.grille.bascule(i, j)
                grille_dico = Solveur.grille_vdico(self.grille.grille)
                if grille_dico not in self.dico:
                    self.file.append(self.grille.exporter())
                    self.dico[grille_dico] = grille_prec
                    if self.grille.a_gagne():
                        sol = self.solution(grille_dico)
                        print(f"Gagné en {len(self.sol) -1} coups !")
                        for g in sol:
                            for l in g:
                                print(l)
                            print()
                        sys.exit()        # met fin aux appels récursifs
                self.grille.bascule(i, j) # remet la grille dans l'état précédent
        self.grille.importer(self.file.popleft())
        self.parcours()      

    def solution(self, grille):
        "reconstruit la solution à partir du dictionnaire"
        res = [grille]
        while grille != None:
            grille = self.dico[grille]
            res.append(grille)
        return list(reversed(res))[1:]
        
        

j = Jeu_gfx(4, 3)   
