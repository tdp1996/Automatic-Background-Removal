import os
import subprocess
from pathlib import Path
import glob

def remove_background(input_folder, output_folder):
    model_path = _prepare_model('https://github.com/tdp1996/model.git')
    # List all files in the input folder
    input_files = [f for f in os.listdir(input_folder) if os.path.isfile(os.path.join(input_folder, f))]

    # Create the output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    # Iterate through each input file
    for input_file in input_files:
        input_path = os.path.join(input_folder, input_file)
        output_path = os.path.join(output_folder, input_file.replace('.png', '_output.png'))  # Adjust output file name as needed

        # Construct the command with double quotes around file paths
        command = f'rembg i -m u2net_custom -x \'{{"model_path": "{model_path}"}}\' "{input_path}" "{output_path}"'

        try:
            # Execute the command
            subprocess.run(command, shell=True, check=True)
            print(f"Processed: {input_file}")
        except subprocess.CalledProcessError as e:
            print(f"Error processing {input_file}: {e}")

def _prepare_model(model_link):
    model_path = Path('model')  # Create a Path object

    if not model_path.exists():
        clone_command = f'git clone {model_link} model'
        try:
            # Execute the command
            subprocess.run(clone_command, shell=True, check=True)
            print(f"Repository cloned successfully")
        except subprocess.CalledProcessError as e:
            print(f"Error cloning repository: {e}")
    else:
        # Repository already exists, pull to update
        pull_command = 'git pull'
        try:
            # Execute the command
            subprocess.run(pull_command, cwd='model', shell=True, check=True)
            print(f"Repository updated successfully")
        except subprocess.CalledProcessError as e:
            print(f"Error updating repository: {e}")

    # Find all files with the .onnx extension in the folder
    onnx_files = glob.glob(os.path.join('model', '*.onnx'))

    # Check if there are any .onnx files
    if onnx_files:
        # If there is at least one .onnx file, get the name of the first file
        model_path = onnx_files[0]
        return model_path
    else:
        return None  # Return None if there are no .onnx files
