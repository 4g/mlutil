mlutil
======

Utilities for ML libraries in python  

1) modeML :   
  Mix any number of classifiers and get combined results. Simple to use:   
    Create : model =  modeML.modeML()  
    Fit    : model.fit(data,labels)  
    Predict: mode.predict(data)   
             will return statistical mode of all results [result which occurs most]  
             OR  
             model.predict(data,function)   
             to combine results using your own function   
    
