"""
Take N (N >= 10) random 2-dimensional points represented in cartesian coordinate space.
Store them in a numpy array. Convert them to polar coordinates.
"""

import numpy as np
import random
import math

arr = np.random.randint(1,10,(10,2))
print(arr)

polarArr = np.zeros((10,2), dtype=float)

for i in range(10):
    r = math.sqrt(arr[i][0]**2 + arr[i][1]**2)
    Q = math.degrees(math.atan(arr[i][1]/arr[i][0]))

    r = round(r,2)
    polarArr[i][0] = r

    Q = round(Q,2) 
    polarArr[i][1] = Q
    
print(polarArr)