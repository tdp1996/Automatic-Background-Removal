import os
from zipfile import ZipFile
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

def zip_and_upload(folder_path, zip_name, drive_folder_id):
    # Compress folders
    with ZipFile(zip_name, 'w') as zipf:
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                file_path = os.path.join(root, file)
                arcname = os.path.relpath(file_path, folder_path)
                zipf.write(file_path, arcname)

    # Create a connection to Google Drive
    gauth = GoogleAuth()
    gauth.LocalWebserverAuth()  # Check the browser and authenticate
    drive = GoogleDrive(gauth)

    # Upload file zip to Google Drive
    file_drive = drive.CreateFile({'title': zip_name, 'parents': [{'id': drive_folder_id}]})
    file_drive.Upload()

    os.remove("TDP_Data.zip")

if __name__ == "__main__":
    folder_to_zip = "TDP_Data"
    zip_file_name = "TDP_Data.zip"
    drive_folder_id = "1BXiSlnq0pKc3bos_YW7LzVH1YwlG5lgX"

    zip_and_upload(folder_to_zip, zip_file_name, drive_folder_id)