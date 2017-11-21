import json
import logging
from api.get_status.get_status import get_status_handler

log = logging.getLogger()
log.setLevel(logging.DEBUG)

def main(event, context):
    log.debug("Received event {}".format(json.dumps(event)))
    return get_status_handler(event)