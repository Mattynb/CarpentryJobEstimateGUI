import PySimpleGUI as sg

# these sent by Room
tab_lay1 = [[sg.T('p = 122')],[sg.T('d = 23')]]
tab_lay2 = [[sg.T('p = 18')],[sg.T('d = 3')]]


tg_lay = [[sg.Tab('Hello', tab_lay1, sg.Tab('Hello2', tab_lay2))]]

# these sent by House
lay = [[sg.T('test')], [sg.TabGroup(tg_lay)]]

#this dealt by main
win = sg.Window('TTest', lay)

while True:
    
    e, v = win.read()

    if e == sg.WINDOW_CLOSED:
        win.close()
        break