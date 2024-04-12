import base64
import io
import os
import subprocess
from PIL import Image
import streamlit as st


def remove_background(input_folder: str, output_folder: str, model_path: str):
    """
    Remove background from images in the input folder using the specified model.

    Args:
    - input_folder (str): Path to the folder containing input images.
    - output_folder (str): Path to the folder where output images will be saved.
    - model_path (str): Path to the model used for background removal.

    Returns:
    - None
    """
    # List all files in the input folder
    input_files = sorted([f for f in os.listdir(input_folder) if os.path.isfile(os.path.join(input_folder, f))])

    # Create the output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    # Iterate through each input file
    for input_file in input_files:
        input_path = os.path.join(input_folder, input_file)
        output_path = os.path.join(
            output_folder, input_file
        )

        # Construct the command with double quotes around file paths
        command = f'rembg i -m u2net_custom -x \'{{"model_path": "{model_path}"}}\' "{input_path}" "{output_path}"'

        try:
            # Execute the command
            subprocess.run(command, shell=True, check=True)
        except subprocess.CalledProcessError as e:
            print(f"Error processing {input_file}: {e}")
    print("Processed all images")


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