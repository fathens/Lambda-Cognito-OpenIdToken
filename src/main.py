from __future__ import print_function

import sys
import boto3
import json
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    if "add" in event:
        return add(event["add"])
    if "remove" in event:
        return remove(event["remove"])
    raise Exception("No request")

def add(params):
    logger.info("Adding: " + params)
    return "Added"
    
def remove(params):
    logger.info("Removing: " + params)
    return "Removed"
