# imports needed libraries
import json, boto3
import botocore.config

def lambda_handler(event, context):
    # Example of incoming request via JSON object {"prompt" : "What day is it?"}
    # parse the prompt from the incoming event object

    #prompt_text = json.loads(event['prompt'])
    prompt_text = event.get('prompt', '')  
    
    #print('Check')
    #print(prompt_text)

    # prompt_text = f"""Human: Can you tell me a short story
    # Assistant:"""

    body = {
        "prompt":prompt_text, 
        "temperature":0.3 ,
        "maxTokens" : 8000
    }

    # calling the bedrock API
    bedrock = boto3.client("bedrock-runtime", region_name="us-east-1",
                           config = botocore.config.Config(read_timeout=300, retries = {'max_attempts':3}))
    
    response = bedrock.invoke_model(body=json.dumps(body),modelId="ai21.j2-ultra-v1")
    response_content = response.get('body').read().decode('utf-8')
    response_data = json.loads(response_content)
    #print(response_data)
    generated_text = response_data['completions'][0]['data']['text']
    #print (generated_text)
    #summary = response_data["completions"].strip()
    
    #return summary
    return generated_text

 