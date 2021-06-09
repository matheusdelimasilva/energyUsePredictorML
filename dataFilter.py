# *****************************************
# Final Project - Data filter
# *****************************************
# Matheus de Lima Silva
#
# COLLABORATION STATEMENTS:
# https://www.programiz.com/python-programming/writing-csv-files
# https://www.geeksforgeeks.org/numpy-quantile-in-python/
# https://www.programiz.com/python-programming/writing-csv-files
# https://stackoverflow.com/questions/36384760/transforming-a-row-vector-into-a-column-vector-in-numpy
# *****************************************

# *****************************************
# Import statements
# *****************************************
import filterFunctions as f
import pandas as pd


# *****************************************
# DRIVER
# *****************************************

# Open file
filename = "data.csv"
data = pd.read_csv(filename)

# Get columns
columns = data.columns

# Get the electricity usage in an array
totalE = data['KWH'].to_numpy()

# Get how many datapoints are being used
dataLength = totalE.size

# Plot the distribution of electricity usage as a histogram
# print("Plotting energy usage histogram")
# f.plotElectricity(totalE)

# Classify electricity usage into:
# very low (1), low (2), high (3), very high (4)
totalE = f.classifyElectricityUsage(totalE, dataLength)

# These are the variables that will be used in this analysis
inputVar = f.query()

# Convert variable codes to a name
labels = f.convert(inputVar)

# Filter variables that will be used in this analysis
fVariables = f.filterData(inputVar, data)

# Add all filtered data to a new csv file
f.writeNewCSV(labels, fVariables, "fData.csv")

print("Data filtered")