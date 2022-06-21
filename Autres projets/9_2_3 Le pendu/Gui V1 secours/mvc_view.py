# Realisation d'une interface GUI
# By Luc VINCENT 
# 2021.11.23
# module mvc_view
# 1.0
# luc.vincent@ac-bordeaux.fr
# sys.version '3.7.9 (tags/v3.7.9:13c94747c7, Aug 17 2020, 18:01:55) [MSC v.1900 32 bit (Intel)]'
# tkinter.TkVersion 8.6

import frames as f
#import draw as d
import display as di
import command as c
import alphabet as a

import string # pour disposer de string.ascii_uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


class View():
    '''
    Partie visible de interface graphique
    '''
    def __init__(self, master):
        self.frames_list = f.create_frame(master)
        self.pannel = di.add_text(self.frames_list[2], "pannel")
        self.word_button = c.add_change(self.frames_list[4])
        self.v_keyboard = Virtual_keyboard(self.frames_list)
        self.advice = di.add_text(self.frames_list[3], "advice")
        
class Virtual_keyboard():
    '''
    Le clavier virtuel
    '''
    def __init__(self, frames_list):
        self.alphabet = a.add_image(frames_list[0])    
     
    def clic(self, event):
        '''
        Gestion de l'événement clic gauche sur la zone graphique du clavier virtuel
        Renvoie le caractère cliqué
        
        '''
        # position du pointeur de la souris
        abs_x = event.x
        ord_y = event.y
        #print(abs_x, ord_y)
        return self.convert(abs_x, ord_y, 40)
        
    def convert(self, clic_x, clic_y, taille):
        '''
        Calcule et renvoie la lettre cliquée selon la position du clic
        clic_x, clic_y postion du clic en pixel
        taille de image lettre
        '''
        # offset_x = taille // 2
        offset_y = taille //4
        # on détermine index_y 0 ou 13 ou 26 lettre de l'alaphabet
        if clic_y > offset_y and clic_y <= (offset_y + taille):
            index_y = 0
        elif clic_y > (2 * offset_y + taille) and clic_y < (2 * offset_y + 2 * taille):
            index_y = 13
        else:
            index_y = 26
        # On détermine index_x -1 0 à 13 ou 26 
        index_x = (clic_x - 20) // (taille + 5) # pour l'indice de la lettre
        j = (clic_x - 20) % (taille + 5) # pour les espaces entre lettres
        # Si on clique sur une lettre
        if j > 0 and j < 40:
            if index_x == -1:
                index_x = 26
            elif index_y == 0 and index_x == 13:
                index_x = 26
            elif (index_x+index_y) < 25:
                return (string.ascii_uppercase[index_x+index_y])
        
        
        