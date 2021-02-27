import json
import logging
import sys
from datetime import datetime

response = {'AttributeDefinitions':
    [
        {'AttributeName': 'id', 'AttributeType': 'S'},
        {'AttributeName': 'linkReference', 'AttributeType': 'S'}
    ],
    'TableName': 'kat-dev-alerter-db',
    'KeySchema': [{'AttributeName': 'id', 'KeyType': 'HASH'}],
    'TableStatus': 'ACTIVE',
    'CreationDateTime': '',
    'ProvisionedThroughput': {'NumberOfDecreasesToday': 0, 'ReadCapacityUnits': 0, 'WriteCapacityUnits': 0},
    'TableSizeBytes': 67479463,
    'ItemCount': 77302,
    'TableArn': 'arn:aws:dynamodb:eu-west-1:248762759038:table/kat-dev-alerter-db',
    'TableId': '84c7122e-df64-42c2-adf4-adc4557acd9d',
    'BillingModeSummary': {'BillingMode': 'PAY_PER_REQUEST', 'LastUpdateToPayPerRequestDateTime': ''},
    'GlobalSecondaryIndexes': [{'IndexName': 'linkReferenceIndex',
                                'KeySchema': [{'AttributeName': 'linkReference', 'KeyType': 'HASH'}],
                                'Projection': {'ProjectionType': 'ALL'},
                                'IndexStatus': 'ACTIVE',
                                'ProvisionedThroughput': {'LastDecreaseDateTime': '',
                                                          'NumberOfDecreasesToday': 0, 'ReadCapacityUnits': 0,
                                                          'WriteCapacityUnits': 0},
                                'IndexSizeBytes': 67479463,
                                'ItemCount': 77302,
                                'IndexArn': 'arn:aws:dynamodb:eu-west-1:248762759038:table/kat-dev-alerter-db/index/linkReferenceIndex'}]}

response1_DeleteMeTable = {'AttributeDefinitions':
                               [{'AttributeName': 'del_id', 'AttributeType': 'S'}],
                           'TableName': 'deleteme',
                           'KeySchema': [{'AttributeName': 'del_id', 'KeyType': 'HASH'}],
                           'TableStatus': 'ACTIVE',
                           'CreationDateTime': 'datetime.datetime(2021, 2, 9, 13, 6, 56, 248000, tzinfo=tzlocal())',
                           'ProvisionedThroughput': {'NumberOfDecreasesToday': 0, 'ReadCapacityUnits': 5,
                                                     'WriteCapacityUnits': 5},
                           'TableSizeBytes': 0,
                           'ItemCount': 0,
                           'TableArn': 'arn:aws:dynamodb:eu-west-1:248762759038:table/deleteme',
                           'TableId': 'd7e87039-be49-46f9-9fe6-7a0ebd3c7182',
                           'SSEDescription': {'Status': 'ENABLED', 'SSEType': 'KMS',
                                              'KMSMasterKeyArn': 'arn:aws:kms:eu-west-1:248762759038:key/01467fea-5153-4627-87de-59dfad0c2cfc'}}

# Table name
print(response['TableName'])
# Item Count
print(response1_DeleteMeTable['ItemCount'])
# Ensure that your Amazon DynamoDB tables are using AWS-managed Customer Master Keys (CMKs) instead of
# AWS-owned CMKs for Server-Side Encryption (SSE), in order to meet strict encryption compliance and
# regulatory requirements.
if 'SSEDescription' in response1_DeleteMeTable:
    if ('SSEType') in response1_DeleteMeTable['SSEDescription']:
        if response1_DeleteMeTable['SSEDescription']['SSEType'] == 'KMS' and response1_DeleteMeTable['SSEDescription'][
            'Status'] == 'ENABLED':
            print(response1_DeleteMeTable['SSEDescription']['SSEType'])
            print(response1_DeleteMeTable['SSEDescription']['KMSMasterKeyArn'])
else:
    print('Wah wah wa')
