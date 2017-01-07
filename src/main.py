from __future__ import print_function

import sys
import boto3
import json
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

client = boto3.client('cognito-identity')

def lambda_handler(event, context):
    if "add" in event:
        return add(event["add"])
    if "remove" in event:
        return remove(event["remove"])
    if "merge" in event:
        return merge(event["merge"])
    raise Exception("No request")

def add(params):
    logger.info("Adding: " + str(params))
    return client.get_open_id_token_for_developer_identity(**params)

def remove(params):
    logger.info("Removing: " + str(params))
    return client.unlink_developer_identity(**params)

def merge(params):
    logger.info("Merging: " + str(params))
    return client.merge_developer_identities(**params)
