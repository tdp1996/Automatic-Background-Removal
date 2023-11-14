from split_images_by_format import split_data

import boto3
from botocore.exceptions import NoCredentialsError

def upload_to_s3(local_path, bucket_name):
    # Create an S3 client
    s3 = boto3.client('s3')

    try:
        # Upload the files
        s3.upload_file(local_path, bucket_name, local_path)
        print(f"Successfully uploaded {local_path} to {bucket_name}")
    except NoCredentialsError:
        print("Credentials not available or not valid.")

if __name__ == "__main__":
    # Set your AWS credentials and region (you can also set them using aws configure)
    aws_access_key_id = "AKIAVXQ6TRPE6R7QI2NS"
    aws_secret_access_key = "9rvKSdfuxXZHdVSjVKZOOogZ8UJMoEit503uqJ8P"
    aws_region = "ap-southeast-2"

    # Set the local folder path and S3 bucket name
    local_folder_path = "jpg"
    s3_bucket_name = "tdp-dataset"

    # Configure AWS credentials
    boto3.setup_default_session(
        aws_access_key_id=aws_access_key_id,
        aws_secret_access_key=aws_secret_access_key,
        region_name=aws_region
    )

    # Upload to S3
    upload_to_s3(local_folder_path, s3_bucket_name)

