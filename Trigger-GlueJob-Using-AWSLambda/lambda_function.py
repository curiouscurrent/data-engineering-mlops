import boto3
import urllib.parse

glue = boto3.client('glue')

def lambda_handler(event, context):
    # Get bucket and file key from S3 event
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'])

    input_path = f's3://{bucket}/{key}'

    print(f"File uploaded: {input_path}")

    # Trigger Glue job
    response = glue.start_job_run(
        JobName='csv_to_json_glue_job',
        Arguments={
            '--input_path': input_path
        }
    )

    print("Glue job started:", response)

    return {
        'statusCode': 200,
        'body': 'Glue job triggered successfully'
    }
