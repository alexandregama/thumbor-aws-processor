import boto3
import json
from config.configurator import ThumborConfigurator

sqs = boto3.resource('sqs')

queue_name = ThumborConfigurator().get_queue_name()
queue = sqs.get_queue_by_name(QueueName=queue_name)

while 1:
    messages = queue.receive_messages(WaitTimeSeconds=5)
    print("Waiting for messages...")
    for message in messages:
        processorProperties = json.loads(message.body)
        print("Url to process: {0}".format(processorProperties['s3-url']))
        print("New Width: {0}".format(processorProperties['resize']['width']))
        print("New Height  : {0}".format(processorProperties['resize']['height']))
        message.delete()
