# *****************************************
# Decision Tree Classifier
# *****************************************
# Matheus de Lima Silva
#
# COLLABORATION:
# https://mljar.com/blog/visualize-decision-tree/
# https://www.geeksforgeeks.org/python-decision-tree-regression-using-sklearn/
# https://scikit-learn.org/stable/modules/generated/sklearn.metrics.accuracy_score.html
# https://scikit-learn.org/stable/modules/tree.html
# *****************************************

import treeFunctions as tf
import pandas as pd
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier
from sklearn import metrics

# Load Data
dataset = pd.read_csv("fData.csv")

# Get column names
colNames = dataset.columns

# Get how many variables/features will be analyzed
nFeatures = colNames.size - 1 #-1 to exclude classes (energy use)

# Get labels for variables/features
labels = colNames[1:nFeatures]

# Get X from csv file, these are the features/variables
X = dataset.iloc[:,1:nFeatures].values

# Get y from csv file, these are the classes 
# (low/high energy use)
y = dataset.iloc[:,nFeatures].values

# Classes names
classNames = ["very low", "low", "high", "very high"]

# Create the decision tree classifiers with different depths
classifier1 = DecisionTreeClassifier(max_depth=3)
classifier2 = DecisionTreeClassifier(max_depth=8)
classifier3 = DecisionTreeClassifier()

classifier1.fit(X, y)
classifier2.fit(X, y)
classifier3.fit(X, y)

#Export smallest tree as "tree.dot" for visualization
# (the other are hard to visualize since they have many
# nodes/branches)
tf.exportTree(classifier1, classNames, labels)

# Test prediction accuracy for each classifier
print("Tree 1 Accuracy score:")
print (tf.testAccuracy(X, y, classifier1))

print("Tree 2 Accuracy score:")
print (tf.testAccuracy(X, y, classifier1))

print("Tree 3 Accuracy score:")
print (tf.testAccuracy(X, y, classifier3))

# Print importance of features
tf.calculateFeatureImportance(classifier3, labels)


