# Realisation d'une interface GUI
# By Luc VINCENT 
# 2021.11.23
# module mvc_controler
# 1.0
# luc.vincent@ac-bordeaux.fr
# sys.version '3.7.9 (tags/v3.7.9:13c94747c7, Aug 17 2020, 18:01:55) [MSC v.1900 32 bit (Intel)]'
# tkinter.TkVersion 8.6

import root as r 
import mvc_model as m
import mvc_view as v

class Controller():
    '''
    Module qui traite les actions de l'utilisateur, modifie les données du modèle et de la vue
    C'est le jeu complet
    '''
    def __init__(self):
        # Creer la fenêtre
        self.root = r.create_main()
        # Creer le model du jeu
        self.model = m.Model()
        # Creer la vue du jeu
        self.view = v.View(self.root)
        # Lier le bouton changer le mot
        self.view.word_button.bind("<Button>", self.change)
        # Lier le clic souris dans l'alpahbet
        self.view.v_keyboard.alphabet.bind('<Button-1>', self.clic)
        # former le mot partiellement trouvé
        self.model.compute()
        # Afficher les informations dans la vue
        self.model.display(self.view, (1, 2))
        self.model.display(self.view, (2, 3))
        print(self.model.the_word)# Affiche solution pour debug
 
    def run(self):
        ''' Ecouteur des evenements'''
        self.root.mainloop()
 
    def clic(self, event):
        ''' Gere le clic souris dans l'alphabet'''
        clicked_char = self.view.v_keyboard.clic(event)
        # On calcule le jeu
        self.model.hanger(self.view, clicked_char)               
 
    def change(self, event):
        ''' Gere le clic sur le bouton'''
        self.model.modify()
        self.model.display(self.view, (1, 2)) # changer pannel
        self.model.display(self.view, (2, 3)) # Changer advice
        # effacer le dessin
        for widget in self.view.frames_list[1].winfo_children():
            widget.destroy()
        print(self.model.the_word) # Affiche solution pour debug
         
if __name__ == '__main__':
    c = Controller()
    c.run()