import json
from flask_lambda import FlaskLambda


app = FlaskLambda(__name__)

@app.route("/auth")
def handler(event, context):
    body = {
        "message": "esta no ar",
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response
