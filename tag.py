import boto3
import sys
ec2 = boto3.client('ec2')
instances = ec2.describe_instances()
ids =['']
print("Changing tags for instances")
ec2.create_tags(Resources=ids,
	Tags=[
	{
            'Key': 'Name',
            'Value': 'ec2user'
	}
    ]
)