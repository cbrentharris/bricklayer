from bricklayer.doctor.config import Configurator
BRICKLAYER_API_BASE_ENDPOINT = "http://TODO"
BRICKLAYER_API_METRICS_ENDPOINT = BRICKLAYER_API_BASE_ENDPOINT + "/metrics" + Configurator.get_uuid()
