from bricklayer.doctor.classifier import Classifier
from unittest import TestCase

class ClassifierTest(TestCase):

    def test_it_classifies(self):
        Classifier.score('/path/to/stats.csv')
        self.assertTrue(False)