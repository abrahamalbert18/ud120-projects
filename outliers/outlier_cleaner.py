#!/usr/bin/python

def getKey(item):
    return item[2]

def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    
    cleaned_data = []
    numOfOutliers = int(len(predictions)*0.1)
    ### your code goes here
    
    for i in range(len(predictions)):
        error = predictions[i] - net_worths[i]
        cleaned_data.append((ages[i],net_worths[i],error))
    
    cleaned_data.sort(key = getKey)
    outliers = cleaned_data[len(predictions)-numOfOutliers+1:]
    print "Outliers = ",outliers
    cleaned_data = cleaned_data[:len(predictions)-numOfOutliers]
    return cleaned_data

