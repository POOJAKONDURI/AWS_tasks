import boto3
s3 = boto3.client('s3')
s3.delete_object(Bucket='my-bucket-s3learn856447', Key='full_grouped.csv')
