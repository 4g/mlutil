import cv2
import numpy  as np
from multiprocessing import Pool

def run(img,func,n=None,mode=0,window=None):
    if mode is 0:        
        img = cv2.split(img)
        n = len(img) if n is None else n
        img = process(img,func,n)
        img = cv2.merge(img)   
            
    if mode is 1:
        n = 4 if n is None else n
        img = np.array_split(img,n)        
        img = process(img,func,n)                  
        img = np.concatenate(img)
        
    if mode is 2:
        n = 4 if n is None else n
        w = 3 if window is None else window
        size = len(img)/n
        img = [img[max(i-w,0):min(i+size+w,len(img))] for i in range(0,len(img),size)]        
        img = process(img,func,n)                  
        img = [i[w:len(i)-w] for i in img]            
        img = np.concatenate(img)
        
    return img    
        
def process(img,func,n):
    pool = Pool(processes=n,)    
    img = pool.map(func,img) 
    pool.close()
    return img 

