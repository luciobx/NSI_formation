# Realisation d'une interface GUI
# By Luc VINCENT 
# 2021.11.20
# Programme root
# 1.0
# module de pendu_gui
# luc.vincent@ac-bordeaux.fr
# sys.version '3.7.9 (tags/v3.7.9:13c94747c7, Aug 17 2020, 18:01:55) [MSC v.1900 32 bit (Intel)]'
# tkinter.TkVersion 8.6

# Realiser les imports
import tkinter as tk


def create_main():
    '''
    Créer un objet fenêtre graphique des dimensions souhaitées
    Renvoyer un objet fenêtre graphique <class 'tkinter.Tk'>
    '''
    # On crée l'objet
    gui = tk.Tk()
    # modifie les propriétés
    gui.title("le pendu") 
    gui.configure(bg="#E5E6AE")
    gui.iconbitmap("icone.ico") # https://convertir-une-image.com/
    # mesurer ecran
    screen_width = gui.winfo_screenwidth()
    screen_height = gui.winfo_screenheight()
    # calculer la fenetre
    gui_width_offset = str(screen_width // 4)
    gui_height_offset = str(screen_height //4)
    screen_width = str(screen_width // 2)
    screen_height = str(screen_height //2)
    gui_dimensions = screen_width + 'x' + screen_height\
                     + '+' + gui_width_offset + '+' + gui_height_offset
    gui.geometry (gui_dimensions)
    gui.resizable(width=False,height=False)
    #print('fenetre :', gui.winfo_width(), gui.winfo_height()) # pour debug
    return gui

if __name__ == "__main__":
    main_windows = create_main()
    main_windows.mainloop() # affiche les objets
