# coding: utf-8
import boto3
session = boto3.Session()
ec2 = session.resource('ec2')
key_name = 'python_automation_key'
key_path = key_name + '.pem'
key = ec2.create_key_pair(KeyName=key_name)
key.key_material
with open(key_path, 'w') as key_file:
    key_file.write(key.key_material)
    
get_ipython().run_line_magic('ls', '-l python_automation_key.pem')
import os, stat
os.chmod(key_path, stat.S_IRUSR | stat.S_IWUSR)
ec2.images.filter(Owners=['amazon']
)
list(ec2.images.filter(Owners=['amazon']
))
img = ec2.Image('ami-0323c3dd2da7fb37d')
img.name
ami_name = 'amzn2-ami-hvm-2.0.20200406.0-x86_64-gp2'
filters = [{'Name': 'name', 'Values': [ami_name]}]
list(ecw.images.filter(Owners=['amazon'], Filters=filters))
list(ec2.images.filter(Owners=['amazon'], Filters=filters))
instances = ec2.create_instance(ImageId=img.id, MinCount=1, MaxCount=1, InstanceType='t2.micro', KeyName=key.key_name)
instances = ec2.create_instances(ImageId=img.id, MinCount=1, MaxCount=1, InstanceType='t2.micro', KeyName=key.key_name)
instances
inst = instances[0]
inst.terminate()
instances = ec2.create_instances(ImageId=img.id, MinCount=1, MaxCount=1, InstanceType='t2.micro', KeyName=key.key_name)
inst = instances[0]
inst.public_dns_name
inst.wait_until_running()
inst.reload()
inst.public_dns_name
ssh -i python_automation_key.pem ec2-user@ec2-18-234-186-29.compute-1.amazonaws.com
key
key_name
ssh -i python_automation_key ec2-user@ec2-18-234-186-29.compute-1.amazonaws.com
get_ipython().run_line_magic('ls', '')
ssh -i python_automation_key.pem ec2-user@ec2-18-234-186-29.compute-1.amazonaws.com
ssh ec2-user@ec2-18-234-186-29.compute-1.amazonaws.com -i python_automation_key.pem
inst.security_groups
sg = ec2.SecurityGroup(inst.security_groups[0]['GroupId'])
sg.authorize_ingress(IpPermissions=[{'FromPort': 22, 'ToPort': 22, 'IpProtocol': 'TCP', 'IpRanges': [{'CidrIp': '98.167.113.163'}]}])
sg.authorize_ingress(IpPermissions=[{'FromPort': 22, 'ToPort': 22, 'IpProtocol': 'TCP', 'IpRanges': [{'CidrIp': '98.167.113.163/32'}]}])
ssh ec2-user@ec2-18-234-186-29.compute-1.amazonaws.com -i python_automation_key.pem
sg.authorize_ingress(IpPermissions=[{'FromPort': 80, 'ToPort': 80, 'IpProtocol': 'TCP', 'IpRanges': [{'CidrIp': '0.0.0.0/0'}]}])
inst.public_dns_name
get_ipython().run_line_magic('history', '')
get_ipython().run_line_magic('save', 'ec2_example.py 1-46')
