# imports needed libraries
import json, os, ai21, boto3
def lambda_handler(event, context):
    # Example of incoming request via JSON object {"prompt" : "What day is it?"}
    # parse the prompt from the incoming event object

    prompt_text = f"""Human: Can you tell me a short story
    Assistant:"""

    body = {
        "prompt":prompt_text,
        "max_tokens_to_sample":5000,
        "temperature":0.3,
        "top_k":250,
        "top_p":0.2,
        "stop_sequences": ["\n\nHuman:"]
    }

    # calling the bedrock API
    bedrock = boto3.client("bedrock-runtime", region_name="us-east-1",
                           config = botocore.config.Config(read_timeout=300, retries = {'max_attempts':3}))
    
    response = bedrock.invoke_model(body=json.dumps(body),modelId="j2-ultra")
    response_content = response.get('body').read().decode('utf-8')
    response_data = json.loads(response_content)
    summary = response_data["completion"].strip()
    
    return summary 
    

 