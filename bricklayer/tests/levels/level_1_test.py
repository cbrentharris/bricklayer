from unittest import TestCase
from bricklayer.levels.level_1 import *
from bricklayer.pieces.enums import Color
from bricklayer.utils.logger import Logger

class Level1TestCase(TestCase):
    
    def test_1x1_function(self):
        put_2D_1x1_RED(0,0)
        self.assertEqual(vs.coords[(0,0,0)].brick.color, Color.RED)

    def test_1x1_function_updates(self):
        put_2D_1x1_RED(0,0)
        self.assertEqual(vs.coords[(0,0,0)].brick.color, Color.RED)
        put_2D_1x1_BLUE(0,0)
        self.assertEqual(vs.coords[(0,0,0)].brick.color, Color.BLUE)
        
        
