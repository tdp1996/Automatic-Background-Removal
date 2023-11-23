import os
import shutil

def split_data(input_folder, jpg_folder, png_folder):

    # Create jpg and png folders if they do not exist
    if not os.path.exists(jpg_folder):
        os.makedirs(jpg_folder)
    if not os.path.exists(png_folder):
        os.makedirs(png_folder)

    # Get a list of all image files in the input folder
    image_files = [f for f in os.listdir(input_folder) if f.lower().endswith(('.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff'))]

    # Split images into jpg or png folders
    for image_file in image_files:
        base_name = os.path.splitext(image_file)[0]
        image_format = os.path.splitext(image_file)[1].lower()

        # Check the format and move the image to the corresponding folder
        if image_format == '.jpg' or image_format == '.jpeg':
            shutil.move(os.path.join(input_folder, image_file), os.path.join(jpg_folder, image_file))
        elif image_format == '.png':
            shutil.move(os.path.join(input_folder, image_file), os.path.join(png_folder, image_file))


if __name__ == "__main__":
# Change the paths to your input folder and define the output folders for jpg and png images
    input_folder_path = 'Raw_Images'
    jpg_output_folder_path = 'Data/TDP_test_data/TDP_IMAGES'
    png_output_folder_path = 'Data/TDP_test_data/TDP_MASKS'

    split_data(input_folder_path, jpg_output_folder_path, png_output_folder_path)
