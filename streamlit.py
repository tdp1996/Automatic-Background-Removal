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
    user_folder = get_user_folder('user_data/unprocessed_images')

    if not os.path.exists(user_folder):
        os.makedirs(user_folder)

    uploaded_successfully = False

    if images is not None:
        for i, img in enumerate(images):
            file_path = os.path.join(user_folder, f"image_{i}.png")
            with open(file_path, 'wb') as f:
                f.write(img.read())
            
            if not uploaded_successfully:
                uploaded_successfully = True
                st.write("All images uploaded successfully!")

    if uploaded_successfully:
        output_folder = get_user_folder('user_data/processed_images')
        remove_background(user_folder, output_folder)
        shutil.rmtree(user_folder)
        if os.path.exists(output_folder):
            image_files = os.listdir(output_folder)
            for i, image_file in enumerate(image_files):
                image_path = os.path.join(output_folder, image_file)
                img = Image.open(image_path)

                st.image(img, caption=f'Edited Image {i+1}',channels="RGB",output_format = "auto")

                with tempfile.NamedTemporaryFile(suffix='.png', delete=False) as temp_file:
                    temp_file_path = temp_file.name
                    img.save(temp_file_path)

                with open(temp_file_path, "rb") as file:
                    img_data = file.read()

                img_data_base64 = base64.b64encode(img_data).decode("utf-8")

                download_link = f'<a href="data:image/png;base64,{img_data_base64}" download="Edited Image {i+1}.png">Download image</a>'
                st.markdown(download_link, unsafe_allow_html=True)


def get_user_folder(folder_name):
    session_id = st.session_state.get('session_id', str(uuid.uuid4()))
    st.session_state.session_id = session_id
    return f"{folder_name}/{session_id}"
if __name__ == "__main__":
    main()
