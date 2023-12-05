import os
import subprocess
from PIL import Image
import io

def remove_background(input_image, model_path):
    input_pil = Image.open(io.BytesIO(input_image))

    # Create temporary files
    output_path = "output.png"
    input_path = "temp_input.png"
    
    try:
        # Save input image
        input_pil.save(input_path)

        # Construct the command with double quotes around file paths
        command = f'rembg i -m u2net_custom -x \'{{"model_path": "{model_path}"}}\' "{input_path}" "{output_path}"'
        
        # Run the command
        subprocess.run(command, shell=True, check=True)

        # Open the output image and return as PIL Image
        output_pil = Image.open(output_path)

        return output_pil

    finally:
        # Clean up temporary files in a 'finally' block to ensure it happens even if an exception occurs
        os.remove(input_path)
        os.remove(output_path)












