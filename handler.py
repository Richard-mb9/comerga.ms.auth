import json


def hello(event, context):
    body = {
        "message": "funcionou o teste",
        #"input": event
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response
