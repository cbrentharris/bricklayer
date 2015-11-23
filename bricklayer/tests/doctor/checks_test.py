from bricklayer.doctor.checks import Checker
from bricklayer.doctor.constants import HelpMessages
from bricklayer.utils.logger import Logger
from unittest import TestCase
import os
import sys
from StringIO import StringIO

class ChecksTest(TestCase):
    def test_executes_program(self):
        checker = Checker()
        filename = os.path.dirname(os.path.realpath(__file__)) + '/invalid_syntax.py'
        checker.check_program(filename)

    def test_it_prints_indentation_message_upon_indentation_error(self):
        checker = Checker()
        filename = os.path.dirname(os.path.realpath(__file__)) + '/invalid_indentation.py'
        out = StringIO()
        sys.stderr = out
        sys.stdout = out
        checker.check_program(filename)
        output = out.getvalue().strip()
        self.assertTrue(HelpMessages.BAD_INDENTATION in output)
        
        
