from bricklayer.space import constants
from bricklayer.utils.helpers import coordinate_to_string
from jinja2 import Environment, PackageLoader
from collections import OrderedDict
import logging
logger = logging.getLogger('bricklayer')

class ThreeDimensionalPoint:
    
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def area(self):
        return self.x * self.y * self.z

    def unpack(self):
        return (self.x, self.y, self.z)


class Coordinate:

    def __init__(self, shift, value, delta, size):
        self.shift = shift
        self.value = value
        self.delta = delta
        self.size = size

    def __iter__(self):
        return self

    def next(self):
        if self.size == 0:
            raise StopIteration
        self.size -= 1
        self.value *= self.shift
        result = self.value + self.delta
        self.shift *= self.delta_shift(self.value, result)
        return (self.shift, self.round(result, self.shift))

    def delta_shift(self, smaller, larger):
        return 10 if len(str(smaller)) != len(str(larger)) else 1

    def round(self, result, shift):
        quotient, remainder = divmod(result, shift)
        return quotient + 1 if remainder > 5 else quotient


class VirtualSpace:

    def __init__(self):
        self.virtual_cube_size = None 
        self.origin = None
        self.offset = None

    def in_bounds(self, x, y, z):
        _x, _y, _z = self.virtual_cube_size
        return all([x < _x, y < _y, z < _z])

    def build_cube(self, three_d_point):
        if self.virtual_cube_size is not None:
            raise Exception("Oops, the virtual space has already been built!")
        if three_d_point.area() > constants.MAX_VIRTUAL_CUBE_AREA:
            logger.warn("You are attempting to build a large virtual space.")
            logger.warn("Your program may be terminated.")
        
        self.virtual_cube_size = three_d_point.unpack()
        x, y, z = three_d_point.unpack()
        self.origin = (0, 0, 0)
        self.upper_bounds = (x, y, z)
        self.offset = (0, 0, 0)
        x_coords = self.coordinate_list(x, constants.START_X, constants.DELTA_X) 
        y_coords = self.coordinate_list(y, constants.START_Y, constants.DELTA_Y) 
        z_coords = self.coordinate_list(z, constants.START_Z, constants.DELTA_Z) 
        self.coords = OrderedDict( ((k, j, i), { 'ldd_coordinate' :  (x_coords[k], y_coords[j], z_coords[i]), 'brick' :  None }) for i in range(len(z_coords)) for j in range(len(y_coords)) for k in range(len(x_coords)) )
                
    def coordinate_list(self, size, start, delta):
        return [c for c in Coordinate(1, start, delta, size)]

    def traverse(self, function):
        starting_point = (0,0,0)
        ending_point = None
        def update_function(point):
            new_brick = function(point)
            self.update(point, new_brick)
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

    def update(self, brick, coordinate):
        if not self.origin <= coordinate or not self.upper_bounds >= coordinate:
            return
        self.coords[coordinate]['brick'] = brick

    def line(self):
        pass

    def weft(self, pattern, starting_point, ending_point, func):
        pass

    def output_to_file(self, filename):
        with open(filename, 'w') as outfile:
            env = Environment(loader=PackageLoader('bricklayer', 'templates'))
            env.globals['coordinate_to_string'] = coordinate_to_string
            template = env.get_template('output.lxfml')
            outfile.write(template.render(coords=self.coords))

        

   #NOTES :: init 3d array with empty bricks. What is the gen all about?
   #TODO: add self.origin, self.upper_bounds
