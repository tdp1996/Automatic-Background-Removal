import streamlit as st
from rmbg import remove_background
import base64
import io
from prepare_model.download_model import download_model

def main():
    model_path = download_model('https://tdp-model.s3.ap-southeast-2.amazonaws.com/ABR_model/ABR_version_1.onnx', 'prepare_model/model')
    st.title(':blue[A]:red[B]:green[R] :sunglasses:')
    with st.form("my-form", clear_on_submit=True):
        images = st.file_uploader("Upload your images", type=None, accept_multiple_files=True)
        submitted = st.form_submit_button("Start!")

    if submitted and images is not None:
        for i, uploaded_file in enumerate(images):
            # Get the file content
            file_content = uploaded_file.read()

            # Call the remove_background function with the raw content
            edited_image = remove_background(file_content,model_path)

            # Display the original and edited images
            col1_name = f'col1_{i}'
            col2_name = f'col2_{i}'
            

            # Use dynamic column names
            globals()[col1_name], globals()[col2_name] = st.columns(2)
            with globals()[col1_name]:
                st.image(uploaded_file, caption=f'Original Image {i+1}',channels="RGB",output_format = "auto")
            with globals()[col2_name]:
                st.image(edited_image, caption=f'Edited Image {i+1}',channels="RGB",output_format = "auto")
                img_data = io.BytesIO()
                edited_image.save(img_data, format="PNG")
                img_data_base64 = base64.b64encode(img_data.getvalue()).decode("utf-8")

                download_link = f'<a href="data:image/png;base64,{img_data_base64}" download="Edited Image {i+1}.png">Download image</a>'
                st.markdown(download_link, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
