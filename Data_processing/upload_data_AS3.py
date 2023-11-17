import boto3
import os
import json

def upload_folder_to_s3(config_file, local_folder, s3_prefix):
    # Create an S3 client
    aws_access_key_id, aws_secret_access_key, aws_region, bucket_name = load_aws_credentials(config_file)

    # Create an S3 client
    s3 = boto3.client('s3', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key, region_name=aws_region)

    # Iterate through each file in the local folder
    for root, dirs, files in os.walk(local_folder):
        for file in files:
            local_file_path = os.path.join(root, file)
            s3_key = os.path.join(s3_prefix, os.path.relpath(local_file_path, local_folder)).replace("\\", "/")

            try:
                # Upload the file to S3
                s3.upload_file(local_file_path, bucket_name, s3_key)
                print(f"Upload successful: {local_file_path} to s3://{bucket_name}/{s3_key}")
            except Exception as e:
                print(f"Error uploading {local_file_path}: {e}")

def load_aws_credentials(file_path):
    with open(file_path, 'r') as config_file:
        config = json.load(config_file)
        return config['aws_access_key_id'], config['aws_secret_access_key'], config['aws_region'], config['aws_bucket']
    

if __name__ == "__main__":
    # Replace these values with your actual AWS credentials and S3 information

    config_file="/Users/admin/Desktop/Automatic-Batch-Editing/Data_processing/config.json"
    local_folder_path = "/Users/admin/Desktop/Automatic-Batch-Editing/Data"  # Replace with the path to your local folder
    s3_prefix = "user_data"  # Replace with the desired prefix in your S3 bucket

    # Upload the folder to S3
    upload_folder_to_s3(config_file, local_folder_path, s3_prefix)
