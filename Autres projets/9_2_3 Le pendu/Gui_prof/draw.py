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
    x0 = x - r
    y0 = y - r
    x1 = x + r
    y1 = y + r
    return canvasName.create_oval(x0, y0, x1, y1, width=5, fill="#000000")


def add_pendu(frame, level):
    '''
    Dessiner dans un canvas du frame
    le pendu au niveau level (x/15) au max
    '''
    # Vérifier que le frame est vide ou le vider ...
    # sinon on recrée un nouveau canvas à chaque fois 
    for widget in frame.winfo_children():
        widget.destroy()
    # creer la zone de dessin
    # print('framedessin:', frame['width'], frame['height']) # debug vérifier la taille du frame
    my_canvas = tk.Canvas(frame, background='ivory', width=frame['width'], height=frame['height'])
    # mesurer le canvas
    x_max = int(my_canvas['width'])
    y_max = int(my_canvas['height'])
    # print('canvas :', x_max, y_max)  # debug vérifier la taille du canvas
    
    # on definit une marge et une unit pour calculer ensuite tous les objets à dessiner
    pad_x = 20
    pad_y = 20
    unit = 50

    if level >= 1: 
        my_canvas.create_line(pad_x, y_max-2*pad_y, unit+pad_x, y_max-2*pad_y,width=5, fill="#ff0000") # base
    if level >= 2:
        my_canvas.create_line((unit//2+pad_x), y_max-2*pad_y, (unit//2+pad_x), pad_y,width=5, fill="#ff0000") # mat
    if level >= 3:
        my_canvas.create_line(pad_x, pad_y, 4*unit, pad_y,width=5, fill="#ff0000") # potence
    if level >= 4:
        my_canvas.create_line((unit//2+pad_x), unit+pad_y, 1.5 *unit + pad_x, pad_y,width=5, fill="#ff0000") # potence
    if level >= 5:
        my_canvas.create_line((3*unit+pad_x),pad_y, (3*unit+pad_x), unit+pad_y,width=5, fill="#00ff00") # corde
    if level >= 6:
        create_circle(my_canvas, (3*unit+pad_x), 1.2*unit+pad_y, unit/4) # head
    if level >= 7:
        my_canvas.create_line((3*unit+pad_x),1.5*unit+pad_y, (3*unit+pad_x), 2.5*unit+pad_y,width=5, fill="#0000ff") # buste
    if level >= 8:
        my_canvas.create_line((3*unit+pad_x),2*unit+pad_y, (3.5*unit+pad_x), 2.5*unit-pad_y,width=5, fill="#0000ff") # brasD
    if level >= 9:
        my_canvas.create_line((3*unit+pad_x),2*unit+pad_y, (2.5*unit+pad_x), 2.5*unit-pad_y,width=5, fill="#0000ff") # brasG
    if level >= 10:
        my_canvas.create_line((3*unit+pad_x),2.5*unit+pad_y, (2.7*unit+pad_x), 4*unit-pad_y,width=5, fill="#0000ff") # jambeG
    if level >= 11:
        my_canvas.create_line((3*unit+pad_x),2.5*unit+pad_y, (3.3*unit+pad_x), 4*unit-pad_y,width=5, fill="#0000ff") # jambeD
    if level >= 12:
        my_canvas.create_line((3.5*unit+pad_x), 2.5*unit-pad_y,(3.5*unit+1.3*pad_x),2.6*unit-pad_y, width=5, fill="#0000ff") # mainD
    if level >= 13:
        my_canvas.create_line((2.5*unit+pad_x), 2.5*unit-pad_y, (2.5*unit+0.7*pad_x),2.6*unit-pad_y, width=5, fill="#0000ff") # mainG
    if level >= 14:
        my_canvas.create_line((3.3*unit+pad_x), 4*unit-pad_y,(3.3*unit+1.3*pad_x),3.8*unit-pad_y, width=5, fill="#0000ff") # piedD
    if level >= 15:
        my_canvas.create_line((2.7*unit+pad_x), 4*unit-pad_y,(2.7*unit+0.7*pad_x),3.8*unit-pad_y, width=5, fill="#0000ff") # piedG    
    my_canvas.pack()


if __name__ == "__main__":
    main_windows = tk.Tk()
    main_windows.geometry('400x300')
    frame_0 = tk.Frame(main_windows, width='400', height='300', borderwidth=5, background='#0000f0')
    frame_0.pack()
    add_pendu(frame_0, 15)
    main_windows.mainloop() # affiche les objets
