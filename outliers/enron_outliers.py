#!/usr/bin/python

import pickle
import sys
import matplotlib.pyplot
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit


### read in data dictionary, convert to numpy array
data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "r") )
features = ["salary", "bonus"]
data_dict.pop("TOTAL")
data = featureFormat(data_dict, features)



### your code below

outlier = []
#Plotting Data points
for point in data:
    salary = point[0]
    bonus = point[1]
    if bonus >= 5000000 and salary > 1000000:
        outlier.append((salary,bonus))
    matplotlib.pyplot.scatter( salary, bonus )

matplotlib.pyplot.xlabel("salary")
matplotlib.pyplot.ylabel("bonus")
matplotlib.pyplot.show()

print "Outlier : ",outlier

# 
# for i in enron_data.keys():
#     if enron_data[i]["bonus"]== data.max():
#         print "Name :",i