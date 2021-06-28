import boto3
from sqsIterate import iterateQueues

client = boto3.client('sqs')

# look for the queue we care about
queue = iterateQueues(client, 'Project', 'AWS-SQS-POC')

# if we can't find it, barf
if not queue:
    print('No queue found with Project=AWS-SQS-POC tag')
    exit()
 
 # lets read some junk from a queue
response = client.receive_message(
    QueueUrl=queue,
    AttributeNames=[
        'SentTimestamp'
    ],
    MaxNumberOfMessages=1,
    MessageAttributeNames=[
        'All'
    ],
    VisibilityTimeout=0,
    WaitTimeSeconds=0
)

if not 'Messages' in response:
    print('No messages')
    exit()

for message in response['Messages']:
    receipt_handle = message['ReceiptHandle']

    # Delete received message from queue
    client.delete_message(
        QueueUrl=queue,
        ReceiptHandle=receipt_handle
    )

    print('Received and deleted message: %s' % message)