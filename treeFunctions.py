# *****************************************
# Final Project - Decision tree functions
# *****************************************
# COLLABORATION STATEMENTS:
# https://mljar.com/blog/visualize-decision-tree/
# https://www.geeksforgeeks.org/python-decision-tree-regression-using-sklearn/
# https://scikit-learn.org/stable/modules/generated/sklearn.metrics.accuracy_score.html
# https://scikit-learn.org/stable/modules/tree.html
# *****************************************

# *****************************************
# Import statements
# *****************************************
import numpy as np
from sklearn import tree
from sklearn import metrics

# *****************************************
# Functions
# *****************************************

'''
PURPOSE: exports the decision tree classifier to a new file 
"tree.dot" to be visualized using http://www.webgraphviz.com/
PARAMETERS: classifier to be exported, class names 
(low, high, etc), features labels (ID, Num of Bathrooms, etc)
RETURNS: nothing, but creates a file "tree.dot"
'''
def exportTree(classifier, classNames, labels):
    tree.export_graphviz(classifier, 
                    out_file="tree.dot", 
                    feature_names=labels,
                    class_names=classNames)
                    
    print("Exporting tree.dot\n")

'''
PURPOSE: creates a training test, use it to evaluate the
accuracy of the decision tree classifier
PARAMETERS: classifier, X (features), y (classes) 
RETURNS: calculated accuracy
'''
def testAccuracy(X, y, classifier):
    # The last 400 datapoints will be used to test the accuracy
    # of our predictions 
    testX = X[-400:,:]
    testTrue = y[-400:]

    testPred = classifier.predict(testX)

    #Calculate model performance
    accuracy = metrics.accuracy_score(testTrue, testPred) 
    
    return accuracy

'''
PURPOSE: calculates the importance that a feature has on
the classifier, from 0 to 100%
PARAMETERS: classifier, features labels (names) 
RETURNS: nothing, prints importance
'''
def calculateFeatureImportance(classifier, labels):
    print("\nFeature Importance:")
    
    #Calculate importance 
    featImportance = classifier.tree_.compute_feature_importances(normalize=True)

    #Convert to numpy array
    labelsArr = labels.to_numpy()

    # Print each feature's importance in percentage
    for i in range(labelsArr.size):
        print(labels[i],"=", round(featImportance[i] * 100, 1), "%")