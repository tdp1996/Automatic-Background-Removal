from download_model import download_model
import os
import tempfile

def test_download_model():
    with tempfile.TemporaryDirectory() as temp_model_folder:
        s3_model_url = 'https://tdp-model.s3.ap-southeast-2.amazonaws.com/ABR_model/ABR_version_1.onnx'
        model_path = download_model(s3_model_url, temp_model_folder)
        assert os.path.exists(model_path)
        assert model_path.startswith(temp_model_folder)
        assert model_path.endswith('.onnx')