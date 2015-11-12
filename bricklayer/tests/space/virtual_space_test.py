from unittest import TestCase
from bricklayer.space.virtual_space import Coordinate, VirtualSpace
from bricklayer.utils.bricklayer_exceptions import OutOfBoundsException
from bricklayer.pieces.bricks import RED_BRICK

class CoordinateTest(TestCase):
    
    def test_it_creates_the_correct_string_representation(self):
        c = Coordinate((0,0,0))
        self.assertEqual(str(c), "0.0,0.0,0.0")


class VirtualSpaceTest(TestCase):
    
    def test_it_doesnt_add_a_brick_outside_the_bounds(self):
        upper_bounds = (10, 10, 10)
        vs = VirtualSpace(upper_bounds)
        with self.assertRaises(OutOfBoundsException):
            vs.add_brick((11,111,11), RED_BRICK)
        
