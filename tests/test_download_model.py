import os
import pytest
from src.download_model import download_model

@pytest.mark.skip(reason="Will run when refactored")
def test_download_model():
    model_path = download_model('https://tdp-model.s3.ap-southeast-2.amazonaws.com/ABR_model/ABR_version_1.onnx', 'prepare_model/model')
    assert os.path.exists(model_path)
    assert model_path.startswith('prepare_model/model')