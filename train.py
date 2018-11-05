import os
import numpy as np
from PIL import Image

imset = []

for filename in os.listdir('/home/user/DATASETS/TRAIN_repository/VIC'):
    imset.append(Image.open('/home/user/DATASETS/TRAIN_repository/VIC/'+filename))

    
def kmeans(imset, k):
    # initiate stable region
    stableregion = []
    for i in range(k):
        stableregion.append(np.random.rand(1600,1000)>0.5)
        
    # initiate membership
    membership = []
    for i in range(k):
        membership.append([im for idx, im in enumerate(imset) if idx%k==i])
    
    return membership


m = kmeans(imset, 5)

print(len(m))
