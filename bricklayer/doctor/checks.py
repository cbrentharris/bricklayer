"""

The point of this module is to run a series of tests on the bricklayer program passed,
so that the end user can be alerted if there are some issues happening

"""

import ast
import subprocess
import py_compile
from bricklayer.utils.logger import Logger

class Checker(object):

    def check_program(self, program_name):
        self.check_program_can_be_compiled(program_name)
        self.check_program_is_using_appropriate_constructs(program_name)

    def check_program_can_be_compiled(self, program_name):
        try:
            py_compile.compile(program_name, doraise=True)
        except py_compile.PyCompileError:
            Logger.debug("Oops, there was a compilation error!")

    def check_program_is_using_appropriate_constructs(self, program_name):
        pass
        
