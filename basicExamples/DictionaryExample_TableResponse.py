import json
import logging
import sys
from datetime import datetime

response = {
    'Table': {
        'AttributeDefinitions': [
            {
                'AttributeName': 'string'  # ,
                #                'AttributeType': 'S' | 'N' | 'B'
            },
        ],
        'TableName': 'employees',
        'KeySchema': [
            {
                'AttributeName': 'string'  # ,
                # 'KeyType': 'HASH' | 'RANGE'
            },
        ],
        # 'TableStatus': 'CREATING' | 'UPDATING' | 'DELETING' | 'ACTIVE' | 'INACCESSIBLE_ENCRYPTION_CREDENTIALS' | 'ARCHIVING' | 'ARCHIVED',
        'CreationDateTime': datetime(2015, 1, 1),
        'ProvisionedThroughput': {
            'LastIncreaseDateTime': datetime(2015, 1, 1),
            'LastDecreaseDateTime': datetime(2015, 1, 1),
            'NumberOfDecreasesToday': 123,
            'ReadCapacityUnits': 123,
            'WriteCapacityUnits': 123
        },
        'TableSizeBytes': 123,
        'ItemCount': 123,
        'TableArn': 'string',
        'TableId': 'string',
        'BillingModeSummary': {
            # 'BillingMode': 'PROVISIONED' | 'PAY_PER_REQUEST',
            'LastUpdateToPayPerRequestDateTime': datetime(2015, 1, 1)
        },
        'LocalSecondaryIndexes': [
            {
                'IndexName': 'string',
                'KeySchema': [
                    {
                        'AttributeName': 'string'  # ,
                        #  'KeyType': 'HASH' | 'RANGE'
                    },
                ],
                'Projection': {
                    # 'ProjectionType': 'ALL' | 'KEYS_ONLY' | 'INCLUDE',
                    'NonKeyAttributes': [
                        'string',
                    ]
                },
                'IndexSizeBytes': 123,
                'ItemCount': 123,
                'IndexArn': 'string'
            },
        ],
        'GlobalSecondaryIndexes': [
            {
                'IndexName': 'string',
                'KeySchema': [
                    {
                        'AttributeName': 'string'  # ,
                        #  'KeyType': 'HASH' | 'RANGE'
                    },
                ],
                'Projection': {
                    # 'ProjectionType': 'ALL' | 'KEYS_ONLY' | 'INCLUDE',
                    'NonKeyAttributes': [
                        'string',
                    ]
                },
                # 'IndexStatus': 'CREATING' | 'UPDATING' | 'DELETING' | 'ACTIVE',
                'Backfilling': True | False,
                'ProvisionedThroughput': {
                    'LastIncreaseDateTime': datetime(2015, 1, 1),
                    'LastDecreaseDateTime': datetime(2015, 1, 1),
                    'NumberOfDecreasesToday': 123,
                    'ReadCapacityUnits': 123,
                    'WriteCapacityUnits': 123
                },
                'IndexSizeBytes': 123,
                'ItemCount': 123,
                'IndexArn': 'string'
            },
        ],
        'StreamSpecification': {
            'StreamEnabled': True | False  # ,
            #  'StreamViewType': 'NEW_IMAGE' | 'OLD_IMAGE' | 'NEW_AND_OLD_IMAGES' | 'KEYS_ONLY'
        },
        'LatestStreamLabel': 'string',
        'LatestStreamArn': 'string',
        'GlobalTableVersion': 'string',
        'Replicas': [
            {
                'RegionName': 'string',
                #   'ReplicaStatus': 'CREATING' | 'CREATION_FAILED' | 'UPDATING' | 'DELETING' | 'ACTIVE' | 'REGION_DISABLED' | 'INACCESSIBLE_ENCRYPTION_CREDENTIALS',
                'ReplicaStatusDescription': 'string',
                'ReplicaStatusPercentProgress': 'string',
                'KMSMasterKeyId': 'string',
                'ProvisionedThroughputOverride': {
                    'ReadCapacityUnits': 123
                },
                'GlobalSecondaryIndexes': [
                    {
                        'IndexName': 'string',
                        'ProvisionedThroughputOverride': {
                            'ReadCapacityUnits': 123
                        }
                    },
                ],
                'ReplicaInaccessibleDateTime': datetime(2015, 1, 1)
            },
        ],
        'RestoreSummary': {
            'SourceBackupArn': 'string',
            'SourceTableArn': 'string',
            'RestoreDateTime': datetime(2015, 1, 1),
            'RestoreInProgress': True | False
        },
        'SSEDescription': {
            #'Status': 'ENABLING' | 'ENABLED' | 'DISABLING' | 'DISABLED' | 'UPDATING',
           # 'SSEType': 'AES256' | 'KMS',
            'SSEType': 'KMS',
            'KMSMasterKeyArn': 'string',
            'InaccessibleEncryptionDateTime': datetime(2015, 1, 1)
        },
        'ArchivalSummary': {
            'ArchivalDateTime': datetime(2015, 1, 1),
            'ArchivalReason': 'string',
            'ArchivalBackupArn': 'string'
        }
    }
}

# Table name
print(response['Table']['TableName'])
# Item Count
print(response['Table']['ItemCount'])
# Ensure that your Amazon DynamoDB tables are using AWS-managed Customer Master Keys (CMKs) instead of
# AWS-owned CMKs for Server-Side Encryption (SSE), in order to meet strict encryption compliance and
# regulatory requirements.
print(response['Table']['SSEDescription']['SSEType'])
print(response['Table']['SSEDescription']['KMSMasterKeyArn'])
