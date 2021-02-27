# Create a bucket
import boto3

client = boto3.client('s3')

response = client.create_bucket(
    ACL='private',
    Bucket='S3Rules_Bucket1',
    CreateBucketConfiguration={
        'LocationConstraint': 'us-west-2',
    }
)
