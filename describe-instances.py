import boto3
ec2 = boto3.client("ec2")
response = response = ec2.describe_instances()
#print(response)
response = response['Reservations']
print(len(response), 'instance(s) found')
print('-----------------------')
x = 1
for instance in response:
    print('instance', x)
    print('Name:',instance['Instances'][0]['KeyName'])
    print('Type:',instance['Instances'][0]['InstanceType'])
    print('State:', instance['Instances'][0]['State']['Name'])
    print('-----------------------')
    x+=1
input('Press any key to continue..')



