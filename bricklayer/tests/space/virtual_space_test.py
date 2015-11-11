from unittest import TestCase
from bricklayer.space.virtual_space import *

class CoordinateTest(TestCase):
    
    def test_it_creates_the_correct_string_representation(self):
        c = Coordinate((0,0,0))
        self.assertEqual(str(c), "0.0,0.0,0.0")
