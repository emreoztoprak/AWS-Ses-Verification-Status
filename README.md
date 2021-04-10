# AWS-Ses-Verification-Status
This simple python script can check your domain on AWS SES and send you a notification via SNS if your domain is unverified.

Change this 'TopicArn' with your own SNS Topic ARN and change 'example.com' to your own domain address.

You can add this script to Lambda and adding trigger to Lambda function with Eventbridge schedule expression.