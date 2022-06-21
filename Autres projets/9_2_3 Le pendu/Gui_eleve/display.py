# Realisation d'une interface GUI
# By Luc VINCENT 
# 2021.11.23
# module de pendu_gui
# 1.0
# luc.vincent@ac-bordeaux.fr
# sys.version '3.7.9 (tags/v3.7.9:13c94747c7, Aug 17 2020, 18:01:55) [MSC v.1900 32 bit (Intel)]'
# tkinter.TkVersion 8.6
    
import tkinter as tk
from tkinter import BOTH

def add_text(frame, message):
    ''' Renvoie le message dans un canvas placé dans le frame
    message: str message à afficher
    frame: <class 'tkinter.Frame'>
    renvoie un objet <class 'tkinter.Canvas'> 
    '''
    pass
 
if __name__ == "__main__":
    main_windows = tk.Tk()
    main_windows.geometry("500x300")
    frame_0 = tk.Frame(main_windows, width=500, height=300, borderwidth=5, background='#0000f0')
    frame_0.pack(fill=BOTH, expand=True)
    canvas_0 = add_text(frame_0, "Affiché au centre !")
    main_windows.mainloop() # affiche les objets
