import os
from PIL import Image

imset = []

for filename in os.listdir('/home/user/DATASETS/TRAIN_repository/VIC'):
    imset.append(Image.open('/home/user/DATASETS/TRAIN_repository/VIC/'+filename))
    print('/home/user/DATASETS/TRAIN_repository/VIC/'+filename)
    
def kmeans(imset, k):
    pass
    
