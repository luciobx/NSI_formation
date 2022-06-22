import PySimpleGUI as sg
sg.popup('This is a popup.....Make sure it is long enough to see title.',
    title="my_own",
    button_color =  'grey',
    background_color = 'cyan',
    text_color = 'black',
    custom_text = ('oui', 'non'),
    line_width = 40)