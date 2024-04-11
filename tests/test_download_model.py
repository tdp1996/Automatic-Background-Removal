import tempfile
from src.download_model import download_model

def test_download_model():
    with tempfile.TemporaryDirectory() as temp_model_folder:     
        model_path = download_model(temp_model_folder)
        assert model_path.startswith(temp_model_folder)
        assert model_path.endswith('ABR.onnx')