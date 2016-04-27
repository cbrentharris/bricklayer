from bricklayer.levels.level_2 import *
from math import pi

put_2D_1x1_BLACK(0, 0)
rotate_Y(pi / 4)
put_2D_1x1_BLACK(0, 2)
undo_rotation()
rotate_Z(pi / 4)
put_2D_1x1_BLACK(0, 4)
undo_rotation()
rotate_X(pi / 4)
put_2D_1x1_BLACK(0, 6)
undo_rotation()
rotate_X(pi / 4)
rotate_Y(pi / 4)
rotate_Z(pi / 4)
put_2D_1x1_BLACK(0, 8)
output()
