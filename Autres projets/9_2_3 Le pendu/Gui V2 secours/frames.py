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

# from tkinter import Tk, RIGHT, LEFT, BOTH, RAISED, TOP
from tkinter import LEFT, RAISED, BOTH


def create_frame(main_gui):
    '''
    Creer les zones d'affichages
    main_gui : <class 'tkinter.Tk'>
    Renvoie la liste des Frames [<tkinter.Frame object .!frame>, ]
    '''
    #mesure de la fenêtre
    main_gui.update_idletasks() # Force la mise à jour des informations sur l'objet
    mgui_height = main_gui.winfo_height()
    mgui_width = main_gui.winfo_width()
    # Création des Frames
    frame_0 = tk.Frame(main_gui, width=mgui_width, height=mgui_height//3, relief=RAISED, borderwidth=5, background='#0000f0')
    frame_1 = tk.Frame(main_gui, width=mgui_width//2, height=mgui_height*2//3, relief=RAISED, borderwidth=5, background='#00f000')
    frame_2 = tk.Frame(main_gui, width=mgui_width//2, height=mgui_height*2//9, relief=RAISED, borderwidth=5, background='#f00000')
    frame_3 = tk.Frame(main_gui, width=mgui_width//2, height=mgui_height*2//9, relief=RAISED, borderwidth=5, background='#707070')
    frame_4 = tk.Frame(main_gui, width=mgui_width//2, height=mgui_height*2//9, relief=RAISED, borderwidth=5, background='#4300CB')
    # affichage des Frames
    frame_0.pack()
    frame_0.pack_propagate(0) # empecher le frame de s'adapter au contenu
    frame_1.pack(side=LEFT)
    frame_1.pack_propagate(0) # empecher le frame de s'adapter au contenu
    frame_2.pack()
    frame_2.pack_propagate(0) # empecher le frame de s'adapter au contenu
    frame_3.pack()
    frame_3.pack_propagate(0) # empecher le frame de s'adapter au contenu
    frame_4.pack()
    frame_4.pack_propagate(0) # empecher le frame de s'adapter au contenu
    # print('frame_1 :', frame_2['width'], frame_2['height']) # Pour debug
    return [frame_0, frame_1, frame_2, frame_3, frame_4]

if __name__ == "__main__":
    main_windows = tk.Tk()
    main_windows.geometry('200x300')
    frames_list = create_frame(main_windows)
    main_windows.mainloop() # affiche les objets
    
 
