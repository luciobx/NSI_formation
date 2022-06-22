# On importe le module
import PySimpleGUI as sg
# On prépare la dsiposition (layout) des éléments 
layout = [ [sg.Text('Une information')],
           [sg.Input(key='-IN-')],
           [sg.Text(size=(20,1), key='-OUT-')],
           [sg.Button('Aller', key='-GO-'), sg.Button('Sortir', key='-END-')] ]
# On définit l'objet fenêtre
window = sg.Window('Titre fenêtre', layout, finalize=True)
# On scrute les évenements
while True:
    # Observer l'évenement et sa valeur
    event, values = window.read()
    print(event, values)
    if event in (None, 'END'):
        # On peut sortir par la croix ou le bouton
        break
    if event == '-GO-':
        # On traite l'évenement
        window['-OUT-'].update(values['-IN-'])
# On ferme le programme
window.close()