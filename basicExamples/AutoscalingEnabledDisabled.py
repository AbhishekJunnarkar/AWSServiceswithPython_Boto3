# Response is dictionary
response = {
    'GlobalTableName': 'string',
    'ReplicaSettings': [
        {
            'RegionName': 'string',
            'ReplicaStatus': 'CREATING' ,
            'ReplicaBillingModeSummary': {
                'BillingMode': 'PROVISIONED',
                'LastUpdateToPayPerRequestDateTime': '1'
            },
            'ReplicaProvisionedReadCapacityUnits': 123,
            'ReplicaProvisionedReadCapacityAutoScalingSettings': {
                'MinimumUnits': 123,
                'MaximumUnits': 123,
                'AutoScalingDisabled': True | False,
                'AutoScalingRoleArn': 'string',
                'ScalingPolicies': [
                    {
                        'PolicyName': 'string',
                        'TargetTrackingScalingPolicyConfiguration': {
                            'DisableScaleIn': True | False,
                            'ScaleInCooldown': 123,
                            'ScaleOutCooldown': 123,
                            'TargetValue': 123.0
                        }
                    },
                ]
            },
            'ReplicaProvisionedWriteCapacityUnits': 123,
            'ReplicaProvisionedWriteCapacityAutoScalingSettings': {
                'MinimumUnits': 123,
                'MaximumUnits': 123,
                'AutoScalingDisabled': True | False,
                'AutoScalingRoleArn': 'string',
                'ScalingPolicies': [
                    {
                        'PolicyName': 'string',
                        'TargetTrackingScalingPolicyConfiguration': {
                            'DisableScaleIn': True | False,
                            'ScaleInCooldown': 123,
                            'ScaleOutCooldown': 123,
                            'TargetValue': 123.0
                        }
                    },
                ]
            },
            'ReplicaGlobalSecondaryIndexSettings': [
                {
                    'IndexName': 'string',
                    'IndexStatus': 'CREATING' ,
                    'ProvisionedReadCapacityUnits': 123,
                    'ProvisionedReadCapacityAutoScalingSettings': {
                        'MinimumUnits': 123,
                        'MaximumUnits': 123,
                        'AutoScalingDisabled': True | False,
                        'AutoScalingRoleArn': 'string',
                        'ScalingPolicies': [
                            {
                                'PolicyName': 'string',
                                'TargetTrackingScalingPolicyConfiguration': {
                                    'DisableScaleIn': True | False,
                                    'ScaleInCooldown': 123,
                                    'ScaleOutCooldown': 123,
                                    'TargetValue': 123.0
                                }
                            },
                        ]
                    },
                    'ProvisionedWriteCapacityUnits': 123,
                    'ProvisionedWriteCapacityAutoScalingSettings': {
                        'MinimumUnits': 123,
                        'MaximumUnits': 123,
                        'AutoScalingDisabled': True | False,
                        'AutoScalingRoleArn': 'string',
                        'ScalingPolicies': [
                            {
                                'PolicyName': 'string',
                                'TargetTrackingScalingPolicyConfiguration': {
                                    'DisableScaleIn': True | False,
                                    'ScaleInCooldown': 123,
                                    'ScaleOutCooldown': 123,
                                    'TargetValue': 123.0
                                }
                            },
                        ]
                    }
                },
            ]
        },
    ]
}

print(response['ReplicaSettings'])