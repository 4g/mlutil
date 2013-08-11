import cv2
import numpy  as np
import time 
from multiprocessing import Pool
import sys

def func(x):
    for i in range(1,50):
        x = cv2.blur(x,(3,3))
        x = cv2.flip(x,-1)
        x = cv2.dilate(x,(3,3))
        x = cv2.erode(x,(3,3))
    return x
    
def parallel(args):
    img = args
    n = 3
    img = cv2.split(img)
    pool = Pool(processes=n,)
    img = pool.map(func,img)  
    img = join(img)
    return img

def join(l):
    img = cv2.merge(l)   
    return img

def serial(args):
    img = args
    img = func(img)   
    return img

def measure(method , args):
    t1 = time.time()
    method(args)
    t2 = time.time()
    return t2 - t1

def check(m1,m2,args):
    return np.array_equal(m1(args), m2(args))
    

def getImage():
    img = cv2.imread("test.jpg")
    for i in range(0,0):
        img = cv2.pyrDown(img)
    return img   
    
img = getImage()    
print measure(serial,img)

img = getImage()    
print measure(parallel,img)

print check(serial,parallel,img)
