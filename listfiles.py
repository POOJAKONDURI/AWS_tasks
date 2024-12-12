import boto3
s3 = boto3.client('s3')

response = s3.list_objects_v2(Bucket='my-bucket-s3learn856447')
for content in response.get('Contents', []):
    print(content.get('Key'))
