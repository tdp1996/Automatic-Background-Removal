import os
import subprocess


def remove_background(input_folder: str, output_folder: str, model_path: str):
    """
    Remove background from images in the input folder using the specified model.

    Args:
    - input_folder (str): Path to the folder containing input images.
    - output_folder (str): Path to the folder where output images will be saved.
    - model_path (str): Path to the model used for background removal.

    Returns:
    - None
    """
    # List all files in the input folder
    input_files = sorted([f for f in os.listdir(input_folder) if os.path.isfile(os.path.join(input_folder, f))])

    # Create the output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    # Iterate through each input file
    for input_file in input_files:
        input_path = os.path.join(input_folder, input_file)
        output_path = os.path.join(
            output_folder, input_file
        )

        # Construct the command with double quotes around file paths
        command = f'rembg i -m u2net_custom -x \'{{"model_path": "{model_path}"}}\' "{input_path}" "{output_path}"'

        try:
            # Execute the command
            subprocess.run(command, shell=True, check=True)
        except subprocess.CalledProcessError as e:
            print(f"Error processing {input_file}: {e}")
    print("Processed all images")
