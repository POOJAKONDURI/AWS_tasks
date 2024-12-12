import boto3
s3 = boto3.client('s3')
s3.upload_file('C:/Users/pooja konduri/Downloads/covid-kaggle-dataset/full_grouped.csv', 'my-bucket-s3learn856447', 'full_grouped.csv')
