import json
import boto3

client=boto3.client('dynamodb')

def lambda_handler(event, context):
    print(f"This is the input from agent{event}")
    alertid=event['parameters'][0]['value']
    response = client.get_item(
        TableName='concat_dependabotalert',
        Key={'number':{'N': alertid}})
    print(response)
    response_body = {
        'application/json': {
            'body': json.dumps(response)
        }
    }
   
    action_response = {
        'actionGroup': event['actionGroup'],
        'apiPath': event['apiPath'],
        'httpMethod': event['httpMethod'],
        'httpStatusCode': 200,
        'responseBody': response_body
    }
   
    session_attributes = event['sessionAttributes']
    prompt_session_attributes = event['promptSessionAttributes']
   
    api_response = {
        'messageVersion': '1.0',
        'response': action_response,
        'sessionAttributes': session_attributes,
        'promptSessionAttributes': prompt_session_attributes
    }
       
    return api_response    

