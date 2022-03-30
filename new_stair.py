
import PySimpleGUI as sg
from classes import Stairs


def new_stair():

    lay = [[sg.Input('Stair Name', key='name')], 
    [sg.T('# of Steps'), sg.Stretch(), sg.DropDown([i for i in range(100)], default_value=0, key='steps')], 
    [sg.B('Ok'), sg.B('close')]]

    win = sg.Window('New Stair', lay, keep_on_top=True)

    while True:
        e, v = win.read()

        if e == 'close' or e == sg.WINDOW_CLOSED:
            win.close()
            return

        if e == 'Ok':
            try:
                newRoom = Stairs(v['name'], v['steps'])
                win.close()
                return newRoom
                
            except:
                sg.popup("Something went Wrong", keep_on_top=True)


if __name__ == '__main__':
    new_stair()