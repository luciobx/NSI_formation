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
    # creer la zone d'affichage
    my_canvas = tk.Canvas(frame, width=frame['width'], height=frame['height'], background='ivory')
    # Calculer le centre du frame
    my_canvas.update_idletasks()
    # print('frame :', frame['width'], frame['height']) 
    # print(my_canvas['width'], my_canvas['height'])
    my_text = my_canvas.create_text(int(my_canvas['width'])//2, int(my_canvas['height'])//2,
                                    fill="darkblue",
                                    font="Times 9 italic bold",
                                    anchor='center',
                                    justify='center',
                                    tag='my_text',
                                    text=message)
    my_canvas.pack()
    return my_canvas
 
if __name__ == "__main__":
    main_windows = tk.Tk()
    main_windows.geometry("500x300")
    frame_0 = tk.Frame(main_windows, width=500, height=300, borderwidth=5, background='#0000f0')
    frame_0.pack(fill=BOTH, expand=True)
    canvas_0 = add_text(frame_0, "Affiché au centre !")
    main_windows.mainloop() # affiche les objets
