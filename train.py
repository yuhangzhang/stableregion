import os
from PIL import Image

imset = []

for filename in os.listdir('/home/user/DATASETS/TRAIN_repository/VIC'):
    imset.append(Image.open(filename))
    print(file)
    
def kmeans(imset, k):
    pass
    
