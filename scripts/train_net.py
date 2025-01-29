import torch
import torchvision.transforms as transforms
import os
from torch.utils.data import DataLoader
import numpy as np
import torchvision
import matplotlib.pyplot as plt

from steerDS import SteerDataSet

transform = transforms.Compose(
[transforms.ToTensor(),
    transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))])

def imshow(img):
    img = img / 2 + 0.5 #unnormalize
    npimg = img.numpy()
    plt.imshow(np.transpose(npimg, (1, 2, 0)))
    plt.show()

#### Setup the training dataset
script_path = os.path.dirname(os.path.realpath(__file__))

train_ds = SteerDataSet(os.path.join(script_path, '..', 'data', 'train_starter'), '.jpg', transform)
print("The train dataset contains %d images " % len(train_ds))

trainloader = DataLoader(train_ds,batch_size=8,shuffle=True)
all_y = []
for S in trainloader:
    im, y = S    
        
    all_y += y.tolist()

print(f'Input shape: {im.shape}')

all_lbls, all_counts = np.unique(all_y, return_counts = True)
plt.bar(all_lbls, all_counts, width = 0.05)
plt.xlabel('Labels')
plt.ylabel('Counts')
plt.xticks(all_lbls)
plt.show()

example_ims, example_lbls = next(iter(trainloader))
# show images and print labels
print(' '.join(f'{example_lbls[j]}' for j in range(len(example_lbls))))
imshow(torchvision.utils.make_grid(example_ims))

