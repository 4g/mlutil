import cv2
import numpy as np
from filter import compose

rand = compose([                
                lambda x : np.random.rand(x[0],x[1],x[2]),
                lambda x : np.multiply(x,20.0),
                lambda x : np.asarray(x,np.uint8)
                ])

clean = compose([
                 cv2.pyrDown , 
                 cv2.pyrUp , 
                 lambda x:cv2.blur(x,(3,3))
                ])           
                 
morph = compose([
                 lambda x:cv2.dilate(x,(3,3)) ,
                 lambda x:cv2.erode(x,(3,3)) , 
                 lambda x:cv2.threshold(x,10,255,cv2.THRESH_BINARY)[1],
                 cv2.pyrUp ,
                 cv2.pyrDown
                ])

show  = compose([
                lambda x:cv2.imshow("w",x),
                lambda y:cv2.waitKey(0)    
               ])
                
                
chain = compose([
                clean,
                morph
                ])                
                
x = rand([100,100,3])   
show(x)
x = chain(x)    
show(x)


