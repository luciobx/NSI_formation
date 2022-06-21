# Realisation d'une interface GUI
# By Luc VINCENT 
# 2021.11.23
# module mvc_model
# 1.0
# luc.vincent@ac-bordeaux.fr
# sys.version '3.7.9 (tags/v3.7.9:13c94747c7, Aug 17 2020, 18:01:55) [MSC v.1900 32 bit (Intel)]'
# tkinter.TkVersion 8.6

from vocabulaire import open_json
from mot import valid_word
import string # pour disposer de string.ascii_uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
import draw as d

class Model():
    '''
    Le modèle représente l'univers dans lequel s'inscrit l'application
    '''
    def __init__(self):
        # Définition des attributs du modele
        # nom du fichier de vocabulaire
        self.fichier_json = "words.json"
        # mot du jeu
        self.the_word = self.set_the_word(self.fichier_json)
        # ensemble des lettres valides
        self.word_letters = set(self.the_word)
        # ensemble des lettres de l'alphabet
        self.alphabet = set(string.ascii_uppercase)
        # ensemble des lettres utilisées
        self.used_letters = set()
        # On initialise le ctr de vie 
        self.lives = len(self.the_word)
        # On dispose d'un mot partiellement deviné
        self.partial_word = ''
        
    def set_the_word(self, filename):
        '''
        Renvoie un mot à partir du nom du fichier vocabulaire
        
        '''
        fichier_json = filename
        some_words = open_json(fichier_json)
        the_word = valid_word(some_words).upper()
        return the_word
    
    
    
    def display(self, viewer, number):
        '''
        viewer Le modele de vue utilisé
        number : tuple numero message, numero frame)
        '''
        message_list =["Il vous reste "+ str(self.lives) + " vies et vous avez utilisé les lettres :\n" + ' '.join(self.used_letters),
                       'le mot est : '+ str(self.partial_word),
                       'CLIQUER SUR UN CARACTERE NON UTILISE',
                       'Vous avez déjà utilisé ce caractère, essayer à nouveau',
                       'GAGNE, LE MOT ETAIT BIEN : '+ str(self.the_word),                 
                       'PERDU, LE MOT ETAIT : '+ str(self.the_word)
                       ]            
        if number[1] == 2:
            viewer.pannel.itemconfig('my_text', text= message_list[number[0]])
        elif number[1] == 3:
            viewer.advice.itemconfig('my_text', text= message_list[number[0]])
        else:
            raise ValueError('Frame 2 ou 3')
        
    def compute(self):
        '''
        Former le mot partiellement deviné en vue de l'affichage
        '''
        # calculer le mot partiellement deviné
        self.partial_word = [letter if letter in self.used_letters else '-' for letter in self.the_word]
        # transformer en str
        self.partial_word = ' '.join(self.partial_word)
    
    def modify(self):
        '''
        Choisr le nouveau mot dans le fichier
        '''
        # Choisir le nouveau mot
        self.the_word = self.set_the_word(self.fichier_json)
        # ensemble des lettres valides
        self.word_letters = set(self.the_word)
        # ensemble des lettres de l'alphabet
        self.alphabet = set(string.ascii_uppercase)
        # ensemble des lettres utilisées
        self.used_letters = set()
        # On initialise le ctr de vie 
        self.lives = len(self.the_word)
        # On calcule le mot partiellement deviné
        self.compute()
        
    
    def hanger(self, viewer, a_char):
        '''
        moteur du jeu du pendu
        '''
        if len(self.word_letters) > 0 and self.lives > 0:
            self.compute()
            #affiche('le mot est :', partial_word)
            self.display(viewer, (1, 2)) 
            # attendre le joueur
            self.display(viewer, (2, 3)) # user_letter = question("ENTRER UN CARACTERE : ")
            if a_char in (self.alphabet - self.used_letters):
                # on l'ajoute dans les lettres utilisées
                self.used_letters.add(a_char)
                if a_char in self.word_letters:
                    # elle est dans le mot alors on l'enlève
                    self.word_letters.remove(a_char)
                    self.compute()
                    self.display(viewer, (1, 2))      
                else:
                # elle n'est pas dans le mot
                    self.lives = self.lives - 1
                    # on affiche le message reste de vies
                    self.display(viewer, (0, 3))
                    # On dessine le pendu
                    # On commence par calculer le coût de l'erreur
                    n_morceaux = (len(self.the_word) - self.lives)* 15 //len(self.the_word)
                    d.add_pendu(viewer.frames_list[1], n_morceaux)            
            elif a_char in self.used_letters:
                #la lettre a déjà été trouvée
                self.display(viewer, (3, 3))
            else:
                # On clique en dehors des lettres 
                pass
            if self.lives <= 0 :
                self.display(viewer, (5, 3))
            if len(self.word_letters) == 0:
                self.display(viewer, (4, 3))
                
        
    