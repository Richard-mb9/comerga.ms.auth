import json
from flask_lambda import FlaskLambda


app = FlaskLambda(__name__)

@app.route("/auth", methods=['GET', 'POST'])
def handler():
    body = {
        "message": "esta no ar",
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response


if __name__ == '__main__':
    app.run(host='0.0.0.0')