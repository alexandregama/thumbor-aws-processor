import boto3
import json
from config.configurator import ThumborConfigurator
import urllib.request

sqs = boto3.resource('sqs')
s3 = boto3.client('s3')

queue_name = ThumborConfigurator().get_queue_name()
queue = sqs.get_queue_by_name(QueueName=queue_name)
thumbor_processor_server = "http://52.202.49.87:8000/unsafe/"

while 1:
    messages = queue.receive_messages(WaitTimeSeconds=5)
    print("Waiting for messages...")
    for message in messages:
        thumbor_image_to_process = json.loads(message.body)

        image_width = thumbor_image_to_process["resize"]["width"]
        image_height = thumbor_image_to_process["resize"]["height"]
        package = thumbor_image_to_process["resize"]["package"]
        resized_name = thumbor_image_to_process["resize"]["image-name"]
        bucket_name = 'procurando-thumbor-images'
        s3_url = thumbor_image_to_process['s3-url']
        original_image_name = thumbor_image_to_process['original-image-name']

        image_url_to_process = s3_url
        if image_width and image_height:
            resize = image_width + "x" + image_height
            image_url_to_process = thumbor_processor_server + resize + "/" + s3_url

        print("Original Image url to process {0}".format(s3_url))
        urllib.request.urlretrieve(s3_url, original_image_name)
        s3.upload_file(original_image_name, bucket_name, original_image_name)

        print("Resized Image url {0}".format(image_url_to_process))
        urllib.request.urlretrieve(image_url_to_process, resized_name)
        s3.upload_file(resized_name, bucket_name, resized_name)

        message.delete()
