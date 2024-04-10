import os
import streamlit as st
import uuid

def create_user_folders(*folders):
    for folder in folders:
        if not os.path.exists(folder):
            os.makedirs(folder)
        delete_files_in_folder(folder)

def delete_files_in_folder(folder_path):
    if os.path.exists(folder_path) and os.path.isdir(folder_path):
        files = os.listdir(folder_path)
        for file in files:
            file_path = os.path.join(folder_path, file)
            try:
                if os.path.isfile(file_path):
                    os.remove(file_path)
            except Exception as e:
                print(f"Error deleting {file_path}: {e}")

def get_user_folder(folder_name):
    session_id = st.session_state.get('session_id', str(uuid.uuid4()))
    st.session_state.session_id = session_id
    return f"{folder_name}/{session_id}"