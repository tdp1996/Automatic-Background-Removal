import os
import streamlit as st
from src.image_processing import display_processed_images, remove_background
from src.download_model import download_model
from src.users_data_preprocessing import create_user_folders, get_unique_user_folder


def main():
    st.set_page_config(
        page_title="ABR",
        layout="centered",
    )
    st.title(" ✨ :blue[A]:red[B]:green[R] ✨ ")
    with st.form("my-form", clear_on_submit=True):
        images = st.file_uploader(
            "Upload your images", type=None, accept_multiple_files=True
        )
        submitted = st.form_submit_button("Start!")

    # Create folders for unprocessed and processed images
    input_images_folder = get_unique_user_folder(
        "user_data/unprocessed_images"
    )
    output_images_folder = get_unique_user_folder(
        "user_data/processed_images"
    )
    create_user_folders(input_images_folder, output_images_folder)

    if submitted and images is not None:
        for i, uploaded_file in enumerate(images):
            file_path = os.path.join(input_images_folder, f"image_{i}.png")
            with open(file_path, "wb") as f:
                f.write(uploaded_file.read())

    # Images processing
    model_path = download_model("model")
    remove_background(input_images_folder, output_images_folder, model_path)

    # Display processed images
    display_processed_images(input_images_folder, output_images_folder)


if __name__ == "__main__":
    main()
