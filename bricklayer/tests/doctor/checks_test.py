from bricklayer.doctor.checks import Checker
from bricklayer.doctor.constants import HelpMessages
from bricklayer.utils.logger import Logger
from unittest import TestCase
import os
import sys
import logging
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
        Logger.addHandler(logging.StreamHandler(out))
        checker.check_program(filename)
        output = out.getvalue()
        self.assertTrue(HelpMessages.BAD_INDENTATION in output)

    def test_it_prints_correct_function_name_upon_value_error(self):
        checker = Checker()
        filename = os.path.dirname(os.path.realpath(__file__)) + '/function_missing.py'
        out = StringIO()
        Logger.addHandler(logging.StreamHandler(out))
        checker.check_program_isnt_mispelling_functions(filename)
        output = out.getvalue()
        self.assertTrue(HelpMessages.INCORRECT_FUNCTION_NAME.format("my_funciton", ["my_function"]) in output)

    def test_it_collects_all_the_user_defined_functions(self):
        checker = Checker()
        filename = os.path.dirname(os.path.realpath(__file__)) + '/function_missing.py'
        user_defined_functions = checker.collect_user_defined_functions(filename)
        self.assertEqual(user_defined_functions, ['my_function'])

    def test_it_collects_all_available_functions_from_import(self):
        checker = Checker()
        filename = os.path.dirname(os.path.realpath(__file__)) + '/import_from.py'
        available_functions = checker.collect_available_functions(filename)
        self.assertIn('put_2D_2x2_RED', available_functions)


        
