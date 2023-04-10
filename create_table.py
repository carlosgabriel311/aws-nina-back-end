import boto3

dynamodb = boto3.client('dynamodb')

table = dynamodb.create_table(
    TableName= 'products',
    KeySchema=[
        {
            'AttributeName': '_id',
            'KeyType': 'HASH'
        },
    ],
    AttributeDefinitions=[
        {
            'AttributeName': '_id',
            'AttributeType': 'S'
        }
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 5,
        'WriteCapacityUnits': 5
    }
)

print(table.response)