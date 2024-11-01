from __future__ import annotations # for forward references in classes
import math


def scalar_product(vector1: Vector, vector2: Vector) -> float:
    """
    Scalar product of two vectors.
    Both arguments should be Vector-class objects.
    """
    if not isinstance(vector1, Vector) or not isinstance(vector2, Vector):
        raise TypeError("Invalid argument type. Accepting only Vector-class objects.")
    
    return vector1.vx * vector2.vx + vector1.vy * vector2.vy



def dist_point_to_point(point1: Point, point2: Point) -> float:
    """
    Returns euclidean distance between two points.
    Both arguments should be Point-class objects.
    """
    if not isinstance(point1, Point) or not isinstance(point2, Point):
        raise TypeError("Invalid argument type. Accepting only Point-class objects.")
    
    p1x, p1y = point1.return_coords()
    p2x, p2y = point2.return_coords()
    dx=p1x-p2x
    dy=p1y-p2y

    return math.sqrt(dx**2 + dy**2)






class Point:
    """
    Point class representing point in R2 space.
    """
    def __init__(self, px, py, c=0):
        """
        px: x-coordinate
        py: y-coordinate
        c: color 0,1,2 or 3, default is 0
        """
        self.px = px
        self.py = py
        self.c = c # color

    def __str__(self) -> str: # Point-class objects can now be directly called in print()
        return f"Point({self.px}, {self.py})"

    def return_coords(self):
        """
        return point coordinates
        """
        return self.px, self.py
    
    def translation_by_vector(self, vector: Vector):
        """
        Translate point by a vector.
        vector needs to be Vector-class object
        """

        if not isinstance(vector, Vector):
            raise TypeError("Arguent should be Vector-class object.")

        self.px += vector.vx
        self.py += vector.vy

            



    
class Vector:
    """
    Vector class representing vector in R2.
    Vector-class object has:
    vx,vy - coordiates of the vector in standard base (e1, e2)
    startpoint (optional) - point in R2 space that is the starting point for the vector. This can be just (0,0) or any given starting point
    """
    def __init__(self, *args, attach=False): 
        """
        Arguments to be passed as *args should be in one of the following form:
        1) vx and vy, both as floats
        2) p1 and p1, both Point-class objects
        3) seg, one Segment-class object
        4) vec, one Vector-class object (for copying)

        'attach' takes boolean value and if true, remembers starting point if two points were passed.

        Examples:
        TODO: ...

        """

        if len(args) > 2:
            raise IndexError("Passed to many arguments. Args should be two Points, two floats or one Segment.")


        #TODO: below some code for 'attach' should be refactored. Now there is huge overuse of if's


        elif len(args) == 2 and isinstance(args[0], Point) and isinstance(args[1], Point):
            self.vx = args[1].px - args[0].px
            self.vy = args[1].py - args[0].py
            if attach:
                self.startpoint = args[0] # for two points, first one is starting point
            else: 
                self.startpoint = Point(0,0,0)

        elif len(args) ==2 and isinstance(args[0], float) and isinstance(args[1], float):
            self.vx = args[0]
            self.vy = args[1]
            self.startpoint = Point(0,0,0) # for two floats, set startpoint to just (0,0)

        elif len(args) == 1 and isinstance(args[0], Segment): # make vector from Segment
            self.vx = args[0].P2.px - args[0].P1.px
            self.vy = args[0].P2.py - args[0].P1.py
            if attach:
                self.startpoint= args[0].P1
            else:
                self.startpoint = Point(0,0,0)

        elif len(args) == 1 and isinstance(args[0], Vector): # create copy of passed vector
            self.vx = args[0].vx
            self.vy = args[0].vy
            if attach:
                self.startpoint = args[0].startpoint      
            else:
                self.startpoint = Point(0,0,0)      

        else: # catch any other exeption, make zero-vector
            self.vx = 0  
            self.vy = 0
            self.startpoint = Point(0,0,0) 
    


    def __str__(self) -> str: # Vector-class objects can now be directly called in print()
        return f"Vector({self.vx}, {self.vy}) attached at {self.startpoint}"



    def get_vector(self):
        return self
    
    def get_vx(self):
        return self.vx
    
    def get_vy(self):
        return self.vy
    
    def norm(self) -> float:
        """
        Returns euclidean norm of the vector.
        """
        return math.sqrt(self.vx**2+self.vy**2)
    
    def multiply_by_scalar(self, scalar):
        """
        Multiply vector by given scalar
        """
        self.vx=scalar*self.vx, 
        self.vy=scalar*self.vy


    def normalize(self):
        """
        Inplace (!) normalization of vector. To get normalized copy of vector, go to get_normalized()
        """
        n = self.norm()

        if n <=0: 
            raise ZeroDivisionError("Vector length is zero. Cannot normalize vector of that length.")
        else:
            self.vx = self.vx / n
            self.vy = self.vy / n




    def get_normalized(self) -> Vector:
        """
        Returns normalized vector. Does not work inplace. To normalize inplace, go to normalize()
        """
        v = Vector(self) # copy
        v.normalize()
        return v









class Segment:
    """
    Segment bounded by two points.
    """
    def __init__(self, P1: Point, P2: Point):
        """
        Constructor takes two points (Point-class objects).
        """
        if not isinstance(P1, Point) or not isinstance(P2, Point):
            raise TypeError("Arguments should be Point-class objects.")
        
        self.P1 = P1
        self.P2 = P2
    



    def length(self) -> float:
        """
        Return length of segment.
        """
        return dist_point_to_point(self.P1, self.P2)
    


