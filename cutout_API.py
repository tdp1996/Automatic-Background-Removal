import os
import requests

def remove_background(folder_path,output_folder_path,API_key):
  # Tạo thư mục đầu ra nếu chưa tồn tại
  if not os.path.exists(output_folder_path):
      os.makedirs(output_folder_path)

  # Lặp qua các tệp tin trong thư mục
  for file_name in os.listdir(folder_path):
      # Kiểm tra nếu tệp tin là ảnh
      if file_name.endswith('.jpg') or file_name.endswith('.png'):
          # Tạo đường dẫn đầy đủ đến tệp tin
          file_path = os.path.join(folder_path, file_name)
          
          response = requests.post(
              'https://www.cutout.pro/api/v1/matting?mattingType=6',
              files={'file': open(file_path, 'rb')},
              headers={'APIKEY': API_key},
          )
          
          # Tạo tên tệp tin đầu ra bằng cách thay đổi phần mở rộng của tệp tin gốc
          output_file_name = os.path.splitext(file_name)[0] + '_matting.png'
          output_file_path = os.path.join(output_folder_path, output_file_name)
          
          with open(output_file_path, 'wb') as out:
              out.write(response.content)


# folder_path = 'data'
# output_folder_path = 'output'  # Đường dẫn đến thư mục đầu ra
# remove_background(folder_path,output_folder_path)
