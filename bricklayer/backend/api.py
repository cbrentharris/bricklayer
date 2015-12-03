u"""

The backend API is used to collect user metrics

"""
from bricklayer.backend.settings import BRICKLAYER_API_METRICS_ENDPOINT
import requests
import responses

class BackendApi(object):

    @staticmethod
    def post_metrics(**metrics):
        requests.post(BRICKLAYER_API_METRICS_ENDPOINT, data=metrics)


class BackendApiMock(object):
    
    @staticmethod
    @responses.activate
    def post_metrics(**metrics):
        REQUIRED_KEYS = ['level', 'filename', 'source_lines_of_code', 'cyclomatic_complexity']
        missing_keys = set(REQUIRED_KEYS) - set(metrics.keys())
        error_json = {}
        if len(missing_keys) > 0:
            responses.add(responses.POST, BRICKLAYER_API_METRICS_ENDPOINT, body={'error' : 'Missing keys -- {}'.format(','.join(missing_keys))}, status=400, content_type='application/json')
            return requests.post(BRICKLAYER_API_METRICS_ENDPOINT, data=metrics)
        else:
            responses.add(responses.POST, BRICKLAYER_API_METRICS_ENDPOINT, status=200, content_type="application/json")
            return requests.post(BRICKLAYER_API_METRICS_ENDPOINT, data=metrics)
            
