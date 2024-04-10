# imports needed libraries
import json, os, ai21, boto3
def lambda_handler(event, context):
    # Example of incoming request via JSON object {"prompt" : "What day is it?"}
    # parse the prompt from the incoming event object
    prompt = json.loads(event['body'])['prompt']

    
    # sets the AI21 Labs API key
    ai21.api_key = '3lnD86XXWECZPjNgTvOmpDtqLuupM5NF'

    # sets the Jurassic model you would like to use
    model = os.environ['ai_21_model']

    # sets the number of completions (results) that will be returned in the model results
    numberOfResults = int(os.environ['model_result_count'])

    # sets the maximum number of tokens that can be used when executing call to model
    maxTokens = int(os.environ['model_max_tokens'])

    # sets the temperature paramter for the model
    temp = os.environ['model_temp']

    # calls the Jurassic-2 model and passes model parameters to the method
    model_response = ai21.Completion.execute(
        model=model,
        prompt=prompt,
        numResults=numberOfResults,
        maxTokens=maxTokens,
        temperature=temp
    )

    # output printed for debugging 
    print(model_response.completions[0].data.text)
    
    # returns the models result in the body of the JSON object
    return {
        'statusCode': 200,
        'body': json.dumps(model_response.completions[0].data.text)
    } 
    
