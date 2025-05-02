import os
import boto3
from botocore.exceptions import NoCredentialsError


# AWS S3 Configuration
AWS_ACCESS_KEY = 'AKIAVREWOSMCWKX7MDWL'
AWS_SECRET_KEY = 'vDccK2YmOlOXVV/Xlwl9uUZMnrs0pUUpDN2DqLc+'
AWS_REGION = 'us-east-1'  # e.g., 'us-east-1'
S3_BUCKET_NAME = 'nutrition-food-images'

s3 = boto3.client(
    's3',
    aws_access_key_id=AWS_ACCESS_KEY,
    aws_secret_access_key=AWS_SECRET_KEY,
    region_name=AWS_REGION
)


def upload_image_to_s3(filename, file_path):
    try:
        s3.upload_file(file_path, S3_BUCKET_NAME, 'images/' + filename)
        print(f"File '{filename}' uploaded successfully to S3 bucket '{S3_BUCKET_NAME}'.")
    except FileNotFoundError:
        print("The file was not found.")
    except NoCredentialsError:
        print("Credentials not available.")