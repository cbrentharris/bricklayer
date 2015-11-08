"""

The point of this module is to run a series of tests on the bricklayer program passed,
so that the end user can be alerted if there are some issues happening

"""

import ast
import subprocess

class Checker(object):

    def check_program(self, program_name):
        self.check_program_can_be_executed(program_name)
        self.check_program_is_using_appropriate_constructs(program_name)

    def check_program_can_be_executed(self, program_name):
        subprocess.call(program_name)

    def check_program_is_using_appropriate_constrcuts(self, program_name):
        pass
        
