import os
import subprocess

def remove_background(input_folder, output_folder):
    model_path = 'model/ARB.onnx'
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



