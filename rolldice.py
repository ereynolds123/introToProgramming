from random import randrange

class dice:
    def __init__(self, sides, value):
        self.sides = sides
        self.value =value
        
    def getValue(self):
        return self.value
    
    def setValue(self, value):
        self.value = value
    
    def roll(self):
        self.value = randrange(1, self.sides+1)