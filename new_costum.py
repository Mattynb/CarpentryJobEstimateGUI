import PySimpleGUI as sg
from classes import Costums


def new_costum():

    lay = [
    [sg.Input('Name', key='name')], 
    [sg.T('Quantity'), sg.Stretch(), sg.DropDown([i for i in range(100)], default_value=0, key='Quantity')], 
    [sg.T('Price per Item'), sg.Stretch(), sg.DropDown([i for i in range(100)], default_value=0, key='price')], 
    [sg.B('Ok'), sg.B('close')]
    ]

    win = sg.Window('New Costum', lay, keep_on_top=True)

    while True:
        e, v = win.read()

        if e == 'close' or e == sg.WINDOW_CLOSED:
            win.close()
            return

        if e == 'Ok':
            try:
                newRoom = Costums(v['name'], v['price'], v['Quantity'])
                win.close()
                return newRoom
                
            except:
                sg.popup("Something went Wrong", keep_on_top=True)


if __name__ == '__main__':
    new_costum()