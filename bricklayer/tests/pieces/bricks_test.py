from unittest import TestCase
from bricklayer.pieces.enums import *
from bricklayer.pieces.bricks import Brick

class BricksTest(TestCase):
    u""""
    Tests for the bricks class representation of the bricklayer internal bricks
    """

    def test_default_orientation_is_normal(self):
        brick = Brick(Color.RED, Shape.BIT)
        self.assertEqual(brick.orientation(), '1.0,0.0,0.0,0.0,1.0,0.0,0.0,0.0,1.0')
