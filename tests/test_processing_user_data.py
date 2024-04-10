import tempfile
import shutil
import os
from src.processing_user_data import create_user_folders, delete_files_in_folder, get_user_folder

def test_create_user_folders():
    
    with tempfile.TemporaryDirectory() as temp_folder_1, tempfile.TemporaryDirectory() as temp_folder_2:
        create_user_folders(temp_folder_1,temp_folder_2)
        
        assert os.path.exists(temp_folder_1) and len(os.listdir(temp_folder_1)) == 0
        assert os.path.exists(temp_folder_2) and len(os.listdir(temp_folder_2)) == 0


def test_delete_files_in_folder():
    test_folder = 'tests/data_test'
    
    with tempfile.TemporaryDirectory() as temp_test_folder:

        # Copy test data to temporary folders
        shutil.copytree(test_folder, temp_test_folder,dirs_exist_ok=True)
        
        delete_files_in_folder(temp_test_folder)

        assert len(os.listdir(temp_test_folder)) == 0

def test_get_user_folder():
    folder_name = 'processing_user_data/user_data/unprocessed_images'
    folder_path = get_user_folder(folder_name)
    assert folder_path.startswith('processing_user_data/user_data/unprocessed_images')