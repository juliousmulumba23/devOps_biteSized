import uuid

def generate_aws_request_id():
    return str(uuid.uuid4())

request_id = generate_aws_request_id()
print(request_id)