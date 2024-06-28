import json

import boto3

ec2 = boto3.client('ec2')

instance_ids = ['insatnce_id1', 'instance_id2']

try:
    
    response = ec2.describe_instances(InstanceIds=instance_ids)

    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            instance_id = instance['InstanceId']
            state = instance['State']['Name']
            print(f"Instance ID: {instance_id}, State: {state}")

except Exception as e:
    print(f"Error: {e}")
    raise e
