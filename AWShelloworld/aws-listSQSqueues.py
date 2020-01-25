import boto3

# Get the service resource
sqs = boto3.resource('sqs')

# Print out each queue name, which is part of its ARN
for queue in sqs.queues.all():
    print(queue.url)
    print(queue.attributes.get('DelaySeconds'))
