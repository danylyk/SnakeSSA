import json
import os

class Level():
    def __init__ (self, n):
        myfile = open(os.path.join("levels", str(n)+".sl"), mode="r")
        grid = json.load(myfile)
        myfile.close()
        self.grid = grid

    def get_obstracles(self):
        grid_copy = [[0,0,0,0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0,0,0,0]]
        for i in range (10):
            for j in range (10):
                grid_copy[i][j] = self.grid[i][j]
        a = []
        b = [] 
        for i in range (10):
            for j in range (10):
                if grid_copy[i][j] == 1 :
                    k = i
                    while k < len(grid_copy) and grid_copy[k][j] == 1:
                        grid_copy[k][j] = 0
                        k += 1
                    a.append([(i,j),(k-1,j)])
                if grid_copy[i][j] == 2 :
                    k = j
                    while k < len(grid_copy[i]) and grid_copy[i][k] == 2:
                        grid_copy[i][k] = 0
                        k += 1
                    b.append([(i,j),(i,k-1)])

        trap_grid = [a,b]
        return trap_grid

    def get_item (self, item):
        try: return self.grid[item[1]][item[0]]
        except: return 1

    def get_points(self) :
        a = []
        for i in range (10):
            for j in range (10):
                if self.grid[i][j] == 5:
                    a.append((i,j))
        return a

    def get_start(self) :
        for i in range (10):
            if self.grid[i][0] == 3:
                return (i,0)
        for i in range (9):
            if self.grid[0][i+1] == 3:
                return (0,i+1)
        for i in range (9):
            if self.grid[9][i+1] == 3:
                return (9,i+1)
        for i in range (8):
            if self.grid[i+1][9] == 3:
                return (i+1,9)

    def get_finish(self) :
        for i in range (10):
            if self.grid[i][0] == 4:
                return (i,0)
        for i in range (9):
            if self.grid[0][i+1] == 4:
                return (0,i+1)
        for i in range (9):
            if self.grid[9][i+1] == 4:
                return (9,i+1)
        for i in range (8):
            if self.grid[i+1][9] == 4:
                return (i+1,9)