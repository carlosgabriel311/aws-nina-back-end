import json
import boto3

dynamodb = boto3.client('dynamodb')

def lambda_handler(event, context):

    post = json.loads(event['body'])

    response = dynamodb.delete_item(
        TableName='products',
        Key= {
            '_id': {
                'S': post['_id'],
            },
        },
    )

    return {
        'isBase64Encoded': False,
        'statusCode': response['ResponseMetadata']['HTTPStatusCode'],
        'headers': {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Credentials': True,
        },
        'multiValueHeaders': dict(),
        'body': json.dumps(response)
    }