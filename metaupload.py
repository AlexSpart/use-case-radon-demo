import json
import os
import boto3
import logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

ARTIFACT_TABLE = os.environ['ARTIFACT_TABLE']
ARTIFACT_TABLE = 'artifacts-test'

def create_meta(event, context):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(ARTIFACT_TABLE)

    topic = event['Records'][0]


    bucket = topic['s3']['bucket']['name']

    artifact_name = topic['s3']['object']['key']

    if artifact_name.endswith('.jar') or artifact_name.endswith('.zip'):
        full_name = topic['s3']['object']['key']
        full_name_list = full_name.split('/')
        org_name = full_name_list[0]
        repo_name = full_name_list[1]
        artifact_object = full_name_list[-1]
        version = full_name_list[-2]
        artifact_name = full_name_list[-3]

        path = full_name.replace(artifact_object,"")
        group_id = full_name.split(artifact_name)[0]
        prefix = f"{org_name}/{repo_name}"
        group_id = group_id.split(prefix)[1]
        group_id = group_id.replace("/",".")
        
        items = {
            'artifactId': topic['s3']['object']['eTag'],
            'organization': org_name,
            'artifactName': artifact_name,
            'groupId':group_id[1:-1],
            'repositoryName':repo_name,
            'version': version,
            'updateAt': topic['eventTime'],
            'link': f"https://repo.cloudstash.io/{org_name}/{bucket}/{path}",
            'downloadCount': 0,
        }

        logger.info(f"full event: {topic}")
        logger.info(f"What triggered this event: {topic['eventSource']}")
        logger.info(f"Which bucket: {topic['s3']['bucket']['name']}")

        table.put_item(Item = items)
        response = {
            "statusCode": 200,
            "body": json.dumps(items)
        }

        return response
    else:
        return None