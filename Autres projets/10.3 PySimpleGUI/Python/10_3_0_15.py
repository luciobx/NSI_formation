import PySimpleGUI as sg
sg.theme('GrayGrayGray')
layout = [[sg.Text('Chemin du fichier')],
          [sg.InputText(), sg.FileBrowse(button_text='Chercher')],
          [sg.Submit(button_text='Valider'), sg.Cancel(button_text='Annuler')]]
window = sg.Window('Sélecteur fichier', layout)
event, values = window.read()
window.close()
source_filename = values[0]



