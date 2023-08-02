import json
#import AWS SDK
import boto3

from time import gtime,strftime

#create dynamodb using AWS SDk

dynamodb=boto3.resource('dynamodb')
#use this db object to select our table
table=dynamodb.Table('HelloWorldDtbase')
#store current table in human readable format

now=strftime("%a,%d %b %Y %H:%M:%S +0000",gtime())
#define a handler function that act as entry point for lambda function

def lambda_handler(event,context):
    #extract values from table and store it in table
    name=event["firstname"]+" "+event["lastname"]
#write name and time to dynamodb using the object we initiated and save it in var
    response=table.put_item(
        Item={
            'ID':name,
            'LatestGreetingTime':now
        
        })
    #return proper formatted data
    return{
        'statusCode':200,
        'body':json.dumps('Hello from Lambda, '+name)
    }



  

