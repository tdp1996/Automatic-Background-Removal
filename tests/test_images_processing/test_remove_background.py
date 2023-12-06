from images_processing.remove_background import remove_background
from prepare_model.download_model import download_model
import os
import tempfile


def test_remove_background():
    model_path = download_model('https://tdp-model.s3.ap-southeast-2.amazonaws.com/ABR_model/ABR_version_1.onnx', 'prepare_model/model')
    input_folder = 'tests/test_data'

    with tempfile.TemporaryDirectory() as temp_output_folder:
        remove_background(input_folder,temp_output_folder,model_path)

        assert len(os.listdir(temp_output_folder)) == len(os.listdir(input_folder))
