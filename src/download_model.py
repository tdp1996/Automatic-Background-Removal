import os
import gdown
from pathlib import Path

def download_model(model_folder: Path) ->Path:
    """
    Download a model from Google Drive and save it to the specified folder.

    Args:
    - model_folder (Path): Path to the directory where the model will be saved.

    Returns:
    - Path: Path to the downloaded model file.
    """
    if not os.path.exists(model_folder):
        os.makedirs(model_folder)
    url = 'https://drive.google.com/uc?id=1vDmBJWMoWjhP0LyTZ-b8eXqwM9EohKHI'
    output = 'ABR.onnx'
    model_path = os.path.join(model_folder, output)
    if not Path(model_path).exists():
        gdown.download(url, model_path, quiet=False)

    return model_path
