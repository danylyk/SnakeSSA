class CItem:
    def __init__ (self):
        self.next = [-1]
        pass

    def set_next (self, next): self.next[0] = next
    def get_next (self): pass

class CMove(CItem):
    def __init__ (self):
        self.next = [-1]
        self.image = "i1.png"
        self.type = 1
        self.p = 0

    def get_next (self): return self.next[self.p]

class CTurnLeft(CItem):
    def __init__ (self):
        self.next = [-1]
        self.image = "i3.png"
        self.type = 2
        self.p = 0

    def get_next (self): return self.next[self.p]

class CTurnRight(CItem):
    def __init__ (self):
        self.next = [-1]
        self.image = "i2.png"
        self.type = 3
        self.p = 0

    def get_next (self): return self.next[self.p]