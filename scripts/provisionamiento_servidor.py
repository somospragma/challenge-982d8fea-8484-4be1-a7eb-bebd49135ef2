import boto3

def provisionar_servidor(config):
    ec2 = boto3.client('ec2')
    instance = ec2.run_instances(
        ImageId=config['image_id'],
        InstanceType=config['instance_type'],
        MinCount=1,
        MaxCount=1
    )
    print(f'Servidor provisionado: {instance['Instances'][0]['InstanceId']}')