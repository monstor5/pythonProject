
import PySimpleGUI as sg


layout = [
    [sg.Text('File 1'), sg.InputText(), sg.FileBrowse(),
     sg.Checkbox('Python'), sg.Checkbox('01(binary code)')
     ],
    [sg.Output(size=(88, 20))],
    [sg.Submit(), sg.Cancel()]
]

window = sg.Window('File Compare', layout)
while True:                             # The Event Loop
    event, values = window.read()
    # print(event, values) #debug
    if event in (None, 'Exit', 'Cancel'):
        break

