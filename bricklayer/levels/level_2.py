from level_1 import *


def inc_offset_2D(x, z):
    vs.inc_offset(x, 0, z)

def dec_offset_2D(x, z):
    vs.dec_offset(x, 0, z)

def set_offset_2D(x, z):
    vs.offset = (x, 0, z)

def line_xz(point_1, point_2, brick):
    vs.line_XZ(point_1, point_2, brick)