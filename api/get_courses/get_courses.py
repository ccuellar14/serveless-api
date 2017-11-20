import os
import json

import logging
log = logging.getLogger()
log.setLevel(logging.DEBUG)

def get_courses_handler(event):
    # Your code goes here!
    e = event.get('e')
    pi = event.get('pi')

    response = {
        'body': e + pi
    }

    return response