import os
from PIL import Image

imset = []

for filename in os.listdir('/home/user/DATASETS/TRAIN_repository/VIC):
    imset.append(Image.open(file))
    print(file)
    
def kmeans(imset, k):
    pass
    