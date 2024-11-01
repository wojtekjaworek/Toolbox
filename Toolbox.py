import math

def scalar_product(vector1, vector2)->float:
    return vector1.vx*vector2.vx + vector1.vy*vector2.vy

def dist_point_to_point(point1, point2)->float:
    p1x, p1y = point1.return_coords()
    p2x, p2y = point2.return_coords()
    dx=p1x-p2x
    dy=p1y-p2y
    return math.sqrt(dx**2 + dy**2)

def return_unit_vector(vector):
    norm = vector.norm()
    return vector.multiply_by_scalar(norm)

class Point:
    def __init__(self, px, py, c=0):
        self.px = px
        self.py = py
        self.c = c # color

    def return_coords(self):
        return self.px, self.py
    
    def translation_by_vector(self, vector):
        self.px+=vector.vx
        self.py+=vector.vy
    
class Vector:
    def __init__(self, *args): # A starting, B ending
        if len(args) > 2:
            None # error here, moze byc tylko dwa punkty, dwa floaty albo jeden odcinek
        elif len(args) == 2 and isinstance(args[0], Point) and isinstance(args[1], Point):
            self.vx = args[1].px - args[0].px
            self.vy = args[1].py - args[0].py
            self.startpoint = args[0]
        elif len(args) ==2 and isinstance(args[0], float) and isinstance(args[1], float):
            self.vx = args[0]
            self.vy = args[1]
            self.startpoint = Point(0,0,0)

        elif len(args) == 1 and isinstance(args[0], Segment):
            self.vx = args[0].P2.px - args[0].P1.px
            self.vy = args[0].P2.py - args[0].P1.py
            self.startpoint= args[0].P1

        else:
            self.vx = 0 # FIXME. trzeba przemyslec czy 0,0,0 czy lepiej NaN albo None czy cos w tym stylu
            self.vy = 0
            self.startpoint = Point(0,0,0) 
    

    def get_vector(self):
        return self
    
    def get_vx(self):
        return self.vx
    
    def get_vy(self):
        return self.vy
    
    def norm(self)->float:
        return math.sqrt(self.vx**2+self.vy**2)
    
    def multiply_by_scalar(self, scalar):
        self.vx=scalar*self.vx, 
        self.vy=scalar*self.vy

class Segment:
    def __init__(self, P1, P2):
        self.P1 = P1
        self.P2 = P2
    
    def length(self)->float:
        return dist_point_to_point(self.P1, self.P2)
    


