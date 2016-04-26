from unittest import TestCase
from bricklayer.space.virtual_space import Coordinate, VirtualSpace
from bricklayer.utils.bricklayer_exceptions import OutOfBoundsException
from bricklayer.pieces.bricks import RED_BRICK, BLACK_BRICK


class CoordinateTest(TestCase):
    def test_it_creates_the_correct_string_representation(self):
        c = Coordinate((0, 0, 0))
        self.assertEqual(str(c), "0.0,0.0,0.0")


class VirtualSpaceTest(TestCase):
    def test_it_doesnt_add_a_brick_outside_the_bounds(self):
        upper_bounds = (10, 10, 10)
        vs = VirtualSpace(upper_bounds)
        with self.assertRaises(OutOfBoundsException):
            vs.add_brick((11, 111, 11), RED_BRICK)

    def test_it_inc_and_decs_the_offset(self):
        upper_bounds = (10, 10, 10)
        vs = VirtualSpace(upper_bounds)
        vs.inc_offset(1, 0, 1)
        self.assertEqual((1, 0, 1), vs.offset)
        vs.dec_offset(1, 0, 0)
        self.assertEqual((0, 0, 1), vs.offset)

    def test_it_uses_the_offset(self):
        # With no offset, we should have 1 to 1 mapping of coordinates
        upper_bounds = (10, 10, 10)
        vs = VirtualSpace(upper_bounds)
        vs.add_brick((1, 1, 1), RED_BRICK)
        self.assertTrue((1, 1, 1) in vs.coords)
        vs.inc_offset(1, 1, 1)
        vs.add_brick((1, 1, 1), BLACK_BRICK)
        self.assertEqual(vs.coords[(1, 1, 1)].brick, RED_BRICK)
        self.assertTrue((2, 2, 2) in vs.coords)
        self.assertEqual(vs.coords[(2, 2, 2)].brick, BLACK_BRICK)
