import boto3
import json
from config.configurator import ThumborConfigurator
import urllib.request

sqs = boto3.resource('sqs')

queue_name = ThumborConfigurator().get_queue_name()
queue = sqs.get_queue_by_name(QueueName=queue_name)

while 1:
    messages = queue.receive_messages(WaitTimeSeconds=5)
    print("Waiting for messages...")
    for message in messages:
        processorProperties = json.loads(message.body)
        print("Url to process: {0}".format(processorProperties['s3-url']))
        print("Original image name  : {0}".format(processorProperties['original-image-name']))
        print("New Width: {0}".format(processorProperties['resize']['width']))
        print("New Height  : {0}".format(processorProperties['resize']['height']))

        bucket_name = 'procurando-thumbor-images'
        url = processorProperties['s3-url']
        original_image_name = processorProperties['original-image-name']
        urllib.request.urlretrieve(url, original_image_name)

        s3 = boto3.client('s3')
        s3.upload_file(original_image_name, bucket_name, original_image_name)

        message.delete()
