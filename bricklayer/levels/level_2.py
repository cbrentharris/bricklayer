from level_1 import *
from bricklayer.space.virtual_space import RotationMatrix


def inc_offset_2D(x, z):
    vs.inc_offset(x, 0, z)


def dec_offset_2D(x, z):
    vs.dec_offset(x, 0, z)


def set_offset_2D(x, z):
    vs.offset = (x, 0, z)


def line_xz(point_1, point_2, brick):
    vs.line_xz(point_1, point_2, brick)


def smooth_line_xz(point_1, point_2, brick):
    vs.smooth_line_xz(point_1, point_2, brick)


def circle_xz(radius, brick, x_center=0, z_center=0, ):
    vs.circle_xz(radius, brick, x_center=x_center, z_center=z_center)


def rotate_X(theta):
    vs.rotation_matrices.append(RotationMatrix.rotate_X(theta))


def rotate_Y(theta):
    vs.rotation_matrices.append(RotationMatrix.rotate_Y(theta))


def rotate_Z(theta):
    vs.rotation_matrices.append(RotationMatrix.rotate_Z(theta))


def undo_rotation():
    vs.rotation_matrices.pop()


def reset_rotations():
    vs.rotation_matrices = []
