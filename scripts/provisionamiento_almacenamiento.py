import boto3

def provisionar_almacenamiento(config):
    s3 = boto3.client('s3')
    bucket_name = config['bucket_name']
    s3.create_bucket(Bucket=bucket_name)
    print(f'Bucket de almacenamiento creado: {bucket_name}')