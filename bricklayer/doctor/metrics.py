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
        cc_response = cc_visit(code)
        raw_response = analyze(code)
        if cc_response:
            self.cyclomatic_complexity = cc_response[0].complexity
        if raw_response:
            self.source_lines_of_code = raw_response.sloc
            self.comments = raw_response.comments
        self.user_defined_functions = self.collect_user_defined_functions(code)
        self.program_name = program_name

    def collect_user_defined_functions(self, code):
        parsed = ast.parse(code)
        return len([node for node in parsed.body if isinstance(node, ast.FunctionDef)])

