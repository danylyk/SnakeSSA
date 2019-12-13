from Items import *

class Control:
    def __init__ (self):
        self.p = 0
        self.history = []
        self.road = []  

    def add_item (self, item: CItem):
        self.history.append([self.p, item])
        if (len(self.history) > 1):
            if (self.history[len(self.history)-2][1].get_next() < 0):
                self.history[len(self.history)-2][1].set_next(self.p)
            else:
                self.history[self.history[len(self.history)-2][1].get_next()][1].set_next(self.p)
        self.p += 1

    def delete_item (self, counter):
        if counter > 0 :
            a = self.history[counter][1].get_next()
            b = self.history[self.history[counter-1][1].get_next()][1]
            if b.type != 4 :                
                del self.history[counter]
                self.history[counter-1][1].set_next(a)
            else:
                while (b.get_next() != counter):
                    b = self.history[b.get_next()][1]
                del self.history[counter]
                self.history[b].set_next(a)

    def add_item_into_place(self, item: CItem, place):
        pass

    def get_road(self, start):
        self.road = [start]
        x = start[0]
        y = start[1]
        view = (0,0)
        if (x == 0):
            view = (1,0)
        elif (x == 9):
            view = (-1,0)
        elif (y == 0):
            view = (0,1)
        elif (y == 9):
            view = (0,-1)
        pointer = 0
        while True :
            if pointer == -1:
                break
            if self.history[pointer][1].type == 1:
                x += view[0]
                y += view[1]
                self.road.append((x,y))
            elif self.history[pointer][1].type == 2:
                if view == (1,0):
                    view = (0,-1)
                elif view == (0,-1):
                    view = (-1,0)
                elif view == (-1,0):
                    view = (0,1)
                elif view == (0,1):
                    view = (1,0)
            elif self.history[pointer][1].type == 3:
                if view == (1,0):
                    view = (0,1)
                elif view == (0,1):
                    view = (-1,0)
                elif view == (-1,0):
                    view = (0,-1)
                elif view == (0,-1):
                    view = (1,0)
            pointer = self.history[pointer][1].get_next()
        return self.road