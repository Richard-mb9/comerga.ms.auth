import json


def handler(event, context):
    body = {
        "message": "esta no ar",
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response
