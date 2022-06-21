# Realisation d'une interface GUI
# By Luc VINCENT 
# 2021.11.23
# module de pendu_gui
# 1.0
# luc.vincent@ac-bordeaux.fr
# sys.version '3.7.9 (tags/v3.7.9:13c94747c7, Aug 17 2020, 18:01:55) [MSC v.1900 32 bit (Intel)]'
# tkinter.TkVersion 8.6

import tkinter as tk

def create_circle(canvasName, x, y, r ): #center coordinates, radius
    '''
    Cree un cercle de centre x, y et de rayon r dans le canvas
    '''
    pass


def add_pendu(frame, level):
    '''
    Dessiner dans un canvas du frame
    le pendu au niveau level (x/15) au max
    '''
    pass


if __name__ == "__main__":
    main_windows = tk.Tk()
    main_windows.geometry('400x300')
    frame_0 = tk.Frame(main_windows, width='400', height='300', borderwidth=5, background='#0000f0')
    frame_0.pack()
    add_pendu(frame_0, 15)
    main_windows.mainloop() # affiche les objets
