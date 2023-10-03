import os
import streamlit as st
from PIL import Image
from rmbg import remove_background
import tempfile
import base64

st.title('AUTOMATIC BACKGROUND REMOVAL')
image_folder = 'uploads'  # Tên thư mục để lưu các ảnh được tải lên

# Tạo thư mục để lưu ảnh nếu chưa tồn tại
if not os.path.exists(image_folder):
    os.makedirs(image_folder)

images = st.file_uploader("Upload your images", type=None, accept_multiple_files=True)

# Lưu các ảnh vào thư mục
if images is not None:
    for i, img in enumerate(images):
        # Lưu ảnh với tên file duy nhất
        file_path = os.path.join(image_folder, f"image_{i}.png")
        with open(file_path, 'wb') as f:
            f.write(img.read())
        st.write(f"Image {i+1} uploaded successfully!")

output_folder = 'data_loader'

remove_background(image_folder, output_folder)
# Xử lý các ảnh đã được tải lên
if os.path.exists(output_folder):
    image_files = os.listdir(output_folder)
    for i,image_file in enumerate(image_files):
        # Đọc ảnh từ thư mục
        image_path = os.path.join(output_folder, image_file)
        img = Image.open(image_path)
        # Tạo tệp tạm thời
        with tempfile.NamedTemporaryFile(suffix='.png', delete=False) as temp_file:
            temp_file_path = temp_file.name
            img.save(temp_file_path)
        
        # Hiển thị ảnh và liên kết tải xuống
        st.image(img, caption=f'Edited Image {i+1}')
        
        # Đọc dữ liệu từ tệp tạm thời
        with open(temp_file_path, "rb") as file:
            img_data = file.read()
        
        # Mã hóa dữ liệu ảnh thành base64
        img_data_base64 = base64.b64encode(img_data).decode("utf-8")
        
        # Tạo liên kết tải xuống với dữ liệu base64
        download_link = f'<a href="data:image/png;base64,{img_data_base64}" download="Edited Image {i+1}.png">Download image</a>'
        
        # Hiển thị liên kết tải xuống
        st.markdown(download_link, unsafe_allow_html=True)


