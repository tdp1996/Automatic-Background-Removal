import os
import subprocess
from PIL import Image
from prepare_model.download_model import download_model
import io

def remove_background(input_image):
    model_path = get_latest_model('prepare_model/model')
    input_pil = Image.open(io.BytesIO(input_image))

    #Creat temporary files
    output_path = "output.png"
    input_path = "temp_input.png"
    input_pil.save(input_path)

    command = f'rembg i -m u2net_custom -x \'{{"model_path": "{model_path}"}}\' "{input_path}" "{output_path}"'
    subprocess.run(command, shell=True, check=True)

    output_pil = Image.open(output_path)

    # Clean up temporary files
    os.remove(input_path)
    os.remove(output_path)

    return output_pil

def get_latest_model(model_folder):
    model_folder= download_model('tdp-model','ABR_model','prepare_model/model')
    model_list =[file for file in os.listdir(model_folder) if file.startswith("ABR_version_")]
    sorted_model_files = sorted(model_list, key=lambda x: int(x[len("ABR_version_"):-len(".onnx")]))
    latest_model = sorted_model_files[-1]
    return os.path.join(model_folder,latest_model)








