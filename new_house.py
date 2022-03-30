import PySimpleGUI as sg
from classes import House, Room
from new_room import new_room
from new_stair import new_stair
from new_costum import new_costum


def new_house():

    lay = [[sg.I('Address', key='addy')],[sg.I('Owner Name', key='ownr')], [sg.B('Add Room to House', key='newroom'), sg.B('Add Stairs'), sg.B('Add Costum')], [sg.Button('Done')]]
    win = sg.Window("New House", lay, keep_on_top=True)
    rooms = []
    stairs = []
    costums = []

    while True:

        e, v = win.read()

        if e == sg.WINDOW_CLOSED:
            win.close()
            return #values?

        if e == 'newroom':
            rooms.append(new_room())

        if e == 'Add Stairs':
            stairs.append(new_stair())

        if e == 'Add Costum':
            costums.append(new_costum())

        if e == 'Done':
            win.close()
            return House(v['addy'], v['ownr'], rooms, stairs, costums)

            

if __name__ == '__main__':
    new_house()
