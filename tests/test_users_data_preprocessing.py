import os
import shutil
import tempfile
from src.users_data_preprocessing import create_user_folders, delete_files_in_folder, get_user_folder

def test_create_user_folders():   
    with tempfile.TemporaryDirectory() as temp_folder_1, tempfile.TemporaryDirectory() as temp_folder_2:
        create_user_folders(temp_folder_1,temp_folder_2)
        
        assert os.path.exists(temp_folder_1) and len(os.listdir(temp_folder_1)) == 0
        assert os.path.exists(temp_folder_2) and len(os.listdir(temp_folder_2)) == 0


def test_delete_files_in_folder():
    test_folder = 'tests/data_test'   
    with tempfile.TemporaryDirectory() as temp_test_folder:
        shutil.copytree(test_folder, temp_test_folder,dirs_exist_ok=True)
        
        delete_files_in_folder(temp_test_folder)

        assert len(os.listdir(temp_test_folder)) == 0

def test_get_user_folder():
    folder_name = 'user_data/unprocessed_images'
    folder_path = get_user_folder(folder_name)
    assert folder_path.startswith('user_data/unprocessed_images')