# response = client.invoke(
#     FunctionName='my-function',
#     Payload='{}',
#     Qualifier='1',
# )

# print(response)

import boto3

endpoint_url = "http://localhost.localstack.cloud:4566"
# alternatively, to use HTTPS endpoint on port 443:
# endpoint_url = "https://localhost.localstack.cloud"

def main():
    client = boto3.client("lambda", endpoint_url=endpoint_url)
    result = client.list_functions()

    response = client.invoke(
    FunctionName='myfirstlambda',
    LogType='Tail',
    ClientContext='string',
    Payload=b'{"a":"b", "c": 1000}')

    print(response)

    print(response['Payload'].read())

if __name__ == "__main__":
    main()