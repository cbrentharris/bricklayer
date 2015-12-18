from unittest import TestCase
from bricklayer.doctor.metrics import Metrics
import os

class MetricsTest(TestCase):

    def setUp(self):
        self.metrics = Metrics()
        filename = os.path.dirname(os.path.realpath(__file__)) + '/simple_module.py'
        self.metrics.collect_metrics(filename)

    def test_it_collects_complexity(self):
        self.assertEqual(self.metrics.cyclomatic_complexity, 2)

    def test_it_collects_sloc(self):
        self.assertEqual(self.metrics.source_lines_of_code, 6)

    def test_it_collects_user_defined_functions(self):
        self.assertEqual(self.metrics.user_defined_functions, 1)

    def test_it_collects_comments(self):
        self.assertEqual(self.metrics.comments, 1)

    def test_it_collects_the_program_name(self):
        self.assertEqual(self.metrics.program_name,  os.path.dirname(os.path.realpath(__file__)) + '/simple_module.py')

    def test_it_collects_the_bricklayer_level(self):
        self.assertEqual(self.metrics.level, 1)


