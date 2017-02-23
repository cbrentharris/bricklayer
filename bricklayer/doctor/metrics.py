"""

This module is intented to allow the doctor to collect stats about a users program.
Examples include:
    * Cyclomatic Complexity
    * SLOC
    * Comments

"""
from radon.complexity import cc_visit
from radon.raw import analyze
import ast


class Metrics(object):
    def collect_metrics(self, program_name):
        program_file = open(program_name, 'r')
        code = program_file.read()
        cc_response = cc_visit(code)
        raw_response = analyze(code)
        self.cyclomatic_complexity = None
        if cc_response:
            self.cyclomatic_complexity = cc_response[0].complexity
        self.source_lines_of_code = 0
        self.comments = 0
        if raw_response:
            self.source_lines_of_code = raw_response.sloc
            self.comments = raw_response.comments
        self.user_defined_functions = self.collect_user_defined_functions(code)
        self.program_name = program_name
        self.level = self.collect_level_being_used(code)

    def collect_user_defined_functions(self, code):
        parsed = ast.parse(code)
        return len([node for node in parsed.body if isinstance(node, ast.FunctionDef)])

    def collect_level_being_used(self, code):
        parsed = ast.parse(code)
        for node in parsed.body:
            if isinstance(node, ast.Import):
                for alias in node.names:
                    level = self.parse_level_or_none_from_module_string(alias.name)
                    if level is not None:
                        return level
            if isinstance(node, ast.ImportFrom):
                level = self.parse_level_or_none_from_module_string(node.module)
                if level is not None:
                    return level

    @staticmethod
    def parse_level_or_none_from_module_string(module_string):
        # Right now, the modules are like
        # from bricklayer.levels.level_x import ...
        try:
            # _, _, level = module_string.split('.')
            # assert 'level_' in level
            return int(module_string[-1])
        except:
            return None
