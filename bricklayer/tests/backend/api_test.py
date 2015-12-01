from unittest import TestCase
from bricklayer.backend.api import BackendApiMock

class BackendApiTest(TestCase):

    def test_it_posts_to_the_api_successfully_with_all_required_keys(self):
        metrics = {
            'level' : 1,
            'filename' : 'somefakefilename.py',
            'source_lines_of_code' : 201,
            'cyclomatic_complexity' : 1,
            'user_defined_functions' : 10
        }

        resp = BackendApiMock.post_metrics(**metrics)
        self.assertEqual(resp.status_code, 200)

