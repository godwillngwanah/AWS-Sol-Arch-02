import json
import boto3

def lambda_handler(event, context):
# Retrieve messages from an SQS queue
    sqs_queue_url = "<QUEUE_URL>"
    sqs_client = boto3.client('sqs')

    msgs = sqs_client.receive_message(QueueUrl=sqs_queue_url)
            
    print(msgs)