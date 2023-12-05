import requests
import os

def download_model(s3_object_url, model_folder):
    # Create the target directory if it doesn't exist
    if not os.path.exists(model_folder):
        os.makedirs(model_folder)
    s3_object_response = requests.get(s3_object_url)

    if s3_object_response.status_code == 200:
        file_name = s3_object_url.split("/")[-1]
        model_path = os.path.join(model_folder, file_name)
        if not os.path.isfile(model_path):
            # save the model
            with open(model_path, 'wb') as local_file:
                local_file.write(s3_object_response.content)
    else:
        print(f"Download failed. Status code: {s3_object_response.status_code}")
    return model_path