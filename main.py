from genericpath import isfile
import PySimpleGUI as sg
from new_house import new_house
import pickle
import os


def main():
    sg.theme('GreenTan')

    # uses the default layout
    lay = [[sg.Text('Estimates GUI', font='underline')]]
    
    # looks for saved houses
    try:
        #appends house to layout
        i = 0
        while i <= 10:
            try:
                h = open(f'pickles/house{i}.txt', 'rb')
                houses = pickle.load(h)
                h.close()
                
                l = [
                [sg.T(f'Est. Price = ${round(houses.get_estimate(True))}  | Est. Hours to complete  = {round(houses.get_estimate(True)/100)}')], 
                [sg.Stretch(), houses.get_tabs(), sg.Stretch()], 
                [sg.Stretch(), sg.Button('Delete_House', key=  f'{i}')]]
 
                l = [sg.Frame(f'{str(houses)}', l)]
                lay.append(l)
                
                i = i + 1
            
            except:
                i = i + 1

    except:
        #there is no house yet
        print('there is no house yet?')
        
    lay.append([sg.B('Add House')])
    win = sg.Window('Estimates GUI', lay, keep_on_top=True)

    main_loop(win)


def main_loop(win):
    i2 =0
    while True:
        e, v = win.read(timeout=0)
        
        if e != '__TIMEOUT__':
            #print(e)
            ...

        if e == sg.WINDOW_CLOSED:
            win.close()
            break

        if e == 'Add House':
            win.close()
            house = new_house()
            
            # to make sure it wont save on existing file
            i = 0 
            while i <= 10:
                if isfile(f'pickles/house{i}.txt'):
                    i = i + 1
                else: break
            
            f = open(f'pickles/house{i}.txt', 'wb')   
            pickle.dump(house, f)      #saves the house
            f.close()
            main()
            break

        # checks for the event to delete a housefile
        for i in range(10):
                if str(i2) == e:
                    os.remove(f'pickles/house{i2}.txt')
                    win.close()
                    main()
                    break

                i2 += i
        i2 = 0


if __name__ == '__main__':
    main()
