import ast
from unittest import TestCase
from bricklayer.doctor.ast_visitors import *

class AstVisitorsTest(TestCase):

    def test_it_gets_all_user_defined_functions(self):
        code = """
def my_function():
    print 'hello'
        """
        v = UserDefinedFunctionVisitor()
        v.visit(ast.parse(code))
        self.assertEqual(v.functions, ['my_function'])

    def test_it_gets_all_imports(self):
        code = """
from bricklayer.levels import level_1
import bricklayer.levels.level_2
        """
        v = ImportedModuleVisitor()
        v.visit(ast.parse(code))
        self.assertEqual(v.imports, ['level_1', 'bricklayer.levels.level_2'])

    def test_it_gets_all_called_functions(self):
        code = """
f('hello')
x(123)
        """
        v = CalledFunctionVisitor()
        v.visit(ast.parse(code))
        self.assertEqual(v.functions, ['f', 'x'])

    
        
        

