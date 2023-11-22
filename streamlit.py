import os
import streamlit as st
from PIL import Image
from rmbg import remove_background
import tempfile
import base64
import uuid
import shutil


def main():
    st.title(':blue[A]:red[B]:green[R] :sunglasses:')

    images = st.file_uploader("Upload your images", type=None, accept_multiple_files=True)
    # Get the user's folder
    user_folder = get_user_folder('user_data/unprocessed_images')

    # Create a folder to save images if it does not exist
    if not os.path.exists(user_folder):
        os.makedirs(user_folder)

    # Save images to the folder
    uploaded_successfully = False  # Variable to track whether images have been uploaded successfully
    if images is not None:
        for i, img in enumerate(images):
            # Save images with unique file names
            file_path = os.path.join(user_folder, f"image_{i}.png")
            with open(file_path, 'wb') as f:
                f.write(img.read())
            
            # Set the variable to True after the first successful upload
            if not uploaded_successfully:
                uploaded_successfully = True
                st.write("All images uploaded successfully!")  # Display only once

    # Proceed only if images have been uploaded successfully
    if uploaded_successfully:
        output_folder = get_user_folder('user_data/processed_images')
        remove_background(user_folder, output_folder)
        # shutil.rmtree(user_folder)
        
        # Process uploaded images
        if os.path.exists(output_folder):
            image_files = os.listdir(output_folder)
            for i, image_file in enumerate(image_files):
                # Read the image from the folder
                image_path = os.path.join(output_folder, image_file)
                img = Image.open(image_path)

                # Create a temporary file
                with tempfile.NamedTemporaryFile(suffix='.png', delete=False) as temp_file:
                    temp_file_path = temp_file.name
                    img.save(temp_file_path)

                # Display the image and download link
                st.image(img, caption=f'Edited Image {i+1}')

                # Read data from the temporary file
                with open(temp_file_path, "rb") as file:
                    img_data = file.read()

                # Encode image data to base64
                img_data_base64 = base64.b64encode(img_data).decode("utf-8")

                # Create a download link with base64-encoded data
                download_link = f'<a href="data:image/png;base64,{img_data_base64}" download="Edited Image {i+1}.png">Download image</a>'

                # Display the download link
                st.markdown(download_link, unsafe_allow_html=True)


def get_user_folder(folder_name):
    session_id = st.session_state.get('session_id', str(uuid.uuid4()))
    st.session_state.session_id = session_id
    return f"{folder_name}/{session_id}"
if __name__ == "__main__":
    main()
