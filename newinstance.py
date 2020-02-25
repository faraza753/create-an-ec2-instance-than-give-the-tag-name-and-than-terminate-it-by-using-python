import boto3
client = boto3.client('ec2')
resp = client.run_instances(ImageId = 'ami-00b6a8a2bd28daf19',
                             InstanceType='t2.micro',
                             MinCount=1,
                             MaxCount=1)
for instance in resp['Instances']:
	print(instance['InstanceId'])