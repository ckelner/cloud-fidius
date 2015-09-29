import boto3
import json

# "Constants"
EXPECTED_INSTANCES_CONFIG = "fidius.json"

def readExpectedInstances():
    with open(EXPECTED_INSTANCES_CONFIG) as json_file:
        json_data = json.load(json_file)
        print(json_data)

def getEc2Instances():
    ec2 = boto3.resource('ec2')
    # Use the filter() method of the instances collection to retrieve
    # all running EC2 instances.
    return ec2.instances.filter(
        Filters=[{
            'Name': 'instance-state-name',
            'Values': ['running']
        }]
    )

readExpectedInstances()
