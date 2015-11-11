from bricklayer.space import constants
from bricklayer.pieces.enums import Dimensions 
from jinja2 import Environment, PackageLoader
from collections import OrderedDict
import math

class Coordinate:

    def __init__(self, coords, brick=None):
        self.coords = coords
        self.brick = brick

    def __hash__(self):
        return hash(self.coords)

    def __str__(self):
        x = self.coords[0] * Dimensions.BRICK_WIDTH
        y = self.coords[1] * Dimensions.BRICK_HEIGHT
        z = self.coords[2] * Dimensions.BRICK_WIDTH
        return ','.join(map(str, [x,y,z]))

    def __unicode_(self):
        return str(self)

    def __repr__(self):
        return str(self)


class VirtualSpace:

    def __init__(self, size):
        self.size = size
        self.coords = {}
        self.origin = (0,0,0)
        self.upper_bounds = size

    def in_bounds(self, x, y, z):
        _x, _y, _z = self.virtual_cube_size
        return all([x < _x, y < _y, z < _z])

    def add_brick(self, point, brick):
        if not self.origin <= point or not self.upper_bounds >= point:
            return
        if point not in self.coords:
            coord = Coordinate(point, brick=brick)
            self.coords[point] = coord
        else:
            self.coords[point].brick = brick

    def traverse(self, function):
        starting_point = (0,0,0)
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
        for x in range(x1, x2+1):
            for y in range(y1, y2+1):
                for z in range(z1, z2 + 1):
                    update_function(x, y, z)

    def line(self, point_1, point_2, brick):
        x1, y1, z1 = point_1
        x2, y2, z2 = point_2
        while any([x1 < x2, y1 < y2, z1 < z2]):
            self.add_brick((x1, y1, z1), brick)
            x1 += 1 if x1 < x2 else 0
            y1 += 1 if y1 < y2 else 0
            z1 += 1 if z1 < z2 else 0

    def cylinder(self, radius, height, brick, x_center=0, z_center=0):
        while radius > 0:
            self.hollow_cylinder(radius, height, brick, x_center=x_center, z_center=z_center)
            radius -= 1

    def hollow_cylinder(self, radius, height, brick, x_center=0, z_center=0):
        for i in range(height+1):
            self.circle(radius, brick, x_center=x_center, z_center=z_center, y_offset=i)

    def circle(self, radius, brick, x_center=0, z_center=0, y_offset=0):
        theta = 0
        while theta <= 2 * math.pi:
            x = x_center + radius * math.cos(theta)
            z = z_center + radius * math.sin(theta)
            self.add_brick((x,y_offset,z), brick)
            theta += 2* math.pi / (45 * float(radius) / 11)

    def fill(self, point_1, point_2, brick):
        x1, y1, z1 = point_1
        x2, y2, z2 = point_2
        for i in range(x1, x2):
            for j in range(y1, y2):
                for k in range(z1, z2):
                    self.add_brick((i,j,k), brick)

    def output_to_file(self, filename):
        with open(filename, 'w') as outfile:
            env = Environment(loader=PackageLoader('bricklayer', 'templates'))
            template = env.get_template('output.lxfml')
            outfile.write(template.render(coords=self.coords.values()))

        
