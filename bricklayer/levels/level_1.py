from bricklayer.space.virtual_space import VirtualSpace
from bricklayer.pieces.bricks import *
from tempfile import NamedTemporaryFile
import subprocess

vs = VirtualSpace((100, 100, 100))

put_2D_1x1_RED    = lambda *point : put_2D((1,1,1), point, RED_BRICK)
put_2D_1x1_WHITE  = lambda *point : put_2D((1,1,1), point, WHITE_BRICK)
put_2D_1x1_BLUE   = lambda *point : put_2D((1,1,1), point, BLUE_BRICK)
put_2D_1x1_YELLOW = lambda *point : put_2D((1,1,1), point, YELLOW_BRICK)
put_2D_1x1_GREEN  = lambda *point : put_2D((1,1,1), point, GREEN_BRICK)
put_2D_1x1_GRAY   = lambda *point : put_2D((1,1,1), point, GRAY_BRICK)
put_2D_1x1_BLACK  = lambda *point : put_2D((1,1,1), point, BLACK_BRICK)
put_2D_1x1_EMPTY  = lambda *point : put_2D((1,1,1), point, EMPTY_BRICK)

put_2D_2x1_RED    = lambda *point : put_2D((2,1,1), point, RED_BRICK)
put_2D_2x1_WHITE  = lambda *point : put_2D((2,1,1), point, WHITE_BRICK)
put_2D_2x1_BLUE   = lambda *point : put_2D((2,1,1), point, BLUE_BRICK)
put_2D_2x1_YELLOW = lambda *point : put_2D((2,1,1), point, YELLOW_BRICK)
put_2D_2x1_GREEN  = lambda *point : put_2D((2,1,1), point, GREEN_BRICK)
put_2D_2x1_GRAY   = lambda *point : put_2D((2,1,1), point, GRAY_BRICK)
put_2D_2x1_BLACK  = lambda *point : put_2D((2,1,1), point, BLACK_BRICK)
put_2D_2x1_EMPTY  = lambda *point : put_2D((2,1,1), point, EMPTY_BRICK)

put_2D_1x2_RED    = lambda *point : put_2D((1,1,2), point, RED_BRICK)
put_2D_1x2_WHITE  = lambda *point : put_2D((1,1,2), point, WHITE_BRICK)
put_2D_1x2_BLUE   = lambda *point : put_2D((1,1,2), point, BLUE_BRICK)
put_2D_1x2_YELLOW = lambda *point : put_2D((1,1,2), point, YELLOW_BRICK)
put_2D_1x2_GREEN  = lambda *point : put_2D((1,1,2), point, GREEN_BRICK)
put_2D_1x2_GRAY   = lambda *point : put_2D((1,1,2), point, GRAY_BRICK)
put_2D_1x2_BLACK  = lambda *point : put_2D((1,1,2), point, BLACK_BRICK)
put_2D_1x2_EMPTY  = lambda *point : put_2D((1,1,2), point, EMPTY_BRICK)

put_2D_2x2_RED    = lambda *point : put_2D((2,1,2), point, RED_BRICK)
put_2D_2x2_WHITE  = lambda *point : put_2D((2,1,2), point, WHITE_BRICK)
put_2D_2x2_BLUE   = lambda *point : put_2D((2,1,2), point, BLUE_BRICK)
put_2D_2x2_YELLOW = lambda *point : put_2D((2,1,2), point, YELLOW_BRICK)
put_2D_2x2_GREEN  = lambda *point : put_2D((2,1,2), point, GREEN_BRICK)
put_2D_2x2_GRAY   = lambda *point : put_2D((2,1,2), point, GRAY_BRICK)
put_2D_2x2_BLACK  = lambda *point : put_2D((2,1,2), point, BLACK_BRICK)
put_2D_2x2_EMPTY  = lambda *point : put_2D((2,1,2), point, EMPTY_BRICK)

put_2D_2x3_RED    = lambda *point : put_2D((2,1,3), point, RED_BRICK)
put_2D_2x3_WHITE  = lambda *point : put_2D((2,1,3), point, WHITE_BRICK)
put_2D_2x3_BLUE   = lambda *point : put_2D((2,1,3), point, BLUE_BRICK)
put_2D_2x3_YELLOW = lambda *point : put_2D((2,1,3), point, YELLOW_BRICK)
put_2D_2x3_GREEN  = lambda *point : put_2D((2,1,3), point, GREEN_BRICK)
put_2D_2x3_GRAY   = lambda *point : put_2D((2,1,3), point, GRAY_BRICK)
put_2D_2x3_BLACK  = lambda *point : put_2D((2,1,3), point, BLACK_BRICK)
put_2D_2x3_EMPTY  = lambda *point : put_2D((2,1,3), point, EMPTY_BRICK)

put_2D_3x2_RED    = lambda *point : put_2D((3,1,2), point, RED_BRICK)
put_2D_3x2_WHITE  = lambda *point : put_2D((3,1,2), point, WHITE_BRICK)
put_2D_3x2_BLUE   = lambda *point : put_2D((3,1,2), point, BLUE_BRICK)
put_2D_3x2_YELLOW = lambda *point : put_2D((3,1,2), point, YELLOW_BRICK)
put_2D_3x2_GREEN  = lambda *point : put_2D((3,1,2), point, GREEN_BRICK)
put_2D_3x2_GRAY   = lambda *point : put_2D((3,1,2), point, GRAY_BRICK)
put_2D_3x2_BLACK  = lambda *point : put_2D((3,1,2), point, BLACK_BRICK)
put_2D_3x2_EMPTY  = lambda *point : put_2D((3,1,2), point, EMPTY_BRICK)

put_2D_4x2_RED    = lambda *point : put_2D((4,1,2), point, RED_BRICK)
put_2D_4x2_WHITE  = lambda *point : put_2D((4,1,2), point, WHITE_BRICK)
put_2D_4x2_BLUE   = lambda *point : put_2D((4,1,2), point, BLUE_BRICK)
put_2D_4x2_YELLOW = lambda *point : put_2D((4,1,2), point, YELLOW_BRICK)
put_2D_4x2_GREEN  = lambda *point : put_2D((4,1,2), point, GREEN_BRICK)
put_2D_4x2_GRAY   = lambda *point : put_2D((4,1,2), point, GRAY_BRICK)
put_2D_4x2_BLACK  = lambda *point : put_2D((4,1,2), point, BLACK_BRICK)
put_2D_4x2_EMPTY  = lambda *point : put_2D((4,1,2), point, EMPTY_BRICK)

put_2D_2x4_RED    = lambda *point : put_2D((2,1,4), point, RED_BRICK)
put_2D_2x4_WHITE  = lambda *point : put_2D((2,1,4), point, WHITE_BRICK)
put_2D_2x4_BLUE   = lambda *point : put_2D((2,1,4), point, BLUE_BRICK)
put_2D_2x4_YELLOW = lambda *point : put_2D((2,1,4), point, YELLOW_BRICK)
put_2D_2x4_GREEN  = lambda *point : put_2D((2,1,4), point, GREEN_BRICK)
put_2D_2x4_GRAY   = lambda *point : put_2D((2,1,4), point, GRAY_BRICK)
put_2D_2x4_BLACK  = lambda *point : put_2D((2,1,4), point, BLACK_BRICK)
put_2D_2x4_EMPTY  = lambda *point : put_2D((2,1,4), point, EMPTY_BRICK)

def put_2D(dimensions, point, brick):
    x, z = point
    y = 0
    delta_x, _, delta_z = dimensions
    for i in range(delta_x):
       for j in range(delta_z):
           vs.add_brick((x+i, y, z+j), brick)

def output():
    f = NamedTemporaryFile(suffix='.lxfml')
    vs.output_to_file(f.name)
    subprocess.call(['open', '-W', f.name])
    
