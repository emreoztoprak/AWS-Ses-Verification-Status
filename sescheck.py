import boto3

clientsns = boto3.client('sns')

client = boto3.client('ses')
response = client.get_identity_verification_attributes(
    Identities=[
        'example.com',
    ],
)
data = response['VerificationAttributes']['example.com']['VerificationStatus']

if data != 'Success':
    clientsns.publish(
        TopicArn='YOUR SNS TOPIC ARN',
        Subject='DOMAIN CHECK',
        Message='Your domain is unverified'

    )
else:
    print("Everything is okay")

