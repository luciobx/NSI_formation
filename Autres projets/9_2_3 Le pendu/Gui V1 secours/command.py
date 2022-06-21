# Realisation d'une interface GUI
# By Luc VINCENT 
# 2021.11.23
# module de pendu_gui
# 1.0
# luc.vincent@ac-bordeaux.fr
# sys.version '3.7.9 (tags/v3.7.9:13c94747c7, Aug 17 2020, 18:01:55) [MSC v.1900 32 bit (Intel)]'
# tkinter.TkVersion 8.6

import tkinter as tk
 #from vocabulaire import open_json
from mot import valid_word


def add_change(frame):
    change_button = tk.Button(frame, text ="Changer de mot") # command = helloCallBack
    change_button.pack(expand=True)
    return change_button
    
if __name__ == "__main__":
    word = ''
    main_windows = tk.Tk()
    frame_0 = tk.Frame(main_windows, borderwidth=5, background='#0000f0')
    frame_0.pack()
    add_change(frame_0)
    main_windows.mainloop() # affiche les objets