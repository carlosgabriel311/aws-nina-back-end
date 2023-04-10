import json
import boto3

dynamodb = boto3.client('dynamodb')

def lambda_handler(event, context):

    post = json.loads(event['body'])

    response = dynamodb.put_item(
        TableName='products',
        Item={
            '_id': {
                'S': post['_id']
            },
            'name': {
                'S': post['name']
            },
            'description': {
                'S': post['description']
            },
            'category': {
                'S': post['category']
            },
            'brand': {
                'S': post['brand']
            },
            'price': {
                'N': post['price']
            },
            'inventory': {
                'M': {
                    'total': {
                        'N' :post['inventory']['total']
                    },
                    'available': {
                        'N' :post['inventory']['available']
                    }
                }
            },
            'images': {
                'L': [post['images']]
            },
            'created_at': {
                'S': post['created_at']
            },
            'updated_at': {
                'S': post['updated_at']
            },
        },
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