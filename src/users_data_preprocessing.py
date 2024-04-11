import os
import uuid
import streamlit as st


def get_unique_user_folder(folder_name: str) ->str:
    """
    Get the user-specific folder path based on the provided folder name.

    Args:
    - folder_name (str): Name of the folder to be created or accessed.

    Returns:
    - str: Path to the user-specific folder, combining the provided folder name with a unique session ID.
    """
    session_id = st.session_state.get("session_id", str(uuid.uuid4()))
    st.session_state.session_id = session_id
    return f"{folder_name}/{session_id}"


def create_user_folders(*folders: str):
    """
    Create user folders and delete all files within each folder if it already exists.

    Args:
    - *folders (str): Variable number of folder paths to be created.

    Returns:
    - None

    Notes:
    - If a folder already exists, all files within it will be deleted.
    - If a folder does not exist, it will be created along with any necessary parent directories.
    """
    for folder in folders:
        if not os.path.exists(folder):
            os.makedirs(folder)
        delete_files_in_folder(folder)


def delete_files_in_folder(folder_path: str):
    """
    Delete all files within the specified folder.

    Args:
    - folder_path (str): The path to the folder containing the files to be deleted.

    Returns:
    - None
    """
    if os.path.exists(folder_path) and os.path.isdir(folder_path):
        files = os.listdir(folder_path)
        for file in files:
            file_path = os.path.join(folder_path, file)
            if os.path.isfile(file_path):
                os.remove(file_path)
