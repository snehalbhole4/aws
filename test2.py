import json

def lambda_handler(event,context):
    product_name=event['queryStringParameters']['product_name']
    product_brand=event['queryStringParameters']['product_brand']
    
    
    app_response={}
    app_response['message']='Hello these are the details for' +product_name+ ' ' + product_brand
    

    responseObject={}
    responseObject['statusCode']=200
    responseObject['headers']={}
    responseObject['headers']['content-Type']='application/json'
    responseObject['body']=json.dumps(app_response)
    
    
    return responseObject
