"""

The point of this module is to run a series of tests on the bricklayer program passed,
so that the end user can be alerted if there are some issues happening

"""

import ast
import subprocess
import py_compile
import importlib
from bricklayer.utils.logger import Logger
from bricklayer.doctor.constants import HelpMessages
from bricklayer.doctor.ast_visitors import * 
from difflib import get_close_matches

class Checker(object):

    def check_program(self, program_name):
        can_be_compiled = self.check_program_can_be_compiled(program_name)
        if can_be_compiled:
            self.check_program_is_using_appropriate_constructs(program_name)

    def check_program_can_be_compiled(self, program_name):
        try:
            py_compile.compile(program_name, doraise=True)
            return True
        except py_compile.PyCompileError as e:
            if "IndentationError" in str(e):
                Logger.debug(HelpMessages.BAD_INDENTATION)
            else:
                Logger.debug(e)
            return False

    def check_program_isnt_mispelling_functions(self, program_name):
        user_defined_functions = self.collect_user_defined_functions(program_name)
        available_functions = self.collect_available_functions(program_name)
        called_functions = self.collect_called_functions(program_name)
        for func in called_functions:
            if func in user_defined_functions + available_functions:
                continue
            closest_matches = get_close_matches(func, user_defined_functions + available_functions)
            Logger.debug(HelpMessages.INCORRECT_FUNCTION_NAME.format(func, closest_matches))

    def check_program_is_using_appropriate_constructs(self, program_name):
        pass
        
    @staticmethod
    def collect_user_defined_functions(program_name):
        v = UserDefinedFunctionVisitor()
        program_file = open(program_name, 'r')
        code = program_file.read()
        v.visit(ast.parse(code))
        return v.functions

    @staticmethod
    def collect_available_functions(program_name):
        v = ImportedModuleVisitor()
        program_file = open(program_name, 'r')
        code = program_file.read()
        v.visit(ast.parse(code))
        available_functions = dir(__builtins__)
        for _import, _from in v.imports:
            try:
                if _from:
                    # It might be a function, constant, etc being imported, so we need
                    # to check
                    try:
                        available_functions += dir(importlib.import_module('.' + _import, package=_from))
                    except ImportError:
                        # Might be a function, constant, etct
                        m = importlib.import_module(_from)
                        f = getattr(m, _import)
                        if f is not None and hasattr(f, '__call__'):
                            available_functions.append(_import)
                else:
                    available_functions += dir(importlib.import_module(_import))
            except ImportError:
                pass
        return available_functions

    @staticmethod
    def collect_called_functions(program_name):
        v = CalledFunctionVisitor()
        program_file = open(program_name, 'r')
        code = program_file.read()
        v.visit(ast.parse(code))
        return v.functions
        
