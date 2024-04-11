import os
import streamlit as st
from PIL import Image
from src.remove_background import remove_background
import io
import base64
from download_model import download_model
from users_data_preprocessing import create_user_folders, get_user_folder
import torch
from images_processing.increase_resolution import increase_image_resolution


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
    input_images_folder = get_user_folder(
        "processing_user_data/user_data/unprocessed_images"
    )
    output_images_folder = get_user_folder(
        "processing_user_data/user_data/processed_images"
    )
    create_user_folders(input_images_folder, output_images_folder)

    if submitted and images is not None:
        for i, uploaded_file in enumerate(images):
            file_path = os.path.join(input_images_folder, f"image_{i}.png")
            with open(file_path, "wb") as f:
                f.write(uploaded_file.read())

    # If GPU support, increase image resolution before removing background
    if torch.cuda.is_available():
        IR_model_url = (
            "https://tdp-model.s3.ap-southeast-2.amazonaws.com/RRDB_ESRGAN_x4.pth"
        )
        input_images_folder = increase_image_resolution(
            input_images_folder, IR_model_url
        )

    # Images processing
    model_path = download_model(
        "https://tdp-model.s3.ap-southeast-2.amazonaws.com/ABR_model/ABR_version_1.onnx",
        "prepare_model/model",
    )
    remove_background(input_images_folder, output_images_folder, model_path)

    # Display processed images
    display_processed_images(input_images_folder, output_images_folder)


def display_processed_images(input_folder, output_folder):
    if os.path.exists(output_folder):
        output_files = sorted(os.listdir(output_folder))
        input_files = sorted(os.listdir(input_folder))
        for input_img, output_img in zip(input_files, output_files):
            # Display the original and edited images
            col1, col2 = st.columns(2)
            with col1:
                input_img_path = os.path.join(input_folder, input_img)
                st.image(
                    input_img_path,
                    caption=f"Original Image",
                    channels="RGB",
                    output_format="auto",
                )
            with col2:
                output_img_path = os.path.join(output_folder, output_img)
                st.image(
                    output_img_path,
                    caption=f"Edited Image: {output_img}",
                    channels="RGB",
                    output_format="auto",
                )
                download_link = create_download_link(output_img, output_img_path)
                st.markdown(download_link, unsafe_allow_html=True)


def create_download_link(filename, filepath):
    img_data = io.BytesIO()
    edited_image = Image.open(filepath)
    edited_image.save(img_data, format="PNG")
    img_data_base64 = base64.b64encode(img_data.getvalue()).decode("utf-8")
    return f'<a href="data:image/png;base64,{img_data_base64}" download="{filename}">Download image</a>'


if __name__ == "__main__":
    main()
