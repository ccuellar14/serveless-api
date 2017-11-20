import os
import json
import boto3

import logging
log = logging.getLogger()
log.setLevel(logging.DEBUG)

def get_courses_handler(event):
    # Your code goes here!
    e = event.get('e')
    pi = event.get('pi')
    return {
        "statusCode": 200,
        "headers": { "Content-Type": "application/json"},
        "body": e + pi
    }