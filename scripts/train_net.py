import torch
import torchvision.transforms as transforms
import os
from torch.utils.data import DataLoader
import numpy as np

from steerDS import SteerDataSet

transform = transforms.Compose(
[transforms.ToTensor(),
    transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))])

script_path = os.path.dirname(os.path.realpath(__file__))


ds = SteerDataSet(os.path.join(script_path, '..', 'data', 'train'), '.jpg', transform)

print("The dataset contains %d images " % len(ds))

ds_dataloader = DataLoader(ds,batch_size=1,shuffle=True)
all_y = []
for S in ds_dataloader:
    im, y = S    
        
    all_y += y.tolist()

print(f'Input shape: {im.shape}')
print('Outputs and their counts:')
print(np.unique(all_y, return_counts = True))
