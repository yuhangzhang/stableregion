import os
import sys
import numpy as np
from PIL import Image

imset = []

for filename in os.listdir('/home/user/DATASETS/TRAIN_repository/VIC'):
    im = Image.open('/home/user/DATASETS/TRAIN_repository/VIC/'+filename).crop([0,0,1600,1000])
    imset.append(np.array(im))

    
def kmeans(imset, k, maxiter=20):
    # initiate stable region
    stableregion = []
    for i in range(k):
        stableregion.append(np.random.rand(1600,1000)>0.5)
        
    # initiate membership
    membership = []
    for i in range(k):
        membership.append([im for idx, im in enumerate(imset) if idx%k==i])
    
    
    for i in range(maxiter):
        print("iter "+str(i))
        center = []
        # with stableregion and membership, update center
        for j in range(k):
            average = np.zeros([1600,1000])
            for im in membership[j]:
                average = average + im*stabelregion[j]
            average = average/len(membership[j])
            center.append(average)
        center = np.array(center)
        
        # with stableregion and center, update membership
        membership = [[] for i in range(k)]
        for im in imset:
            assign = 0
            mindis = sys.float_info.max
            for j in range(k):
                diff = center[j]-im*stableregion[j]
                diff = np.fabs(diff).sum()
                if diff<mindis:
                    mindis = diff
                    assign = j
            membership[assign].append(im)
            
        membership = np.array(membership)

        # with membership, update stableregion
        variance = np.var(membership, axis=0)
        for j in range(k):
            median = np.median(variance[j])
            stableregion[j] = variance<median
    
    return stableregion, membership
             
region, grouping = kmeans(imset,10)
