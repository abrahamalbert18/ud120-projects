#!/usr/bin/python


"""
    Starter code for the validation mini-project.
    The first step toward building your POI identifier!

    Start by loading/formatting the data

    After that, it's not our code anymore--it's yours!
"""

import pickle
import sys
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit

data_dict = pickle.load(open("../final_project/final_project_dataset.pkl", "r") )

### first element is our labels, any added elements are predictor
### features. Keep this the same for the mini-project, but you'll
### have a different feature list when you do the final project.
features_list = ["poi", "salary"]

data = featureFormat(data_dict, features_list)
labels, features = targetFeatureSplit(data)

#print labels[:10],features[:10]

### it's all yours from here forward!  
from sklearn.cross_validation import train_test_split
from sklearn.tree import DecisionTreeClassifier
# from sklearn.model_selection import cross_val_score
from sklearn.metrics import accuracy_score

# kf = KFold(len(labels),2)
# for train_indices,test_indices in kf:
    # features_train = [features[i] for i in train_indices]
    # features_test =  [features[i] for i in test_indices]
    # labels_train = [labels[i] for i in train_indices]
    # labels_test = [labels[i] for i in test_indices]
    #     

features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size=0.3, random_state=42)
clf = DecisionTreeClassifier()
clf = clf.fit(features_train,labels_train)
pred = clf.predict(features_test)

accuracy = accuracy_score(pred,labels_test)
print accuracy    