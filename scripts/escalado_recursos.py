import boto3

def escalar_recursos(config):
    ec2 = boto3.client('ec2')
    instances = ec2.describe_instances(InstanceIds=config['instance_ids'])['Reservations'][0]['Instances']
    for instance in instances:
        ec2.modify_instance_attribute(InstanceId=instance['InstanceId'], InstanceType={'Value': config['new_instance_type']})
    print('Recursos escalados.')