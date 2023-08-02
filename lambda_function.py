import json

# defining a function that lambda service will use as entry point
def lambda_handler(event,context):
    # extract the values form lambda function that we extracted
    name=event['firstname']+' '+event['lastname']
    # return formatted json format
    return{
        'statusCode':200,
        'body':json.dumps('Hello from Lambda, '+name)
    }