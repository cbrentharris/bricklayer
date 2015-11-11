from unittest import TestCase
from bricklayer.doctor.metrics import Metrics
import os

class MetricsTest(TestCase):
    def test_it_collects_complexity(self):
        m = Metrics()
        filename = os.path.dirname(os.path.realpath(__file__)) + '/simple_module.py'
        m.collect_metrics(filename)
        self.assertEqual(m.cc_response[0].complexity, 2)

    def test_it_collects_sloc(self):
        m = Metrics()
        filename = os.path.dirname(os.path.realpath(__file__)) + '/simple_module.py'
        m.collect_metrics(filename)
        self.assertEqual(m.raw_response.sloc, 5)

    def test_it_collects_user_defined_functions(self):
        m = Metrics()
        filename = os.path.dirname(os.path.realpath(__file__)) + '/simple_module.py'
        m.collect_metrics(filename)
        self.assertEqual(m.user_defined_functions, 1)

    def test_it_collects_comments(self):
        m = Metrics()
        filename = os.path.dirname(os.path.realpath(__file__)) + '/simple_module.py'
        m.collect_metrics(filename)
        self.assertEqual(m.raw_response.comments, 1)

