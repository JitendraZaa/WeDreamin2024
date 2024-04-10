# imports needed libraries
import json, os, ai21, boto3
def lambda_handler(event, context):
    # Example of incoming request via JSON object {"prompt" : "What day is it?"}
    # parse the prompt from the incoming event object
    prompt = 'What day is it?'

    
    # sets the AI21 Labs API key
    ai21.api_key = '3lnD86XXWECZPjNgTvOmpDtqLuupM5NF'

    client = boto3.client(service_name="bedrock-runtime", region_name="us-east-1")

    wrapper = BedrockRuntimeWrapper(client)

    
    # returns the models result in the body of the JSON object
    return wrapper.invoke_jurassic2(prompt)
    
def invoke_jurassic2(self, prompt):
    """
    Invokes the AI21 Labs Jurassic-2 large-language model to run an inference
    using the input provided in the request body.

    :param prompt: The prompt that you want Jurassic-2 to complete.
    :return: Inference response from the model.
    """

    try:
        # The different model providers have individual request and response formats.
        # For the format, ranges, and default values for AI21 Labs Jurassic-2, refer to:
        # https://docs.aws.amazon.com/bedrock/latest/userguide/model-parameters-jurassic2.html

        body = {
            "prompt": prompt,
            "temperature": 0.5,
            "maxTokens": 200,
        }

        response = self.bedrock_runtime_client.invoke_model(
            modelId="ai21.j2-mid-v1", body=json.dumps(body)
        )

        response_body = json.loads(response["body"].read())
        completion = response_body["completions"][0]["data"]["text"]

        return completion

    except ClientError:
        logger.error("Couldn't invoke Jurassic-2")
        raise


