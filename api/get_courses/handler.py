import json
import logging
from api.get_courses.get_courses import get_courses_handler


log = logging.getLogger()
log.setLevel(logging.DEBUG)

def main(event, context):
    log.debug("Received event {}".format(json.dumps(event)))
    return get_courses_handler(event)