
class vec:

    def __init__(self, x, y):
        self.x = x
        self.y = y 

    def __add__(self, temp):
        return vec(self.x + temp.x, self.y + temp.y)

    def __eq__(self, temp):
        return self.x == temp.x and self.y == temp.y
    
    def __sub__(self, temp):
        return vec(self.x-temp.x, self.y - temp.y)
    
    def __mul__(self, temp):
        if isinstance(temp, vec):
            return vec(self.x * temp.x, self.y * temp.y)
        else:
            return vec( self.x * temp, self.y * temp)  