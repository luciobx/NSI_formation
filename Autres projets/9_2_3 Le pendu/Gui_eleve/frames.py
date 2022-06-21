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
    pass

if __name__ == "__main__":
    main_windows = tk.Tk()
    main_windows.geometry('200x300')
    frames_list = create_frame(main_windows)
    main_windows.mainloop() # affiche les objets
    
 
