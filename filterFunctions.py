# *****************************************
# Final Project - Data filter functions
# *****************************************
# COLLABORATION STATEMENTS:
# https://www.programiz.com/python-programming/writing-csv-files
# https://www.geeksforgeeks.org/numpy-quantile-in-python/
# https://www.programiz.com/python-programming/writing-csv-files
# https://stackoverflow.com/questions/36384760/transforming-a-row-vector-into-a-column-vector-in-numpy
# *****************************************

# *****************************************
# Import statements
# *****************************************
import matplotlib.pyplot as plt
import numpy as np
import csv

# *****************************************
# Functions
# *****************************************
'''
PURPOSE: plots the electricity usage histogram. Used to
visualize the distribution in order to find a way to classify
the electricity into categories.
PARAMETERS: electricity usage datapoints, 
RETURNS: nothing 
'''
def plotElectricity(totalE):
    plt.hist(totalE, bins = 50)
    plt.xlabel("Electricity usage (in kilowatts/hour)")
    plt.ylabel("Number of households")
    plt.title("Histogram of electricity usage")
    plt.show()

'''
PURPOSE: classify each electricity usage data point into 
very low (bottom 25%), low (25% to 50%), high (50% to 75%)
or very high (top 25%) using quantiles. 
PARAMETERS: electricity usage datapoints, data length (number
of datapoints)
RETURNS: electricty usage dapoints with values ranging from
1 to 4 
'''
def classifyElectricityUsage(totalE, dataLength):
    #Get quantiles to classify usage
    Q1 = np.quantile(totalE, .25)
    Q2 = np.quantile(totalE, .50)
    Q3 = np.quantile(totalE, .75)

    for i in range(dataLength):
        #25% of households use less than Q1
        #So this is very low energy use
        if (totalE[i] <= Q1):
            totalE[i] = 1

        #25% of households use more than Q3
        #So this is very high energy use
        elif (totalE[i] >= Q3):
            totalE[i] = 4

        #25% of households use more than Q1 and less than Q2
        # So this is low energy use
        elif (totalE[i] <= Q2):
            totalE[i] = 2

        #25% use more than Q2 and less than Q3
        #This is high energy use 
        else:
            totalE[i] = 3
    
    return totalE

'''
PURPOSE: gets input from user about which variables to be
included in this analysis
PARAMETERS: none
RETURNS: array with user input
'''
def query():
    prompt = """
    Input which variables will be analyzed, or END to finish
    Possible options:
    NHSLDMEM    (number of household members)
    MONEYPY     (income)
    KOWNRENT    (owned or rented house)
    AIRCOND     (whether or not it has air conditioner)
    NCOMBATH    (number of bathrooms)
    NUMFRIG     (number of fridges )
    EDUCATION   (respondent's educational level)
    SOLAR       (whether or not solar energy is generated)
    SWIMPOOL    (wheter or not house has a swimming pool)
    LGTINNUM    (number of lightbulbs in the house)
    """
    #Print prompt
    print(prompt)

    # Create list to store variables
    varArray = []

    userIn = input("Input:")
    while userIn != "END":
        varArray.append(userIn)
        userIn = input("Input:")
    
    return varArray

'''
PURPOSE: convert variable codes to more readable names
PARAMETERS: array with inputted variables
RETURNS: array with more readable names to be used when
creating a filtered CSV file
'''
def convert(inputVar):
    #Add IDs to the list
    converted = ["IDS"]

    #For each element, convert code into readable name
    for i in range(len(inputVar)):
        code = inputVar[i]
        if code == "NHSLDMEM":
            converted.append("Num of members")
        elif code == "MONEYPY":
            converted.append("Income")
        elif code == "KOWNRENT":
            converted.append("Own/rent")
        elif code == "AIRCOND":
            converted.append("AC")
        elif code == "NCOMBATH":
            converted.append("Bathrooms")
        elif code == "LGTINNUM":
            converted.append("Lightbulbs")
        elif code == "EDUCATION":
            converted.append("Education level")
        elif code == "DOEID":
            converted.append("ID")
        elif code == "KWH":
            converted.append("Energy usage")
        elif code == "SOLAR":
            converted.append("Solar energy")
        elif code == "NUMFRIG":
            converted.append("Refrigerators")
        # If not on this list, just use its code
        else:
            converted.append(code)

    # Finally, append energy usage to the end
    converted.append("Energy usage")

    print("Inputted data:", converted)
    return converted

'''
PURPOSE: filters from the dataset the variables the user 
requested to be included.
PARAMETERS: array with user input, unfiltered data from 
the dataset
RETURNS: array with household data for selected variables
'''
def filterData(inputVar, data):
    # Create 2D array to hold the variables and
    # add household IDs (0, 1, 2...)
    variables = data['DOEID'] - 10001

    for i in range(len(inputVar)):
        #Get variable name
        varName = inputVar[i]
        #Search it in the CSV file and add to the array
        variables = np.vstack((variables, data[varName]))
    
    #Finally add electricity usage
    variables = np.vstack((variables, data['KWH'])) 

    #Flip the array, so each row represents a member 
    #(not a variable)
    return np.transpose(variables).astype(int)

'''
PURPOSE: outputs the filtered data into a new csv file
to later be used by the decision tree classifier.
PARAMETERS: features/variables labels, array of filtered
variables, name of the file to be created
RETURNS: nothing, but outputs a new csv file
'''
def writeNewCSV(labels, fVariables, filename):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(labels)
        writer.writerows(fVariables)


