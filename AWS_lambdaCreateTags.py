import json
import boto3

ec2 = boto3.client('ec2')

def lambda_handler(event, context):
    print(event)

    instanceId = event['detail']['responseElements']['instancesSet']['items'][0]['instanceId']

    userType = event['detail']['userIdentity']['type']

    response = ec2.create_tags(
        Resources=[
            instanceId,
        ],
        Tags=[
            {
                'Key': 'creationAuthority',
                'Value': userType
            },
        ]
    )