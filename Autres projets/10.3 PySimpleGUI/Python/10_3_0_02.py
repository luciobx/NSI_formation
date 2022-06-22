import PySimpleGUI as sg

# Choisir le thème
sg.theme('GrayGrayGray')  

# Lister les éléments utilisés
layout = [[sg.Text('nom_texte')],
          [sg.Input(), sg.FileBrowse()],
          [sg.OK(), sg.Cancel()]] 

# Créer la fenêtre
window = sg.Window('nom_fenetre', layout, finalize=True)

# Ecouter la fenêtre
event, values = window.read()

# Fermer par bouton
window.close()