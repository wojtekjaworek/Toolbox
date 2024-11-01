from Toolbox import *
import os
import sys

def get_working_directory(): #funkcja 
    if getattr(sys, 'frozen', False):
        return os.path.dirname(sys.executable)
    else:
        return os.path.dirname(os.path.abspath(__file__))

if __name__ == '__main__':
    os.chdir(get_working_directory())


    point1 = Point(0,0,0)

    point2 = Point(1,1,0)

    vec1 = Vector(1.0,1.0)

    seg1 = Segment(Point(0.0, 0.0,0), Point(1.0, 1.0,0))


    vec2 = Vector(seg1)

    print(vec2.norm())









