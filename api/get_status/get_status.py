import os
import json

import logging
log = logging.getLogger()
log.setLevel(logging.DEBUG)

def get_status_handler(event):
    
    return {'response': 'This root API'}