import boto3
from sqsIterate import iterateQueues

client = boto3.client('sqs')

# look for the queue we care about
queue = iterateQueues(client, 'Project', 'AWS-SQS-POC')

# if we can't find it, barf
if not queue:
    print('No queue found with Project=AWS-SQS-POC tag')
    exit()
 
# lets write some junk to a queue
response = client.send_message(
    QueueUrl=queue,
    DelaySeconds=0,
    MessageAttributes={
        'Title': {
            'DataType': 'String',
            'StringValue': 'The Whistler'
        },
        'Author': {
            'DataType': 'String',
            'StringValue': 'John Grisham'
        },
        'WeeksOn': {
            'DataType': 'Number',
            'StringValue': '6'
        }
    },
    MessageBody=(
        'Information about current NY Times fiction bestseller for '
        'week of 12/11/2016.'
    )
)

print(response['MessageId'])