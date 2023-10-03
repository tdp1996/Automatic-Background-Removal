from rembg import remove
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
        
        # Remove the background
        output_img = remove(input_img)
        
        # Get the full path for the output image
        output_file = os.path.join(output_path, img_file)
        
        # Save the output image
        output_img.save(output_file)


# if __name__ == "__main__":
#     input_path = 'data'
#     output_path = 'output'
#     remove_background(input_path, output_path)