from __future__ import print_function
import boto3
import urllib.parse
import time, urllib
import json
import pandas as pd
import io
import time 
print ("Loading Function..")
s3 = boto3.client('s3')


def lambda_handler(event, context):
    print(event)
    print("hi hello")
    s3_records = event['Records'][0]
    bucket_name = str(s3_records['s3']['bucket']['name'])
    file_name = str(s3_records['s3']['object']['key'])
    print(bucket_name, "file - ", file_name)
    file_obj = s3.get_object(Bucket = bucket_name, Key = file_name)
    
    file_content = file_obj['Body'].read()
    b = io.BytesIO(file_content)

    df = pd.read_excel(b)
    links = df['Links'].dropna().tolist()
    print(len(links))
    sqs = boto3.client('sqs') 
 
    for link in links:
        try:
            response = sqs.send_message(
                QueueUrl = "https://sqs.eu-north-1.amazonaws.com/826844983734/ngo-formfiller-website-queue",
                MessageBody= link
                )
            print(response)
        except:
            print("error in links = ", link)
                
            

    return {
        'statusCode': 200,
        'body': 'Links extracted and queued successfully!'
    }        
        


        
    
    
    
