import configparser

class ThumborConfigurator:

    def get_queue_name(self):
        config = configparser.ConfigParser()
        config.read('thumbor-processor.conf')
        print("Sections: {0}".format(config.sections()))
        queue_name = config['SQS']['SQS_QUEUE_NAME']
        print("SQS Queue to read: {0}".format(queue_name))
        return queue_name
