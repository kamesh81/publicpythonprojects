import json
import csv
import boto3

# Define the Lambda function.
def lambda_handler(event, context):
  # Get the S3 bucket name and object key from the event.
  bucket_name = event['Records'][0]['s3']['bucket']['name']
  object_key = event['Records'][0]['s3']['object']['key']

  # Create a DynamoDB client.
  dynamodb = boto3.client('dynamodb')

  # Read the CSV file from S3.
  with open('s3://{}/{}'.format(bucket_name, object_key), 'r') as f:
    reader = csv.reader(f)

    # Upsert the data into DynamoDB.
    for row in reader:
      dynamodb.put_item(
        TableName='my_table',
        Item={
          'column_1': row[0],
          'column_2': row[1],
          'column_3': row[2]
        }
      )

  return {
    'statusCode': 200,
    'body': json.dumps('Success!')
  }
