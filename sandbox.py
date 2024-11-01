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


    

    seg = Segment((0,1), (0,2))

    p1=(0,0)
    p2 = (1,0)
    print(dist_point_to_point(p1,p2))






