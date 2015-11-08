from bricklayer.doctor.checks import Checker
from unittest import TestCase
import os

class ChecksTest(TestCase):
    def test_executes_program(self):
        checker = Checker()
        filename = os.path.dirname(os.path.realpath(__file__)) + '/invalid_syntax.py'
        checker.check_program(filename)
        
