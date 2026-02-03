import numpy as np
from glob import glob
from torchvision import transforms
from torch.utils.data import Dataset
import cv2
from glob import glob
from os import path

from steer_labels import LABELS, steering_to_class

class SteerDataSet(Dataset):
    
    def __init__(self,root_folder,img_ext = ".jpg" , transform=None):
        self.root_folder = root_folder
        self.transform = transform        
        self.img_ext = img_ext        
        self.filenames = glob(path.join(self.root_folder,"*" + self.img_ext))            
        self.totensor = transforms.ToTensor()
        self.class_labels = LABELS
        
    def __len__(self):        
        return len(self.filenames)
    
    def __getitem__(self,idx):
        f = self.filenames[idx]        
        img = cv2.imread(f)[120:, :, :]
        
        if self.transform == None:
            img = self.totensor(img)
        else:
            img = self.transform(img)   
        
        steering = path.split(f)[-1].split(self.img_ext)[0][6:]
        steering = float(steering)       

        steering_cls = steering_to_class(steering)
                      
        return img, steering_cls
