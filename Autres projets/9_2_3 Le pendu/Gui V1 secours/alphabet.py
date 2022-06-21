# Realisation d'une interface GUI
# By Luc VINCENT 
# 2021.11.20
# Programme alphabet
# module de pendu_gui
# 1.0
# luc.vincent@ac-bordeaux.fr
# sys.version '3.7.9 (tags/v3.7.9:13c94747c7, Aug 17 2020, 18:01:55) [MSC v.1900 32 bit (Intel)]'
# tkinter.TkVersion 8.6

# Realiser les imports
import tkinter as tk
from tkinter import NW

import string # pour disposer de string.ascii_uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

class Picture:
    def __init__(self, lettre):
        self.img = tk.PhotoImage(file="lettres\\"+ lettre + '.png')
        
def all_pic(a_canvas, color):
    '''
    Renvoyer un objet canvas dont l'attribut img est la liste de toutes les lettres à affichers
    color : str r ou b pour red ou back
    ''' 
    a_canvas.img =[]
    for letter in string.ascii_uppercase:
        picture = Picture(letter + '_' + color)
        a_canvas.img.append(picture.img)
    return a_canvas
     
def convert(clic_x, clic_y, taille):
    '''
    taille de image lettre
    '''
    #offset_x = taille // 2
    offset_y = taille //2
    if clic_y > offset_y and clic_y <= (offset_y + taille):
        index_y = 0
    elif clic_y > (2 * offset_y + taille) and clic_y < (2 * offset_y + 2 * taille):
        index_y = 13
    else:
        index_y = 26
      
    index_x = (clic_x - 20) // (taille + 5) # pour l'indice de la lettre
    j = (clic_x - 20) % (taille + 5) # pour les espaces entre lettres
    if j > 0 and j < 40:
        if index_x == -1:
            index_x = 26
        
        elif index_y == 0 and index_x == 13:
            index_x = 26
    
        elif (index_x+index_y) < 25:
            print(string.ascii_uppercase[index_x+index_y])
    
    
    
def clic(event):
    """ Gestion de l'événement clic gauche sur la zone graphique """
    # position du pointeur de la souris
    abs_x = event.x
    ord_y = event.y
    # print(abs_x, ord_y)
    convert(abs_x, ord_y, 40)

def add_button(a_canvas):
#     # Création d'un widget Canvas (zone graphique)
#     alphabet_dessin = tk.Canvas(frame, bg = 'white')
#     alphabet_dessin.pack(padx = 5, pady = 5)
    # La méthode bind() permet de lier un événement avec une fonction :
    # un clic gauche sur la surface provoquera l'appel de la fonction clic()
    a_canvas.bind('<Button-1>', clic)






def add_image(frame):
    '''
    Ajouter toutes les lettres de l'alphabet dans le frame passé en argument
    '''
    # Creer le canvas
    
    canvas = tk.Canvas(frame, width=640 , height= 120, background='ivory')
#     Conseil
#     picture = tk.PhotoImage(file='lettres\A_r.png')#
#     # Cla ligne suivante est indispensable si ce code se trouve dans une fonction
#     #  car picture est une variable locale à cette fonction
#     # c'est sa référence qu'il faut passer ensutie à create.image()
#     # sinon le garbage collector fait disparaitre la référence picture
#     canvas.img = picture

    canvas = all_pic(canvas, 'b')

    for i in range(0, 26):
        if i < 13 :
            canvas.create_image(20 + 45*i, 10, anchor=NW, image=canvas.img[i])
        else:
            canvas.create_image(20 + 45*(i-13), 60, anchor=NW, image=canvas.img[i])
    canvas.pack()
    return canvas
    


if __name__ == "__main__":
    main_windows = tk.Tk()
    frame_0 = tk.Frame(main_windows, borderwidth=5, background='#0000f0')
    frame_0.pack()
    my_canvas = add_image(frame_0)
    add_button(my_canvas)
    main_windows.mainloop() # affiche les objets





