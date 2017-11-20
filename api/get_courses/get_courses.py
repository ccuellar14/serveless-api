import os
import json
import boto3

import logging
log = logging.getLogger()
log.setLevel(logging.DEBUG)

def get_courses_handler(event):
    body = {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "input": event
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response