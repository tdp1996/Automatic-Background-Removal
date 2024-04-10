import os
import cv2
import glob
import numpy as np
import torch
from images_processing.RRDBNet import RRDBNet as arch 
import os.path as osp

def increase_image_resolution(input_image_folder, model_path):   
    model = arch.RRDBNet(3, 3, 64, 23, gc=32)
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')     
    model.load_state_dict(torch.load(model_path), strict=True)
    model.eval()
    model = model.to(device)

    idx = 0
    for path in glob.glob(f'{input_image_folder}/*'):
        idx += 1
        base = osp.splitext(osp.basename(path))[0]
        print(idx, base)
        try:
            # read images
            img = cv2.imread(path, cv2.IMREAD_COLOR)
            img = img * 1.0 / 255
            img = torch.from_numpy(np.transpose(img[:, :, [2, 1, 0]], (2, 0, 1))).float()
            img_LR = img.unsqueeze(0)
            img_LR = img_LR.to(device)

            with torch.no_grad():
                output = model(img_LR).data.squeeze().float().cpu().clamp_(0, 1).numpy()
            os.remove(path)
            output = np.transpose(output[[2, 1, 0], :, :], (1, 2, 0))
            output = (output * 255.0).round()
            cv2.imwrite(os.path.join(input_image_folder, '{:s}.png'.format(base)), output)
        except Exception as e:
            print(f"Failed to process image {base} due to an out-of-memory error. Skipping to the next image. Error: {e}")
            continue
    return input_image_folder
