# Cloud Fidius
A tool to reconcile what is running in your cloud environment and compare it to
what you expect to be running in that environment.

# Getting Started

## Requirements
- Python 2 (2.6.7)

## Config
Fidius is built on top of [Boto 3](https://github.com/boto/boto3) which utilizes
the AWS SDK, and therefore re-uses AWS configuration.  Therefore if you've ever
used the AWS CLI tools, you'll likely already have the following configuration
available to Fidius:

Set up your configuration and credentials in ``~/.aws/config`` under a new profile:
```ini
    [profile YOUR_PROFILE_NAME]
    output = json
    region = us-east-1
    aws_access_key_id = YOUR_KEY
    aws_secret_access_key = YOUR_SECRET
```
