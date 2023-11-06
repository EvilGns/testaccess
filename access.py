import boto3

# Hardcoded AWS Access Key (Replace with your real key)
aws_access_key = 'AKIAEXAMPLEACCESSKEY'
aws_secret_key = 'YourSecretKeyHere'

# Initialize an AWS S3 client
s3 = boto3.client('s3', aws_access_key_id=aws_access_key, aws_secret_access_key=aws_secret_key)

# List buckets
buckets = s3.list_buckets()
for bucket in buckets['Buckets']:
    print(f'Bucket Name: {bucket["Name"]}')
