import boto3
import json

s3 = boto3.client('s3')

def lambda_handler(event, context):

    post = json.loads(event['body']),

    response = s3.put_object(
        Bucket= post['bucket'],
        Key = post['key'],
        body = post['body'],
        Metadata = {
            '_id' : post['_id'],
        }
    )

    return {
        'isBase64Encoded': False,
        'statusCode':response['ResponseMetadata']['HTTPStatusCode'],
        'headers': {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Credentials': True,
        },
        'multiValueHeaders': dict(),
        'body': json.dumps(response)
    }

