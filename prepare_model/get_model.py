import os
import boto3

def download_model(bucket_name, folder_prefix, local_folder):
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

    return local_folder

if __name__ == "__main__":
    bucket_name = 'tdp-model'
    folder_prefix = 'ABR_model'
    local_folder = 'prepare_model/model'

    download_model(bucket_name, folder_prefix, local_folder)