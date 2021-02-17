response = {
    'GlobalTableName': 'string',
    'ReplicaSettings': [
        {
            'RegionName': 'string',
            'ReplicaStatus': 'ACTIVE',
            'ReplicaBillingModeSummary': {
                'BillingMode': 'PROVISIONED',
                'LastUpdateToPayPerRequestDateTime': ''
            },
            'ReplicaProvisionedReadCapacityUnits': 123,
            'ReplicaProvisionedReadCapacityAutoScalingSettings': {
                'MinimumUnits': 123,
                'MaximumUnits': 123,
                'AutoScalingDisabled': True,
                'AutoScalingRoleArn': 'string',
                'ScalingPolicies': [
                    {
                        'PolicyName': 'string',
                        'TargetTrackingScalingPolicyConfiguration': {
                            'DisableScaleIn': True,
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
                'AutoScalingDisabled': True,
                'AutoScalingRoleArn': 'string',
                'ScalingPolicies': [
                    {
                        'PolicyName': 'string',
                        'TargetTrackingScalingPolicyConfiguration': {
                            'DisableScaleIn': True,
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
                    'IndexStatus': 'ACTIVE',
                    'ProvisionedReadCapacityUnits': 123,
                    'ProvisionedReadCapacityAutoScalingSettings': {
                        'MinimumUnits': 123,
                        'MaximumUnits': 123,
                        'AutoScalingDisabled': True,
                        'AutoScalingRoleArn': 'string',
                        'ScalingPolicies': [
                            {
                                'PolicyName': 'string',
                                'TargetTrackingScalingPolicyConfiguration': {
                                    'DisableScaleIn': True,
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
                        'AutoScalingDisabled': True,
                        'AutoScalingRoleArn': 'string',
                        'ScalingPolicies': [
                            {
                                'PolicyName': 'string',
                                'TargetTrackingScalingPolicyConfiguration': {
                                    'DisableScaleIn': True,
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
print(response['GlobalTableName'])

print(response['ReplicaSettings'])


for data in response['ReplicaSettings']:
    print(data['ReplicaProvisionedReadCapacityAutoScalingSettings']['AutoScalingDisabled'])


#      ['ReplicaProvisionedReadCapacityAutoScalingSettings'])