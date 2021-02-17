response = {'Table': {'AttributeDefinitions': [{'AttributeName': 'LockID', 'AttributeType': 'S'}],
                      'TableName': 'kat-terraform-locks', 'KeySchema': [{'AttributeName': 'LockID', 'KeyType': 'HASH'}],
                      'TableStatus': 'ACTIVE',
                      'CreationDateTime': '1',
                      'ProvisionedThroughput': {'NumberOfDecreasesToday': 0, 'ReadCapacityUnits': 0,
                                                'WriteCapacityUnits': 0}, 'TableSizeBytes': 4866, 'ItemCount': 42,
                      'TableArn': 'arn:aws:dynamodb:eu-west-1:248762759038:table/kat-terraform-locks',
                      'TableId': '452bb11b-efda-4155-a8bf-fd368fedc1c0',
                      'BillingModeSummary': {'BillingMode': 'PAY_PER_REQUEST',
                                             'LastUpdateToPayPerRequestDateTime':
                                                 '1'}},
            'ResponseMetadata': {'RequestId': '61BBQ8OC62F2HVTJ9BQ8T2FGNFVV4KQNSO5AEMVJF66Q9ASUAAJG',
                                 'HTTPStatusCode': 200,
                                 'HTTPHeaders': {'server': 'Server', 'date': 'Fri, 12 Feb 2021 09:52:12 GMT',
                                                 'content-type': 'application/x-amz-json-1.0', 'content-length': '729',
                                                 'connection': 'keep-alive',
                                                 'x-amzn-requestid': '61BBQ8OC62F2HVTJ9BQ8T2FGNFVV4KQNSO5AEMVJF66Q9ASUAAJG',
                                                 'x-amz-crc32': '3826582830'}, 'RetryAttempts': 0}}

if 'BillingModeSummary' in response['Table']:
    print(response['Table']['BillingModeSummary']['BillingMode'])
