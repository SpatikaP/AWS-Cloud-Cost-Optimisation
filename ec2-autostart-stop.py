import boto3

def lambda_handler(event,context):
    ec2=boto3.client('ec2')
    if event['action'] == 'start':
        start_instances(ec2,event)
    elif event['action'] == 'stop':
        stop_instances(ec2,event)

def start_instances(ec2, event):
    try:
        for instance_id in event['instanceid']:
            ec2.start_instances(InstanceIds=[instance_id])
    except Exception as e:
        print(e)

def stop_instances(ec2, event):
    try:
        for instance_id in event['instanceid']:
            ec2.stop_instances(InstanceIds=[instance_id])
    except Exception as e:
        print(e)
    
        

