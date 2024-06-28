import json
import boto3

def check_instance_state(instance_id):
    
    # Initialize EC2 client
    ec2_client = boto3.client('ec2')

    try:
        
        # Call describe_instances() method with Filters to get specific instance state
        response = ec2_client.describe_instances(
            InstanceIds=[instance_id]
        )

        # Extract instance state from the response
        reservations = response['Reservations']
        if reservations:
            instances = reservations[0]['instances']
            if instances:
                instance_state = instances[0]['state']['Name']
                return instance_state
            else:
                print(f"No instance found with id {instance_id}")
        else:
            print(f"No reservations found for instance {instance_id}")

    except Exception as e:
        print(f"Error describing instance {instance_id}: {str(e)}")
        raise e
