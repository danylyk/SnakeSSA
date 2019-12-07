from level import Level

class Snake:
    def __init__(self, x, y, see):
        self.x = x
        self.y = y
        self.see = see

    def set_point(self):
        self.point += 1

    def snake_position(self):
        return (self.x, self.y)

    def move(self):
        self.x += self.see[0]
        self.y += self.see[1]
        return (self.x,self.y)

    def turn_right(self):
        if self.see == [1,0]:
            self.see == [0,-1]
        elif self.see == [0,-1]:
            self.see == [-1,0]
        elif self.see == [-1,0]:
            self.see == [0,1]
        else :
            self.see == [1,0]

    def turn_left(self):
        if self.see == [1,0]:
            self.see == [0,1]
        elif self.see == [0,1]:
            self.see == [-1,0]
        elif self.see == [-1,0]:
            self.see == [0,-1]
        else :
            self.see == [1,0]

def main():
    lev = Level ()
    for i in range (10):
        if lev.grid[i][0] == 3:
            x = 0
            y = i
            see = [1,0]
    for i in range (8):
        if lev.grid[0][i+1] == 3:
            x = i+1
            y = 0
            see = [0,-1]
    for i in range (8):
        if lev.grid[9][i+1] == 3:
            x = i+1
            y = 9
            see = [0,1]
    for i in range (10):
        if lev.grid[i][9] == 3:
            x = 9
            y = i
            see = [-1,0]
                
    snake = Snake(x, y, see)
    
    while True:
        for i in range (10) :
            print (lev.grid[i])
        command = input("Command : ")
        if command == "turn right":
            snake.turn_right()
        if command == "turn left":
            snake.turn_left()
        if command == "move":
            snake.move()

if __name__ == "__main__":
    main()