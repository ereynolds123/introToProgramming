from math import sin, cos, radians

class Projection:
    
    def __init__(self, angle, velocity, height):
        self.xpos=0.0
        self.ypos =height
        theta = math.radians(angle)
        self.xvel =velocity * math.co