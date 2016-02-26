from bricklayer.doctor.config import Configurator
BRICKLAYER_API_METRICS_ENDPOINT = Configurator.get('General', 'hostname') + "/metrics/" + Configurator.get_uuid()
