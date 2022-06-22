import PySimpleGUI as sg
sg.theme('GrayGrayGray')
# 3 listes sont placées dans une liste qui représente la fenêtre entière.
layout = [[sg.Text('Enter a Number')],
          [sg.Input()],
          [sg.OK()] ]

window = sg.Window('Entrer un nombre', layout)
event, values = window.read()
window.close()
sg.Popup(event, values[0])



