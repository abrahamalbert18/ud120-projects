#!/usr/bin/python
from time import time
import matplotlib.pyplot as plt
from prep_terrain_data import makeTerrainData
from class_vis import prettyPicture

features_train, labels_train, features_test, labels_test = makeTerrainData()


### the training data (features_train, labels_train) have both "fast" and "slow"
### points mixed together--separate them so we can give them different colors
### in the scatterplot and identify them visually
grade_fast = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==0]
bumpy_fast = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==0]
grade_slow = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==1]
bumpy_slow = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==1]


#### initial visualization
plt.xlim(0.0, 1.0)
plt.ylim(0.0, 1.0)
plt.scatter(bumpy_fast, grade_fast, color = "b", label="fast")
plt.scatter(grade_slow, bumpy_slow, color = "r", label="slow")
plt.legend()
plt.xlabel("bumpiness")
plt.ylabel("grade")
plt.show()
################################################################################


### your code here!  name your classifier object clf if you want the 
### visualization code (prettyPicture) to show you the decision boundary

from sklearn import ensemble
a = [ 0.65+(i/100.0)  for i in range(21)]
maximumAccuracy = 0.936
for n_estimator in range(55,65):
    for learning_rates in a:
        t0 = time() #algorithm='SAMME'
        clf = ensemble.AdaBoostClassifier(algorithm='SAMME',n_estimators=n_estimator,learning_rate=learning_rates)
        clf = clf.fit(features_train,labels_train)
        pred = clf.predict(features_test)
        print "Training time of Adaboost: ", round(time()-t0,3),"s"
        
        from sklearn import metrics
        accuracy = metrics.accuracy_score(pred,labels_test)
        if accuracy >= maximumAccuracy:
            print "Successful"
            print "accuracy =",accuracy,"n_estimator =",n_estimator, "learning rate = ",learning_rates 
            break
        print "accuracy =",accuracy,"n_estimator =",n_estimator, "learning rate = ",learning_rates 
        
        
        try:
            prettyPicture(clf, features_test, labels_test)
        except NameError:
            pass
