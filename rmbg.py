from rembg import remove,new_session
from PIL import Image
import os

def remove_background(input_path, output_path):
     # Create the output directory if it doesn't exist
    os.makedirs(output_path, exist_ok=True)
    # Iterate over files in the input directory
    for img_file in os.listdir(input_path):
        # Get the full path of the input image
        img_path = os.path.join(input_path, img_file)
        
        # Open the input image
        input_img = Image.open(img_path)
        model_name = "isnet-general-use"
        session = new_session(model_name)
        # Remove the background
        output_img = remove(input_img,session=session,alpha_matting=True, alpha_matting_foreground_threshold=270,alpha_matting_background_threshold=20, alpha_matting_erode_size=11)
        
        # Get the full path for the output image
        output_file = os.path.join(output_path, img_file)
        
        # Save the output image
        output_img.save(output_file)

output_folder = 'data_loader'
image_folder = 'data'
remove_background(image_folder, output_folder)