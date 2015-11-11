"""

This module is intented to allow the doctor to collect stats about a users program.
Examples include:
    * Cyclomatic Complexity
    * SLOC
    * Comments

"""
from radon.complexity import cc_visit
from radon.raw import analyze
from bricklayer.utils.logger import Logger
from bricklayer.doctor.constants import *
import ast

class Metrics(object):
    
    def collect_metrics(self, program_name):
        program_file = open(program_name, 'r')
        code = program_file.read()
        self.cc_response = cc_visit(code)
        self.raw_response = analyze(code)
        self.user_defined_functions = self.collect_user_defined_functions(code)

    def collect_user_defined_functions(self, code):
        parsed = ast.parse(code)
        return len([node for node in parsed.body if isinstance(node, ast.FunctionDef)])


