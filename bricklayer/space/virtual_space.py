import constants

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
        actual_vlue = value * shift
        result = actual_value + delta
        new_shift = shift * self.delta_shift(actual_value, result)
        return (new_shift, self.round(result, new_shift))

    def delta_shift(self, smaller, larger):
        return 1- if len(str(smaller)) != len(str(larger)) else 1

    def round(self, result, shift):
        quotient, remainder = divmod(result, shift)
        return quotient + 1 if remainder > 5 else quotient


class VirtualSpace:

    def __init__(self):
        self.virtual_cube_size = None 

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
        x_coords = self.coordinate_list(x, constants.START_X, constants.DELTA_X) 
        y_coords = self.coordinate_list(y, constants.START_Y, constants.DELTA_Y) 
        z_coords = self.coordinate_list(z, constants.START_Z, constants.DELTA_Z) 
        self.coords = [(_x, _y, _z) for _x in x_coords for _y in y_coords for _z in z_coords]
         
    def bounds_are_safe(self, three_d_point_a, three_d_point_b):
        x_bounds, y_bounds, z_bounds = self.virtual_cube_size
        x1, y1, z1 = three_d_point_a.unpack()
        x2, y2, z2 = three_d_point_b.unpack()
        return all([
            x1 <= x2,
            y1 <= y2,
            z1 <= z2,
            0 <= x1 <= x_bounds,
            0 <= x2 <= x_bounds,
            0 <= y1 <= y_bounds,
            0 <= y2 <= y_bounds,
            0 <= z1 <= z_bounds,
            0 <= z2 <= z_bounds,
        ])

    def coordinate_list(self, size, start, delta):
        return [c for c in Coordinates(1, start, delta, shift)]

    def output_to_file(self, filename):
        with open(filename, 'w') as outfile:
            #get refID
            # 
        

   #NOTES :: init 3d array with empty bricks. What is the gen all about?
