#################################################################################
# Lambda function to be used as custom AWS Config Rule for Dynamodb compliance.##
# The following SCB rules will be evaluated:                                   ##
#  - AWS KMS Customer Master Keys for Table Encryption(Details:Refer Readme)   ##
#################################################################################

import json
import logging
import sys
from datetime import datetime

import boto3

# initialize logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

handler = logging.StreamHandler(sys.stdout)
logger.addHandler(handler)

config = boto3.client('config')
client = boto3.client('dynamodb')
dynamodb = boto3.resource('dynamodb')


def lambda_handler(event, context):
    if "debug" in event:
        debug = event['debug']
    else:
        debug = False
    invoking_event = json.loads(event['invokingEvent'])
    invoking_time = datetime.strptime(invoking_event['notificationCreationTime'], '%Y-%m-%dT%H:%M:%S.%fZ')

    evaluations = []
    dynamodb_tables = list_dynamodb_tables()

    for tableName in dynamodb_tables:
        compliant = False
        logger.debug("DynamoDB Table found: {}".format(tableName))
        table = client.describe_table(TableName=tableName)
        key_to_lookup = 'SSEDescription'
        if key_to_lookup in table['Table']:
            if (table[key_to_lookup]['Status'] == 'ENABLED' and table['Table'][key_to_lookup]['SSEType'] == 'KMS'):
                logger.info("The DynamoDB Table {} is using AWS-managed Customer Master Keys (CMKs) {}".format(
                    table['Table']['TableName'],
                    ": and is Compliant "))
            compliant = True
        else:
            compliant = False
            logger.info(("The DynamoDB Table {} is NOT using AWS-managed Customer Master Keys (CMKs) {}".format(
                table['Table']['TableName'],
                ": and is Non-compliant ")))

            if compliant:
                logger.info("Table {} is compliant".format(tableName.attributes['TopicArn']))
                evaluation = {
                    'ComplianceResourceType': 'AWS::DynamoDB::Table',
                    'ComplianceResourceId': table['Table']['TableArn'],
                    'ComplianceType': 'COMPLIANT',
                    'OrderingTimestamp': invoking_time
                }
                evaluations.append(dict(evaluation))
            else:
                evaluation = {
                    'ComplianceResourceType': 'AWS::DynamoDB::Table',
                    'ComplianceResourceId': table['Table']['TableArn'],
                    'ComplianceType': 'NON_COMPLIANT',
                    'Annotation': 'The DynamoDB Table is unused in violation of rule AWS-DYNAMODB-PG-AWS-01',
                    'OrderingTimestamp': invoking_time
                }

        evaluations.append(dict(evaluation))

        if len(evaluations) == 0:
            logger.info("No Non-Encrypted Dynamodb tables found in the account")
        else:
            post_response(evaluations, event['resultToken'], debug)


# find all the dynamodb tables in the account
def list_dynamodb_tables():
    more_results = True
    dynamodb_tables = []
    next_table = ""
    while more_results:
        if not next_table:
            result = client.list_tables()
        else:
            result = client.list_tables(
                nextToken="{}".format(next_table)
            )
        dynamodb_tables = dynamodb_tables + result['TableNames']
        if 'LastEvaluatedTableName' not in result:
            more_results = False
        else:
            next_table = result['LastEvaluatedTableName']
    return dynamodb_tables


# Post the results of the check to AWS config
def post_response(evaluations, token, debug=False):
    logger.debug("posting results to AWS config")
    response = config.put_evaluations(
        Evaluations=evaluations,
        ResultToken=token,
        TestMode=debug
    )


# Local test
if __name__ == "__main__":
    event = {
        "resultToken": "testDebug",
        "invokingEvent": json.dumps({
            "notificationCreationTime": "1992-06-20T22:50:16.021Z",
        }),
        "debug": True
    }
    context = []
    lambda_handler(event, context)
