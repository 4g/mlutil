import modeML as modeML
import sys
import numpy as np

#sample code for ModeML. 

def main(argv):    
    # create sample data
    num_train_samples = 50
    num_test_samples = 10    
    training_data , training_labels , test_data , correct_results = getSampleData(num_train_samples,num_test_samples)    
        
    # create an instance of modeML model and use it to fit data and then predict results
    model = modeML.modeML()
    model.fit(training_data,training_labels)    
    predicted_results = model.predict(test_data) # default method . will return a mode of results
    
    #predicted_results = model.predict(test_data , np.mean) # send a method alongwith data. Will return mean of results
    
    # show correct and predicted results
    for (i,j) in zip(correct_results,predicted_results):
        print "Correct = " , i , "Predicted = ", j
    
    # Calculate percentage accuracy
    accuracy = (1.0 - np.count_nonzero(np.subtract(correct_results,predicted_results))/(len(correct_results)*1.0))*100
    print "% accuracy = " , accuracy
        
        
# the function our model is trying to learn        
def function(x):
    return 1 if x*x + 2*x > 251000 else 0

# create data randomly
def getData(length):
    return [[np.random.randint(1,1000)] for x in range(1,length)]

#get labels for data using above stated function
def getLabels(data):
     return [function(x[0]) for x in data]

def getSampleData(ntr,nte):
    train_data , test_data =  getData(ntr) , getData(nte)
    return train_data , getLabels(train_data) , test_data , getLabels(test_data)
    
if __name__ == "__main__":
    main(sys.argv[1:])    
