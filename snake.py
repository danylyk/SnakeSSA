import math

class Snake:
    def __init__ (self, start):
        self.x = start[0]
        self.y = start[1]

        self.view = (1,0)
        self.trail = []
        self.points = []
        self.trail_shift = 0
        
        if (self.x == 0):
            self.view = (1,0)
        elif (self.x == 9):
            self.view = (-1,0)
        elif (self.y == 0):
            self.view = (0,1)
        elif (self.y == 9):
            self.view = (0,-1)

    def set_view (self, view):
        self.view = view;

    def get_angle (self):
        dir = -1
        if (self.view[1] < 0): dir = 1
        return dir*(math.acos((self.view[0]*1)/(self.__v_len(self.view)))/math.pi*180)

    def __v_len (self, v):
        return (v[0]**2+v[1]**2)**(1/2)
