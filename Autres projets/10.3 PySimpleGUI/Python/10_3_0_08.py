import PySimpleGUI as sg
sg.theme('GrayGrayGray')
text = sg.popup_get_text('Message utilisateur','Mon titre', \
                         text_color='black', \
                         default_text='12 euros')

