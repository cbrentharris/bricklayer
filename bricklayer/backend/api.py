u"""

The backend API is used to collect user metrics

"""
from bricklayer.backend.settings import BRICKLAYER_API_ENDPOINT
import requests

class BackendApi(object):

    def __init__(self, **metric_kwargs):
        self.metrics = metric_kwargs

    def post_metrics(self):
        requests.post(BRICKLAYER_API_ENDPOINT, data=self.metrics)

