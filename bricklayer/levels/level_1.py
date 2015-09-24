from bricklayer.spaces.virtual_space import VirtualSpace
from bricklayer.pieces.bricks import *

vs = VirtualSpace(100, 100, 100)

def put_2D_1x1_RED(point):
    put_2D((1,1,1), point, RED_BRICK)

def put_2D(dimensions, point, brick):
    x, y, z = point
    delta_x, _, delta_z = dimensions
    for i in range(delta_x):
       for j in range(delta_z):
           vs.add_brick((x+i, y, z+j), brick)

def output():
    vs.output_to_file('some_file_here')
