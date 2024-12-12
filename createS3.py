import boto3

s3 = boto3.client('s3')
bucket_name = 'my-bucket-s3learn856447'
region = 'us-west-1'

s3.create_bucket(Bucket=bucket_name, CreateBucketConfiguration={'LocationConstraint': region})
