import boto3
import json

dynamodb = boto3.client('dynamodb')

def lambda_handler(event, context):
    key = event['Records'][0]['s3']['object']['key']
    bucket = event['Records'][0]['s3']['bucket']['name']
    url = f'https://{bucket}.s3.amazonaws.com/{key}'

    response = dynamodb.update_item(
        Table='products',
        Key={
            '_id': event['Records'][0]['s3']['object']['metadata']['_id']   # tip: set post _id as object metadata in S3
        },
        UpdateExpression='delete :images',
        ExpressionAttributeValues={
            ':images': [url]
        },
        ReturnValues='UPDATED_NEW'
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
