import json


def endpoint(event, context):
    numbers =event['body'].split(',')
    body = {
        "message": numbers
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response