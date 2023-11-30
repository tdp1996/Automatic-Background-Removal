import os
import boto3
import streamlit as st


def download_model(bucket_name, folder_prefix, local_folder):

    # Retrieve AWS credentials from environment variables
    aws_access_key_id = st.secrets["AWS_ACCESS_KEY_ID"]
    aws_secret_access_key = st.secrets["AWS_SECRET_ACCESS_KEY"]
    aws_region = st.secrets["AWS_REGION"]

    # Create an S3 client
    s3 = boto3.client('s3', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key, region_name=aws_region)

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

    return local_folder
