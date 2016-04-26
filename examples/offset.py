from bricklayer.levels.level_2 import *


def thing1():
    put_2D_2x2_BLUE(0, 0)
    put_2D_1x1_GREEN(1, 0)
    put_2D_1x1_GREEN(0, 1)

def thing2():
    put_2D_2x2_GREEN(0, 0)
    put_2D_1x1_BLUE(1, 0)
    put_2D_1x1_BLUE(0, 1)

thing1()

set_offset_2D(3, 0)

thing2()

set_offset_2D(3, 3)

thing1()

set_offset_2D(0, 3)

thing2()

output()