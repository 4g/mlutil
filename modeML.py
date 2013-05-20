import sys, getopt
import config as config
import numpy as np

class modeML:
    models = dict()    
    lib = dict()
    
    # initialize empty dictionaries which will contain modules and models
    def __init__(self):            
        self.models = dict()
        self.lib = dict()
        self.empty = True
    
    # load all modules required as specified in config file
    def loadAll(self):        
        for family in config.classifiers:
           self.lib[family] = __import__(family)   
           self.lib[family] =  getattr(self.lib[family],family.split(".")[1])
           for classifier in config.classifiers[family]:                    
               self.models[classifier] = getattr(self.lib[family],classifier)()  

    # fit data into modules after initializing them if they are not yet created                           
    def fit(self,data,label):
        if self.empty:
            self.loadAll()                     
            self.empty = False                                             
        for family in config.classifiers:
            for classifier in config.classifiers[family]:   
                self.models[classifier] = self.models[classifier].fit(data,label)
        return self        
        
    # predict results from model and take mode to return most popular result
    def predict(self,data,method=None):
        results = []
        for family in config.classifiers:
            for classifier in config.classifiers[family]:
                results.append(self.models[classifier].predict(data))   
        results = np.array(results)
        
        if method == 1:
            return results       
        else:
            method = method if method is not None else self.mode                                                             
            return self.operate(results,method)
    
    def operate(self,results,method):
        return np.asarray([method(results[:,x]) for x in range(0,len(results[0]))])
        
    # result as mode of results
    def mode(self,results):      
        u, indices = np.unique(results, return_inverse=True)
        mode = u[np.argmax(np.bincount(indices))]
        return mode
