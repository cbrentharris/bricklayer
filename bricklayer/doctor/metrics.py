"""

This module is intented to allow the doctor to collect stats about a users program.
Examples include:
    * Cyclomatic Complexity
	* SLOC
	* Comments

"""
import ast
import radon

class Metrics(object):
    
	def collect_metrics(self, program_name):
	    program_file = open(program_name, 'r')
		code = program_file.read()
	    cc_response = radan.complexity.cc_visit(code)
		raw_response = radon.raw.analyze(code)


