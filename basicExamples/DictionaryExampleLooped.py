import datetime

response = {
    'ContinuousBackupsDescription': {
        'ContinuousBackupsStatus': 'ENABLED',  # |'DISABLED',
        'PointInTimeRecoveryDescription': {
            'PointInTimeRecoveryStatus': 'ENABLED',  # | 'DISABLED',
            'EarliestRestorableDateTime': '1',
            'LatestRestorableDateTime': '2'
        }
    }
}
print(response)
print(response['ContinuousBackupsDescription'])
print('###')
print(response['ContinuousBackupsDescription']['ContinuousBackupsStatus'])
print('### ###')
print(response['ContinuousBackupsDescription']['PointInTimeRecoveryDescription']['PointInTimeRecoveryStatus'])

