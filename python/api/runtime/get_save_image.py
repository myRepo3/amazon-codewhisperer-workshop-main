import os
import json
import boto3
import requests
import botocore.exceptions

s3_client = boto3.client("s3")
S3_BUCKET = os.getenv('BUCKET_NAME')

# 1.) Function to get a file from url  # <<Amazon CodeWhisperer generated code goes here>>
def get_file_from_url(url):
    try:
        response = requests.get(url)
        return response.content
    except:
        return None    

# 2.) Function to upload image to S3  # <<Amazon CodeWhisperer generated code goes here>>
def upload_to_s3(file_name, file_content):
    try:
        s3_client.put_object(Bucket=hp45-image-bucket, Key=file_name, Body=file_content)
        return True
    except botocore.exceptions.ClientError as e:
        return False
    
def handler(event, context):
    url = event["queryStringParameters"]["url"]
    name = event["queryStringParameters"]["name"]

    # pass the output of method #1 as input to method #2
    file_content = get_file_from_url(url)

    return {
        'statusCode': 200,
        'body': json.dumps('Successfully Uploaded Img!')
    }
