class Level():
    def __init__ (self):
        self.grid = [[0,0,0,1,0,0,0,0,0,0],
                     [3,0,0,1,0,0,0,0,0,0],
                     [0,0,0,1,0,1,0,0,0,0],
                     [0,0,0,0,0,1,0,0,0,0],
                     [0,0,0,0,0,1,0,5,0,0],
                     [0,0,5,0,0,1,0,0,0,4],
                     [0,0,0,0,0,0,0,0,0,0],
                     [0,0,0,0,2,2,2,2,0,0],
                     [0,0,0,0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0,0,0,0]]

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
                    while grid_copy[k][j] == 1:
                        grid_copy[k][j] = 0
                        k += 1
                    a.append([(i,j),(k-1,j)])
                if grid_copy[i][j] == 2 :
                    k = j
                    while grid_copy[i][k] == 2:
                        grid_copy[i][k] = 0
                        k += 1
                    b.append([(i,j),(i,k-1)])

        trap_grid = [a,b]
        return trap_grid

    def get_points() :
        a = []
        for i in range (10):
            for j in range (10):
                if self.grid[i][j] == 5:
                    a = (i,j)
        return a

    def get_start() :
        for i in range (10):
            for j in range (10):
                if self.grid[i][j] == 3:
                    return (i,j)

    def get_finish() :
        for i in range (10):
            for j in range (10):
                if self.grid[i][j] == 4:
                    return (i,j)