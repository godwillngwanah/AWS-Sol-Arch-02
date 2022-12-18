import json
import boto3

def lambda_handler(event, context):

    sqs_queue_url="<QUEUE_URL> "
    
    sqs_client = boto3.client('sqs')
   
    msg = sqs_client.send_message(QueueUrl=sqs_queue_url,MessageBody=event,MessageGroupId='mygroup',MessageDeduplicationId='dedupeID',
)