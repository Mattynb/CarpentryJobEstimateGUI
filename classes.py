import PySimpleGUI as sg
from datetime import datetime

class House():
    def __init__(self, addy, ownr, rooms = [], stairs = [], costums = []):
        self.addy = str(addy)
        self.ownr = str(ownr) 
        self.rooms = rooms
        self.stairs = stairs 
        self.costums = costums
        self.startdate = datetime.now().strftime("%b %d %Y")


    def __str__(self):
        return f'{self.ownr}\'s property at {self.addy}. Started @{self.startdate}'

    def get_estimate(self, baseboard=False, Cromolden = False):
        cost = 0
        
        for room in self.rooms:
            cost += room.get_price(baseboard, Cromolden)
        
        for s in self.stairs:
            cost += s.get_price()

        for c in self.costums:
            cost += c.get_price()

        return cost

    def get_tabs(self):
        '''Returns tabgroup with all the rooms in the house'''
        tabG_cnt = []

        # gets the name and content of each room and add it to the house tabgroup
        for r in self.rooms:
            tabG_cnt.append([r.get_tab()])

        for s in self.stairs:
            tabG_cnt.append([s.get_tab()])
        
        for c in self.costums:
            tabG_cnt.append([c.get_tab()])

        
        return sg.TabGroup(tabG_cnt)

    def add_room(self, room):
        self.rooms.append(room)

    def add_stairs(self, stairs):
        self.stairs.append(stairs)



class Room():
    def __init__(self, name, sqft, doorN = 1, jan_N = 0, doubledoor = 0, cabinet = 0, vanity = 0):
        self.name = str(name)   #ex. "Room West"
        self.squareFt = float(sqft)
        self.doorN = int(doorN)
        self.jan_N = int(jan_N)
        self.doubledoor = int(doubledoor)
        self.cabinet = int(cabinet)
        self.vanity = int(vanity)
        self.attr = {'name': self.name, 'squareFt': self.squareFt, 'doorN': self.doorN, 'jan_N': self.jan_N, 'doubledoor': self.doubledoor, 'cabinet': self.cabinet, 'vanity': self.vanity}

        # prices
        self.basebwt = 3 #3$ per feet
        self.vanitywt = 300 
        self.doorwt = 175
        self.cabinwt = 1350 #cabinet set
        self.janwt = 190

    def get_info(self):
        return self.attr

    def get_tab(self):
        '''Returns Sg Element with 2*n layout'''

        #count = 0
        #col = []
        tab_lay = []  # contents of tab

        for i in self.attr:
            if type(self.attr[i]) == str:
                continue

            tab_lay.append([sg.T(f'{i} = {self.attr[i]}')])

            '''if self.attr[i] > 0:
                col.append(sg.T(f'{i} = {self.attr[i]}'))
                
                #if count == 0:
                    #col.append(sg.Stretch())

                count += 1

            if count == 2:
                tab_lay.append(col)
                count = 0
                col = []'''
            
        return sg.Tab(self.name, tab_lay)
    
    def get_price(self, baseboard=False, Cromolden = False, vanity = 0, cabinet = 0):
        cost = 0
        length = self.squareFt ** .5
        
        # per feet
        if baseboard:
            cost += (length * 4) * self.basebwt

        if Cromolden:
            cost += ((length * 4) * self.basebwt) * 1.3

        # per item        
        cost += self.vanity * self.vanitywt
        cost += self.cabinet * self.cabinwt

        # door
        cost += self.doorN * self.doorwt
        cost += self.doubledoor * (self.doorwt * 1.85) 

        # window
        cost += self.jan_N * self.janwt
        return cost


class Stairs():
    def __init__(self, name, steps):
        self.name = name
        self.steps = int(steps)
        self.attr = {'name': self.name, 'steps': self.steps}

        #price
        self.stepP = int(320)  

    def get_tab(self):
        return sg.Tab(self.name, [[sg.T(f'steps = {self.steps} * {self.stepP} = {self.steps * self.stepP}')]])

    def get_info(self):
        return self.attr

    def get_price(self):
        cost = self.steps * self.stepP
        return cost

    def set_step_price(self, price):
        self.stepP = price


class Costums():
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = int(price)
        self.quantity = int(quantity)
        self.attr = {'name': self.name, 'quantity': self.quantity}

    def get_tab(self):
        return sg.Tab(self.name, [[sg.T(f'{self.name} = {self.quantity} * {self.price} = {self.quantity * self.price}')]])

    def get_info(self):
        return self.attr

    def get_price(self):
        return self.quantity * self.price

      
