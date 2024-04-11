# Links
1. [AWS Bedrock Models](https://us-east-1.console.aws.amazon.com/bedrock/home?region=us-east-1#/modelaccess)
1. [Get information about foundation models](https://docs.aws.amazon.com/bedrock/latest/userguide/models-get-info.html)
1. [Bedrock vs Sagemaker](https://repost.aws/questions/QURQ0DJ5oPSUyyaLv0jjS4vw/bedrock-vs-sagemaker)
1. [ Gen AI API Gateway](https://medium.com/@naman884/how-to-build-serverless-generative-ai-app-using-amazon-bedrock-api-gateway-lambda-s3-and-postman-535436d05f4b)
1. [ API Building Bedrock](https://medium.com/@naman884/how-to-build-serverless-generative-ai-app-using-amazon-bedrock-api-gateway-lambda-s3-and-postman-535436d05f4b)
1. [AWS Jurrasic](https://github.com/aws-samples/lambda-gen-ai-endpoint-blog?tab=readme-ov-file)
1. [Cloud Formation Stack](https://us-east-1.console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/events?stackId=arn%3Aaws%3Acloudformation%3Aus-east-1%3A014531769354%3Astack%2Fjurrasic-2-lambda-endpoint%2F05236720-f6af-11ee-b48d-0ec1a19f506f&filteringText=&filteringStatus=active&viewNested=true)


# Other Info
1. AI21 API Key - 3lnD86XXWECZPjNgTvOmpDtqLuupM5NF , [AI 21 API](https://studio.ai21.com/account/api-key)
1. Region - US East


# Commands

1. Create Zip File of dependency
```bash
pip3 install boto3 ai21 -t ./python/lib/python3.9/site-packages && zip -r lambda_layer.zip ./python && rm -R ./python && ls
```

2. Upload Lambda Layer
```bash
aws lambda publish-layer-version --layer-name AI21_layer --zip-file fileb://lambda_layer.zip --compatible-runtimes python3.9
```

3. Testing endpoint
```bash
curl -X POST -H "Content-Type: application/json" -d '{"prompt" : "Tell me a short story about a tiger and lion."}' https://4ztbnapd65jlwjwpo23rxqk3gu0slhcv.lambda-url.us-east-1.on.aws/
```

4. Live Endpoint for Postman
```bash
https://ruk048xh2b.execute-api.us-east-1.amazonaws.com/devenv?prompt=How many country are in world
```