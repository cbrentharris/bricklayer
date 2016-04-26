u"""

The backend API is used to collect user metrics

"""
from bricklayer.doctor.config import Configurator
import requests
import responses


class BackendApi(object):
    @classmethod
    def post_metrics(cls, **metrics):
        requests.post(cls.metrics_endpoint(), data=metrics)

    @staticmethod
    def metrics_endpoint():
        return "http://{}/metrics/{}".format(Configurator.get("hostname"), Configurator.get("uuid"))


class BackendApiMock(object):
    @staticmethod
    @responses.activate
    def post_metrics(**metrics):
        REQUIRED_KEYS = ['level', 'filename', 'source_lines_of_code', 'cyclomatic_complexity']
        missing_keys = set(REQUIRED_KEYS) - set(metrics.keys())
        error_json = {}
        if len(missing_keys) > 0:
            responses.add(responses.POST, "http://localhost",
                          body={'error': 'Missing keys -- {}'.format(','.join(missing_keys))}, status=400,
                          content_type='application/json')
            return requests.post("http://localhost", data=metrics)
        else:
            responses.add(responses.POST, "http://localhost", status=200, content_type="application/json")
            return requests.post("http://localhost", data=metrics)
