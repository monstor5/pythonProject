import PySimpleGUI as sg
import time
class pictures:
    mylist = [1, 2, 3, 4, 5, 6, 7, 8]
    progressbar = [
        [sg.ProgressBar(len(mylist), orientation='h', size=(51, 10), key='progressbar')]
    ]

    layout = [
        [sg.Frame('Progress', layout=progressbar)],
        [sg.Text('File 1'), sg.InputText(), sg.FileBrowse(),
         sg.Checkbox('Python'), sg.Checkbox('01(binary code)')
         ],
        [sg.Output(size=(88, 20))],
        [sg.Submit(), sg.Cancel()]
    ]

    window = sg.Window('File Compare', layout)
    while True:  # The Event Loop
        event, values = window.read()
        # print(event, values) #debug
        if event in (None, 'Exit', 'Cancel'):
            break
