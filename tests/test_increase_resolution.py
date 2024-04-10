from images_processing.increase_resolution import increase_image_resolution
from download_model import download_model
import tempfile
import shutil
import os
import torch

def test_increase_image_resolution():
    if torch.cuda.is_available():
        with tempfile.TemporaryDirectory() as temp_model_folder:
            model_url = "https://tdp-model.s3.ap-southeast-2.amazonaws.com/RRDB_ESRGAN_x4.pth"
            model_path = download_model(model_url,temp_model_folder)
            test_folder = "tests/test_data"
            with tempfile.TemporaryDirectory() as temp_test_folder:

                # Copy test data to temporary folders
                shutil.copytree(test_folder, temp_test_folder, dirs_exist_ok=True)

                temp_output_folder = increase_image_resolution(temp_test_folder, model_path)
                assert len(os.listdir(temp_output_folder)) == len(os.listdir(test_folder)) 
                
                test_files = sorted([f for f in os.listdir(test_folder) if os.path.isfile(os.path.join(test_folder, f))])
                temp_output_files = sorted([f for f in os.listdir(test_folder) if os.path.isfile(os.path.join(test_folder, f))])
                for test_file, temp_output_file in zip(test_files,temp_output_files):
                    assert test_file == temp_output_file
