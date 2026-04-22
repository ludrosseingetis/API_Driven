import boto3
import os

# On récupère l'URL LocalStack via les variables d'environnement
endpoint_url = "http://localhost:4566"
ec2 = boto3.client('ec2', endpoint_url=endpoint_url, region_name='us-east-1')

def lambda_handler(event, context):
    # On récupère l'action (start ou stop) et l'ID de l'instance
    action = event.get('action')
    instance_id = event.get('instance_id')
    
    if action == 'start':
        ec2.start_instances(InstanceIds=[instance_id])
        return {"statusCode": 200, "body": f"Instance {instance_id} démarrée"}
    elif action == 'stop':
        ec2.stop_instances(InstanceIds=[instance_id])
        return {"statusCode": 200, "body": f"Instance {instance_id} arrêtée"}
    
    return {"statusCode": 400, "body": "Action non reconnue"}
