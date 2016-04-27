from bricklayer.pieces.enums import Dimensions
from bricklayer.utils.bricklayer_exceptions import OutOfBoundsException
from jinja2 import Environment, PackageLoader
from math import sin, cos, atan2, pi
from numpy import matrix
import copy


class Coordinate:
    u"""
    A class used to define a coordinate within the virtual space. It's simply made up of
    an x, y, and z coordinate plus a bricklayer brick
    """

    def __init__(self, coords, brick=None):
        self.coords = coords
        self.brick = brick

    def __hash__(self):
        return hash(self.coords)

    def __str__(self):
        x = self.coords[0] * Dimensions.BRICK_WIDTH
        y = self.coords[1] * Dimensions.BRICK_HEIGHT
        z = self.coords[2] * Dimensions.BRICK_WIDTH
        return ','.join(map(str, [x, y, z]))

    def __unicode_(self):
        return str(self)

    def __repr__(self):
        return str(self)


class VirtualSpace:
    u"""
    This is the in memory representation of the Lego 3D space that will eventually be output
    to a flat custom XML file
    """

    def __init__(self, size):
        self.size = size
        self.coords = {}
        self.origin = (0, 0, 0)
        self.offset = (0, 0, 0)
        self.rotation_matrices = []
        self.upper_bounds = size

    def in_bounds(self, *point):
        return all([i1 <= i2 for i1, i2 in zip(self.origin, point) + zip(point, self.upper_bounds)])

    def add_brick(self, point, brick, already_offset=False):
        if already_offset:
            point_with_offset = point
        else:
            point_with_offset = tuple(a + b for a, b in zip(point, self.offset))

        if not self.in_bounds(*point_with_offset):
            error_message = "The point {} that you tried to use it outside the bounds defined in the virtual space.\nUpper bounds : {}.\nLower Bounds : {}.".format(
                point_with_offset, self.upper_bounds, self.origin)
            raise OutOfBoundsException(error_message)

        if len(self.rotation_matrices) > 0:
            brick = copy.deepcopy(brick)
            for matrix in self.rotation_matrices:
                brick.update_rotation_matrix(matrix)
        if point_with_offset not in self.coords:
            coord = Coordinate(point_with_offset, brick=brick)
            self.coords[point_with_offset] = coord
        else:
            self.coords[point_with_offset].brick = brick

    def traverse(self, function):
        starting_point = (0, 0, 0)
        ending_point = None

        def update_function(point):
            new_brick = function(point)
            self.add_brick(point, new_brick)

        self.safe_traverse(starting_point, ending_point, update_function)

    def safe_traverse(self, p1, p2, update_function):
        x1, y1, z1 = p1
        x2, y2, z2 = p2
        if not all([x1 <= x2, y1 <= y2, z1 <= z2]):
            return
        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                for z in range(z1, z2 + 1):
                    update_function(x, y, z)

    def line_xz(self, point_1, point_2, brick):
        x1, z1 = tuple(a + b for a, b in zip(point_1, self.offset))
        x2, z2 = tuple(a + b for a, b in zip(point_2, self.offset))
        delta_x = abs(x2 - x1)
        delta_z = abs(z2 - z1)
        theta = atan2(delta_x, delta_z)
        while any([x1 < x2, z1 < z2]):
            self.add_brick((x1, 0, z1), brick, already_offset=True)
            if abs(theta - pi / 4) < .01:
                x_offset = 1
                z_offset = 1
            elif theta > pi / 4:
                x_offset = 1
                z_offset = 1 * cos(theta)
            else:
                x_offset = 1 * sin(theta)
                z_offset = 1
            x1 += x_offset if x1 < x2 else 0
            z1 += z_offset if z1 < z2 else 0

    def smooth_line_xz(self, point_1, point_2, brick):
        x1, z1 = tuple(a + b for a, b in zip(point_1, self.offset))
        x2, z2 = tuple(a + b for a, b in zip(point_2, self.offset))
        delta_x = x2 - x1
        delta_z = z2 - z1
        theta = atan2(delta_x, delta_z)
        self.rotation_matrices.append(RotationMatrix.rotate_Y(-theta))
        while any([x1 < x2, z1 < z2]):
            self.add_brick((x1, 0, z1), brick, already_offset=True)
            x1 += 1 * sin(theta) if x1 < x2 else 0
            z1 += 1 * cos(theta) if z1 < z2 else 0
        self.rotation_matrices.pop()

    def cylinder(self, radius, height, brick, x_center=0, z_center=0):
        while radius > 0:
            self.hollow_cylinder(radius, height, brick, x_center=x_center, z_center=z_center)
            radius -= 1

    def hollow_cylinder(self, radius, height, brick, x_center=0, z_center=0):
        for i in range(height + 1):
            self.circle(radius, brick, x_center=x_center, z_center=z_center, y_offset=i)

    def circle_xz(self, radius, brick, x_center=0, z_center=0, y_offset=0):
        theta = 0
        while theta <= 2 * pi:
            x = x_center + radius * cos(theta)
            z = z_center + radius * sin(theta)
            self.rotation_matrices.append(RotationMatrix.rotate_Y(theta))
            self.add_brick((x, y_offset, z), brick)
            self.rotation_matrices.pop()
            theta += 2 * pi / (45 * float(radius) / 11)

    def fill(self, point_1, point_2, brick):
        x1, y1, z1 = point_1
        x2, y2, z2 = point_2
        for i in range(x1, x2):
            for j in range(y1, y2):
                for k in range(z1, z2):
                    self.add_brick((i, j, k), brick)

    def output_to_file(self, filename):
        with open(filename, 'w') as outfile:
            env = Environment(loader=PackageLoader('bricklayer', 'templates'))
            template = env.get_template('output.lxfml')
            outfile.write(template.render(coords=self.coords.values()))

    def inc_offset(self, *new_offset):
        self.offset = tuple(x1 + x2 for x1, x2 in zip(self.offset, new_offset))

    def dec_offset(self, *new_offset):
        self.offset = tuple(x1 - x2 for x1, x2 in zip(self.offset, new_offset))


class RotationMatrix:
    """
    In Lego Digital Designer, each brick has a 3D rotation matrix applied to it.
    See https://en.wikipedia.org/wiki/Rotation_matrix for basic rotations
    """

    @staticmethod
    def rotate_X(theta):
        return matrix([
            [1, 0, 0],
            [0, cos(theta), -sin(theta)],
            [0, sin(theta), cos(theta)]
        ])

    @staticmethod
    def rotate_Y(theta):
        return matrix([
            [cos(theta), 0, sin(theta)],
            [0, 1, 0],
            [-sin(theta), 0, cos(theta)]
        ])

    @staticmethod
    def rotate_Z(theta):
        return matrix([
            [cos(theta), -sin(theta), 0],
            [sin(theta), cos(theta), 0],
            [0, 0, 1]
        ])
