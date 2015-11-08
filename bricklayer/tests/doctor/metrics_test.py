from unittest import TestCase
from bricklayer.doctor.metrics import Metrics
import os

class MetricsTest(TestCase):
    def test_it_collects_metrics(self):
        m = Metrics()
        filename = os.path.dirname(os.path.realpath(__file__)) + '/simple_module.py'
        m.collect_metrics(filename)

