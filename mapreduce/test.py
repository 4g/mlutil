import cvp
import cv2
import time , numpy as np

def func(img):
    for i in range(1,1000):
        img = cv2.blur(img,(3,3)) 
        img = cv2.dilate(img,(3,3)) 
        img = cv2.erode(img,(3,3)) 
    return img
    
def test():
    img = cv2.imread("test.jpg")     
    for i in range(0,3):
        img = cv2.pyrDown(img)  
                
    #MODE 0 TEST
    t1 = time.time()
    cvp.run(img,func,mode=0)    
    
    #MODE 1 TEST
    t2 = time.time()
    cvp.run(img,func,mode=1)

    #SERIAL PROCESS
    t3 = time.time()
    func(img)    
    
    t4 = time.time()
    
    
    print t2 - t1 , t3 - t2 , t4 - t3

test()
