import PySimpleGUI as sg
from classes import Room


def new_room():

    lay = [
        [sg.I('Room Name', key='name')], [sg.I('Total Sqft', key='sqft')], 
        [sg.T('# of Doors'), sg.Stretch(), sg.DropDown([i for i in range(100)], default_value=0, key='doorN')], 
        [sg.T('# of Windows'), sg.Stretch(), sg.DropDown([i for i in range(100)], default_value=0, key='janN')], 
        [sg.T('# of Double Doors'), sg.Stretch(), sg.DropDown([i for i in range(100)], default_value=0, key='DD')], 
        [sg.T('# of cabinets'), sg.Stretch(), sg.DropDown([i for i in range(100)], default_value=0, key='cabs')], 
        [sg.T('# of vanities'), sg.Stretch(), sg.DropDown([i for i in range(100)], default_value=0, key='van')], 
        [sg.B('Ok')]]

   
    win = sg.Window("New Room", lay, keep_on_top=True)

    while True:
        e, v = win.read()

        if e == 'close' or e == sg.WINDOW_CLOSED:
            win.close()
            return

        if e == 'Ok':
            try:
                newRoom = Room(v['name'], v['sqft'], v['doorN'], v['janN'], v['DD'], v['cabs'], v['van'])
                win.close()
                return newRoom
                
            except:
                sg.popup("Total Sqft needs to be a number", keep_on_top=True)
                


if __name__ == '__main__':
    new_room()

