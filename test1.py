import boto3

client = boto3.resource('dynamodb')

table = client.Table('Product')

def lambda_handler(event, context):
    table.put_item(Item=event)
    return{"code":200,"message":"Product has been inserted!"}