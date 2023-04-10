import json
import boto3

dynamodb = boto3.client('dynamodb')

def lambda_handler(event, context):

    post = json.loads(event['body'])

    response = dynamodb.update_item(
        TableName='products',
        Key= {
            '_id': {
                'S' : post['_id']
            },
        },
        UpdateExpression = 'SET #na = :name, #des = :description, #cat = :category, #bra = :brand, #pri = :price, #inv = :inventory, #ima = :images, #cre = :created_at, #upd = :updated_at',
        ExpressionAttributeNames = {
            '#nam' : 'name',
            '#des': 'description',
            '#cat': 'category',
            '#bra': 'brand',
            '#pri': 'price',
            '#inv': 'inventory',
            '#ima': 'images',
            '#cre': 'created_at',
            '#upd': 'updated_at',

        },
        ExpressionAttributeValues = {
            ':name': {
                'S': post['name']
            },
            ':description': {
                'S': post['description']
            },
            ':category': {
                'S': post['category']
            },
            ':brand': {
                'S': post['brand']
            },
            ':price': {
                'N': post['price']
            },
            ':inventory': {
                'M': {
                    'total': {
                        'N' :post['inventory']['total']
                    },
                    'available': {
                        'N' :post['inventory']['available']
                    }
                }
            },
            ':images': {
                'L': [post['images']]
            },
            ':created_at': {
                'S': post['created_at']
            },
            ':updated_at': {
                'S': post['updated_at']
            },
        },
        ReturnValues='ALL_NEW',
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