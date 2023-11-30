import os
from dotenv import load_dotenv
import boto3

# # Load environment variables from .env
# load_dotenv()

# def upload_folder_to_s3(local_folder,bucket_name):
#     # Retrieve AWS credentials from environment variables
#     aws_access_key_id = os.environ.get('AWS_ACCESS_KEY_ID')
#     aws_secret_access_key = os.environ.get('AWS_SECRET_ACCESS_KEY')
#     aws_region = os.environ.get('AWS_REGION')
#     # bucket_name = os.environ.get('AWS_BUCKET')

#     # Create an S3 client
#     s3 = boto3.client('s3', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key, region_name=aws_region)

#     # Iterate through each file in the local folder
#     for root, dirs, files in os.walk(local_folder):
#         for file in files:
#             local_file_path = os.path.join(root, file)
#             s3_key = os.path.relpath(local_file_path, local_folder).replace("\\", "/")

#             try:
#                 # Upload the file to S3
#                 s3.upload_file(local_file_path, bucket_name, s3_key)
#             except Exception as e:
#                 print(f"Error uploading {local_file_path}: {e}")

#     print('Upload successfully')

# upload_folder_to_s3('custom_U_2_Net/saved_models','tdp-model')

import os
import boto3

def download_folder(bucket_name, folder_prefix, local_folder):
    s3 = boto3.client('s3')

    # List objects in the bucket with the specified prefix
    response = s3.list_objects(Bucket=bucket_name, Prefix=folder_prefix)

    # Check if 'Contents' key is present in the response
    if 'Contents' in response:
        objects = response['Contents']
        
        # Download each object
        for obj in objects:
            key = obj['Key']
            local_path = os.path.join(local_folder, os.path.relpath(key, folder_prefix))

            # Create local directories if they don't exist
            os.makedirs(os.path.dirname(local_path), exist_ok=True)

            # Download the object
            s3.download_file(bucket_name, key, local_path)
    else:
        print(f"No objects found with prefix: {folder_prefix}")

if __name__ == "__main__":
    bucket_name = 'tdp-model'
    folder_prefix = 'ABR_model'
    local_folder = 'model'

    download_folder(bucket_name, folder_prefix, local_folder)






