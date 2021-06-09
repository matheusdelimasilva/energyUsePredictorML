-------------------------------------------------------------------
|     Predicting household energy usage with Decision Trees       |
| Matt de Lima Silva                                              | 
| 05/14/21                                                        |
-------------------------------------------------------------------

DESCRIPTION: The program allows the user to select which variables to be 
analyzed. Those variables are then used to build a decision tree classifier 
that predicts energy usage (in killowatts/hour) in a US household.

INSTRUCTIONS: 

1. Run dataFilter.py and select which variables will be used in this model.
A few options are printed, but the complete list can be seen here 
(https://drive.google.com/file/d/1ppLAwUb6dLWkKPEaVfLZUhaU3PVvvolA/view?usp=sharing)

2. A filtered CSV (fData.csv) will be generated.

3. Run decisionTree.py to build three different decision tree
algorithms (each one with a different height). 

4. Each classifier's accuracy will be printed. The importance of
each feature/variable for predicting a class will also be printed. 


FILE LIST: 
- data.csv: Original dataset. Includes data from more than 5000
    households in the US.
- dataFilter.py: Script for filtering the original dataset.
- filterFunctions.py: Includes the functions used by dataFilter.py
- fData.csv: File built by dataFilter.py. Filtered version of 
data.csv.
- decisionTree.py: Driver, creates decision trees with data from
fData.csv.
- treeFunctions.py: Includes the functions used by decisionTree.py
- tree.dot: File created by decisionTree.csv. Includes webgraphiz
code used to visualize trees in http://www.webgraphviz.com. 
- README.txt: this file. 

FEATURES DESCRIPTIONS:

Design choices:
    - The original dataset had too much information. So I decided
    to create a program to filter it and generate a new datafile. 
    I then decided to make it to accept user input, so different
    decision trees can be easily created and their accuracies 
    can be compared.

    - The original dataset has the actual energy usage by household.
    However this makes a prediction algorithm hard (if not 
    impossible) to make. So I divided the household energy usages
    into four classes (very low, low, high, very high). "Very low"
    includes the bottom 25% of energy use; "very high" includes the 
    top 25%, and the others the remaining half. This was done by
    calculating the quantiles. 

    - After creating my first decision tree algorithm I did not 
    find a good way to test it. So I decided to get 400 datapoints
    to predict their class. I then compared those predicted classes
    to their original classes so I could get an accuracy score. 

    - After checking accuracy scores I would like to know which 
    specific features were important in predicting a class. So 
    I used a "feature importance" calculator for that. 

    - Separating the driver file from the functions file was good
    for readability and modularity of the program. 

LIBRARIES: 
    - "sklearn trees" was used to create the decision trees
    - "sklearn statistics" was used to calculate the accuracy of
    the trees
    - "pandas" was used to manipulate data from the dataset. 
    - "csv" was used by the filter program to create a new dataset
    file
    
