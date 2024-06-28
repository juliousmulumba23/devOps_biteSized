import json
import boto3

def lambda_handler(event, context):
    # Create ec2 object
    ec2 = boto3.resource('ec2')

    for instance in ec2.instances.all():
        state = instance.state['Name']
        if state == 'running':
            try:
                instance.terminate()
            except Exception as e:
                print(e)