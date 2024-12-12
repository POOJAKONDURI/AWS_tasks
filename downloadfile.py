import boto3
s3 = boto3.client('s3')
s3.download_file('my-bucket-s3learn856447', 'day_wise.csv', 'downloaded_file1.csv')
