import cv2
import numpy as np
import time
from multiprocessing import Pool

size = (2000 , 2000)
t = time.time


def function(img):
    for i in range(0,img.shape[0]):
        for j in range(0,img.shape[1]):
            img[i][j] = np.random.randint(1,100)
    return img

def serial(array):    
    array = function(array)
    
def parallel(array):       
    pool = Pool(processes=4,)
    array = list(chunks(array,4))   
    array = pool.map(function,array)           

def chunks(l, n):
  for i in xrange(0, len(l), n):
    yield l[i:i+n]
    
def measure(method,args):
    t1 = t()
    method(args)
    t2 = t()
    return t2 - t1
    
    
array = np.zeros(size)
print measure(serial,array)

array = np.zeros(size)
print measure(parallel,array)

